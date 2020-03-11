- 请求方式

    - GET
    
- 请求URL

    `\api\index`

- 返回示例
    ```
    {
        "china_data": {
            "confirmed": "80933",
            "died": "3140",
            "cured": "60237", 
            "NewConfirmed": "20", 
            "NewUnconfirmed": "36", 
            "NewCured": "1298", "NewDied": "17", 
            "NowConfirm": "17556", 
            "NewNowConfirm": "-1295"
        }, 
        "province_data": [
            {
                "name": "\u897f\u85cf",
                "confirmed": "1",
                "died": 0, 
                "cured": "1", 
                "NewConfirmed": "0", 
                "NewCured": "0", 
                "NewDied": "0", 
                "NowConfirm": "0", 
                "NewNowConfirm": "0"
            }, {
                ...
            }
        ],
        "chine_trend_data": {
            "date": [
                "1.26", 
                ..., 
                "3.9"
            ],
            "data": [
                {
                    "name": "confirmed",
                    "data": [
                        1,
                        ...,
                        80924
                    ]
                }, {
                ...
                }, {
                    "name": "NewDied",
                    "data": [...]
                }
            ]
        }
    }
    ```

- 返回参数说明
    - `china_data` 全国数据总榜
    - `province_data` 各省数据
    - `china_trend_data`  全国数据趋势