from datetime import datetime

import requests
import re
import json
import logging
from db import Redis
from config import Config


_URL = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3"
_storage_name_chinese = {
    '确诊': 'confirmed',
    '疑似': 'unconfirmed',
    '治愈': 'cured',
    '死亡': 'died',
    '当前确诊': 'NowConfirm',
    '新增当前确诊': 'NewConfirm',
    '新增确诊': 'NewNowConfirmed',
    '新增疑似': 'NewUnconfirmed',
    '新增治愈': 'NewCured',
    '新增死亡': 'NewDied'
}
# 只需要用得到的数据
_storage_name_in_baidu = {
    'confirmed': 'confirmed',
    'died': 'died',
    'cured': 'cured',
    'unConfirmed': 'unconfirmed',
    'confirmedRelative': 'NewConfirmed',
    'unconfirmedRelative': 'NewUnconfirmed',
    'curedRelative': 'NewCured',
    'diedRelative': 'NewDied',
    'curConfirm': 'NowConfirm',
    'curConfirmRelative': 'NewNowConfirm'
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


def get_china_data(data):
    china_data = {}
    for key in data:
        if key in _storage_name_in_baidu:
            china_data.update({
                _storage_name_in_baidu[key]: data[key]
            })
    return china_data


def get_province_data(data):
    _data = []
    for i in data:
        province_data = {'name': i['area']}
        for key in _storage_name_in_baidu:

            k = key if key != 'cured' else 'crued'
            if k not in i:
                continue

            province_data.update({
                _storage_name_in_baidu[key]: i[k] or 0
            })
        _data.append(province_data)
    return _data


def get_china_trend_data(data):
    trend_data_dict = {
        'date': data['updateDate'],
        'data': None
    }
    trend_data_list = []
    for i in data['list']:
        trend_data_list.append({
            'name': _storage_name_chinese[i['name']],
            'data': i['data']
        })
    trend_data_dict['data'] = trend_data_list
    return trend_data_dict


def set_all_data_task():
    logging.warning('正在更新数据')
    _data = _get_data()
    if _data and _data['component'] and _data['component'][0]:
        data = _data['component'][0]
        index_page_data = {
            'china_data': get_china_data(data['summaryDataIn']),
            'province_data': get_province_data(data['caseList']),
            'chine_trend_data': get_china_trend_data(data['trend'])
        }
        Redis.set(Config.INDEX_PAGE_DATA_KEY, json.dumps(index_page_data))

        logging.info('数据更新完毕')
    else:
        logging.warning('无法获取数据')


if __name__ == "__main__":
    set_all_data_task()
