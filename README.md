# 某疫情统计可视化

## 项目介绍

|这个作业属于哪个课程|[班级链接](https://edu.cnblogs.com/campus/fzu/2020SpringW)|
|:--- |:---:|
|这个作业要求在哪里|[作业链接](https://edu.cnblogs.com/campus/fzu/2020SpringW/homework/10456)|
|结对学号   |	221701133 021700511|
|这个作业的目标|某次疫情统计可视化的实现|
|作业正文|....  |
|其他参考文献|... |

## 运行方式
运行环境
- Python3.7或3.7以上版本 (测试环境为Python3.7)
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
3. 使用Nginx部署

    Nginx配置信息
    ```
    server {
        listen 80;
        root <InfectStatisticWeb\frontend的目录路径>;
        index index.html
        server_name  localhost;
        
        location /api/ {
                rewrite ^(/api/.*) /$1 break; 
                proxy_pass http://localhost:<服务端的端口号>;
        }  
    }
    ```

4. 运行
    ```
    flask run -p 端口号 
    ```

## 接口文档

获取主页数据: `/api/index` [接口文档](doc/api/index.md)

获取新闻数据：`/api/news` [接口文档](doc/api/news.md)

获取省份数据：`/api/province?name=<省份>`[接口文档](doc/api/province.md)
