- 请求方式

    - GET
    
- 请求URL

    `\api\news`

- 返回示例

    ```
    {
        "news": [
            {
                "title": "\u65b0\u578b\u80ba\u708e\u5b9e\u65f6\u52a8\u6001",
                "url": "https://www.baidu.com/s?wd=\u65b0\u578b\u80ba\u708e\u5b9e\u65f6\u52a8\u6001"
            },{
                "title": "\u6e56\u5317\u4f01\u4e1a\u590d\u5de5\u4e0d\u65e9\u4e8e2.13",
                "url": "https://www.baidu.com/s?wd=\u6e56\u5317\u4f01\u4e1a\u590d\u5de5\u4e0d\u65e9\u4e8e2.13"},
            },{
                ...
            }
        ],
        "fake_news": [
            {
                "title": "\u7eb8\u5e01\u4f1a\u4f20\u64ad\u51a0\u72b6\u75c5\u6bd2",
                "url": "https://www.baidu.com/s?wd=\u7eb8\u5e01\u4f1a\u4f20\u64ad\u51a0\u72b6\u75c5\u6bd2&sa=osari_yaoyan"
            }, {
                "title": "\u5168\u8eab\u55b7\u6d12\u9152\u7cbe\u53ef\u6d88\u6bd2",
                "url": "https://www.baidu.com/s?wd=\u5168\u8eab\u55b7\u6d12\u9152\u7cbe\u53ef\u6d88\u6bd2&sa=osari_yaoyan"
            }, {
                ...            
            }
        ]
    }
    ```
  
- 返回参数说明
    - `news` 热搜
    - `fake_news` 谣言
    