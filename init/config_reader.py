# -*- coding: utf-8 -*-
import configparser
import os
from init.route import Route
from init.analysis import PropertiesReader

def read_config():

    try:
        # 獲取配置文件路徑，获取配置信息
        config_file_path = Route.get_config_path(filename='config.properties')
        # print("配置文件config.properties的路徑：", config_file_path)
        # 创建配置解析器对象
        config = PropertiesReader(config_file_path)

        # 从配置文件中获取数据库连接信息
        host = config.get('LOCALHOST')
        port = config.get('PORT')
        database = config.get('DATABASE')
        username = config.get('DATANAME')
        password = config.get('PASSWORD')

        return {
            'host': host,
            'port': port,
            'database': database,
            'username': username,
            'password': password
        }

    except Exception as e:
        print(f"读取配置文件时发生错误: {e}")
        return None


def init_database_connection():
    """
    使用配置文件中的信息初始化数据库连接
    """
    # 读取配置
    db_config = read_config()

    if db_config:
        print("配置信息读取成功:")
        print(f"主机: {db_config['host']}")
        print(f"数据库: {db_config['database']}")
        print(f"用户名: {db_config['username']}")
        # 注意：密码不打印到控制台，实际使用时应谨慎处理

        # 这里可以使用db_config中的信息来初始化数据库连接
        # 例如使用mysql-connector-python或pymysql等库
        return db_config
    else:
        print("配置文件读取失败")
        return None


# if __name__ == "__main__":
#     # 测试配置读取功能
#     config_info = init_database_connection()
#     if config_info:
#         print("数据库初始化配置完成")
#     else:
#         print("数据库初始化配置失败")
