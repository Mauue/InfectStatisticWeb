- 请求方式

    - GET
    
- 请求URL

    `\api\province?name=<省份名>`
    
    - 例如  `\api\province?name=福建`
    
    - 若不加参数或省份不存在会返回空白数据

- 返回示例

```
{
  "name": "福建",
  "date": [
    "1.26",
    "1.27",
    ...,
    "3.12"
  ],
  "trend_data": {
    "confirmed": [29, 59, ..., 296],
    "cured": ...,
    "died": ...,
    "newNowConfirmed": ...,
  },
  "summary_data": {
    "confirmed": "296",
    "died": "1",
    "cured": "295",
    "newConfirmed": "0",
    "newCured": "0",
    "newDied": "0",
    "nowConfirm": "0",
    "newNowConfirm": "0"
  }
}
```

- 返回参数说明
    - `name` 省份名字
    - `date` 数据日期范围
    - `trend_data` 趋势数据
    - `summary_data` 总数据