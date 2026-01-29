# -*- coding: utf-8 -*-
import pymysql
from mysql.connector import Error

from init.analysis import PropertiesReader
from init.route import Route


def read_config():
    try:
        # 獲取配置文件路徑，获取配置信息
        config_file_path = Route.get_config_path(dirname='config', filename='config.properties')
        # print("配置文件config.properties的路徑：", config_file_path)
        # 创建配置解析器对象
        config_reader = PropertiesReader(config_file_path)

        # 从配置文件中获取数据库连接信息
        host = config_reader.get('LOCALHOST') or '127.0.0.1'
        # port = config_reader.get('PORT')
        database = config_reader.get('DATABASE') or ''
        username = config_reader.get('DATANAME') or ''
        password = config_reader.get('PASSWORD') or ''
        print("03 读取配置结果：", host)
        return {
            'host': host,
            # 'port': port,
            'database': database,
            'username': username,
            'password': password
        }

    except Exception as e:
        print(f"读取配置文件时发生错误: {e}")
        return None

def create_connection():
    """
    创建MySQL数据库连接
    """
    print("01 创建MySQL数据库连接")
    config_data = read_config()
    print("02 读取配置完成")
    if not config_data:
        print("无法读取配置信息")
        return None

    connection = None

    try:
        # connection = mysql.connector.connect(
        connection = pymysql.connect(
            host=config_data['host'],  # 数据库主机地址
            # port='port',  # 数据库主机地址
            # port=3306,
            database=config_data['database'],  # 数据库名称
            user=config_data['username'],  # 用户名
            password=config_data['password'],  # 密码
            charset='utf8mb4',  # 设置字符集
            autocommit=True  # 自动提交事务
            # connection_timeout=10  # 设置连接超时
        )

        # if connection.is_connected():
        #     db_info = connection.get_server_info()
        #     print("成功连接到MySQL数据库")
        #     print(f"MySQL服务器版本: {db_info}")
        #     return connection
        # 检查连接
        try:
            connection.ping()
            print("000 连接成功")
            return connection
        except Exception as e:
            print("001 连接失败:", e)
            return None


    # except Error as e:
    #     print(f"连接MySQL时发生错误: {e}")
    #     if connection:
    #         try:
    #             connection.close()
    #         except:
    #             pass
    #     return None
    #
    except Exception as e:
        print(f"未知错误: {e}")
        if connection:
            try:
                connection.close()
            except:
                pass
        return None


def close_connection(connection):
    """
    关闭数据库连接
    """
    try:
        if connection:
            connection.close()
            print("MySQL连接已关闭")
    except Exception as e:
        print(f"关闭连接时发生错误: {e}")


def execute_query(connection, query):
    """
    执行查询语句
    """
    if not connection:
        print("数据库连接无效")
        return None

    try:
        # 检查连接状态
        connection.ping(reconnect=True)
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except Error as e:
        print(f"执行查询时发生错误: {e}")
        return None
    except Exception as e:
        print(f"未知错误: {e}")
        return None
