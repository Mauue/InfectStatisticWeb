# 某疫情统计可视化

## 项目介绍


## 运行方式
运行环境
- Python3.7及以上 (测试环境为Python3.7)
- Redis

运行方式
1. 安装依赖库
    ```
    pip install -r requirements.txt
    ```
2. 运行Redis服务端 并在config.py中配置Redis路径
    ```Python3
    REDIS_HOST = 'localhost'
    REDIS_PORT = '6379'
    REDIS_DB = 0
    ```
3. 配置Nginx
    ```
    server {
        listen 80;
        root <InfectStatisticWeb\frontend的目录路径>;
        index index.html
        server_name  localhost;
        
        location /api/ {
                rewrite ^(/api/.*) /$1 break;   #两个反斜杆
                proxy_pass http://localhost:<服务端的端口号>;
        }  
    }
    ```

4. 运行
    ```
    flask run
    ```

## 接口文档

[GET: `/api/index`](doc/api/index.md)

[GET: `/api/news`](doc/api/news.md)

[GET: `/api/province?name=<省份>`](doc/api/province.md)

## 程序结构