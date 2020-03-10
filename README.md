# 某疫情统计可视化

## 项目介绍


## 运行方式
运行环境
- Python3 (测试环境为Python3.7)
- Redis

运行方式
1. 安装依赖库
    ```
    pip install -r requirement.txt
    ```
2. 运行Redis服务端 并在config.py中配置Redis路径
    ```Python3
    REDIS_HOST = 'localhost'
    REDIS_PORT = '6379'
    REDIS_DB = 0
    ```
3. 配置Nginx
    ```
    ...
    ```

4. 运行
    ```
    flask run
    ```

## 接口文档

[在这](doc/api/index.md)

## 程序结构