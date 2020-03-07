import requests
import re
import json
import logging
from db import Redis

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


def set_all_data():
    _data = _get_data()
    if _data and _data['component'] and _data['component'][0]:
        data = _data['component'][0]
        set_chine_data(data['trend']['list'])
    else:
        logging.warning('无法获取数据')


def set_chine_data(data):
    if not isinstance(data, list):
        return
    china_data = {}
    for i in data:
        china_data[_storage_name[i['name']]] = i['data'][-1]

    Redis.set('china-data', json.dumps(china_data))



if __name__ == "__main__":
    set_all_data()