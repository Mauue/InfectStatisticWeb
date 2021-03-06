from datetime import datetime

import requests
import re
import json
import logging
from db import Redis
from config import Config
from urllib.parse import quote, unquote

_URL = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3&city=福建-福建"
_URL_PROVINCE = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3&city={0}-{0}"
_storage_name_chinese = {
    '确诊': 'confirmed',
    '疑似': 'unconfirmed',
    '治愈': 'cured',
    '死亡': 'died',
    '当前确诊': 'nowConfirm',
    '新增当前确诊': 'newConfirm',
    '新增确诊': 'newNowConfirmed',
    '新增疑似': 'newUnconfirmed',
    '新增治愈': 'newCured',
    '新增死亡': 'newDied'
}
# 只需要用得到的数据
_storage_name_in_baidu = {
    'confirmed': 'confirmed',
    'died': 'died',
    'cured': 'cured',
    'unconfirmed': 'unconfirmed',
    'confirmedRelative': 'newConfirmed',
    'unconfirmedRelative': 'newUnconfirmed',
    'curedRelative': 'newCured',
    'diedRelative': 'newDied',
    'curConfirm': 'nowConfirm',
    'curConfirmRelative': 'newNowConfirm'
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
    _dict = {}
    for i in data['list']:
        _dict.update({
            _storage_name_chinese[i['name']]: i['data']
        })
    trend_data_dict['data'] = _dict
    return trend_data_dict


def get_news_data(news_data, fake_news_data):
    news_list = []
    fake_news_list = []
    for _news in news_data:
        news = {
            'title': _news['query'],
            'url': 'https://www.baidu.com/s?wd={}'.format(_news['query'])
        }
        news_list.append(news)
    for _fake_news in fake_news_data:
        fake_news = {
            'title': _fake_news['query'],
            'url': 'https://www.baidu.com/s?wd={}&sa=osari_yaoyan'.format(_fake_news['query'])
        }
        fake_news_list.append(fake_news)
    return {
        'news': news_list,
        'fake_news': fake_news_list
    }


def get_province_trend_data(data, summary_data):
    province_trend_data = []
    summary_data_dict = {}
    for i in summary_data:
        name = i.pop('name')
        summary_data_dict.update({
            name: i
        })

    for _province_data in data:
        data_list = _province_data['trend']['list']
        for i in data_list:
            i['name'] = _storage_name_chinese[i['name']]
        trend_data = {}
        for i in data_list:
            trend_data.update({
                i['name']: i['data']
            })
        province_data = {
            'name': _province_data['name'],
            'date': _province_data['trend']['updateDate'],
            'trend_data': trend_data,
            'summary_data': summary_data_dict[_province_data['name']]
        }
        province_trend_data.append(province_data)

    return province_trend_data


def set_all_data_task():
    logging.warning('正在更新数据')
    _data = _get_data()
    if _data and _data['component'] and _data['component'][0]:
        data = _data['component'][0]
        province_summary_data = get_province_data(data['caseList'])
        index_page_data = {
            'china_data': get_china_data(data['summaryDataIn']),
            'province_data': province_summary_data,
            'china_trend_data': get_china_trend_data(data['trend'])
        }
        Redis.set(Config.INDEX_PAGE_DATA_KEY, json.dumps(index_page_data))

        news_data = get_news_data(data['hotwords'], data['gossips'])
        Redis.set(Config.NEWS_DATA_KEY, json.dumps(news_data))

        province_trend_data = get_province_trend_data(data['provinceTrendList'], province_summary_data)
        for province in province_trend_data:
            Redis.set(province['name'], json.dumps(province))

        logging.info('数据更新完毕')
    else:
        logging.warning('无法获取数据')


if __name__ == "__main__":
    set_all_data_task()