from datetime import datetime

import requests
import re
import json
import logging
from db import Redis
from config import Config


_URL = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3"
_storage_name = {
    '确诊': 'confirmed',
    '疑似': 'suspected',
    '治愈': 'cured',
    '死亡': 'died',
    '当前确诊': 'NowConfirm',
    '新增确诊': 'NewConfirm',
    '新增疑似': 'NewSuspected',
    '新增治愈': 'NewCured',
    '新增死亡': 'NewDied'
}
_storage_name_in_baidu = {
    '确诊': 'confirmed',
    '治愈': 'crued',
    '死亡': 'died',
    '当前确诊': 'curConfirm',
    '新增确诊': 'curConfirmRelative',
    '新增治愈': 'curedRelative',
    '新增死亡': 'diedRelative'
}


def _get_data():
    resp = requests.get(_URL)
    _pattern = r'<script type="application/json" id="captain-config">(.*?)</script>'
    result = re.search(_pattern, resp.text)
    if result is not None:
        text = result.group(1)
        try:
            data = json.loads(bytes(text, encoding="utf-8"))
            return data
        except json.JSONDecodeError:
            pass
    return None


def set_chine_data(data):
    if not isinstance(data, list):
        return
    china_data = {}
    for i in data:
        china_data[_storage_name[i['name']]] = i['data'][-1]
    # 计算当前确诊
    china_data['NowConfirm'] = china_data['confirmed'] - china_data['cured'] - china_data['died']
    # 更新日期
    china_data['update_time'] = datetime.now().isoformat(sep=' ', timespec='seconds')
    Redis.set(Config.CHINA_DATA_KEY, json.dumps(china_data))


def set_province_data(data):
    if not isinstance(data, list):
        return
    Redis.clear_list(Config.PROVINCES_DATA_KEY)
    for i in data:
        province_data = {'name': i['area']}
        for k in _storage_name_in_baidu:
            province_data.update({
                _storage_name[k]: i[_storage_name_in_baidu[k]] or 0
            })
        Redis.rpush(Config.PROVINCES_DATA_KEY, json.dumps(province_data))


def set_all_data_task():
    logging.warning('正在更新数据')
    _data = _get_data()
    if _data and _data['component'] and _data['component'][0]:
        data = _data['component'][0]
        set_chine_data(data['trend']['list'])
        set_province_data(data['caseList'])
        logging.info('数据更新完毕')
    else:
        logging.warning('无法获取数据')


if __name__ == "__main__":
    set_all_data_task()
