# -*- coding: utf-8 -*-
import mysql.connector
import config
from mysql.connector import Error

from init.analysis import PropertiesReader
from init.route import Route
def read_config():
    try:
        # 獲取配置文件路徑，获取配置信息
        config_file_path = Route.get_config_path(filename='config.properties')
        # print("配置文件config.properties的路徑：", config_file_path)
        # 创建配置解析器对象
        config = PropertiesReader(config_file_path)

        # 从配置文件中获取数据库连接信息
        host = config.get('LOCALHOST')
        # port = config.get('PORT')
        database = config.get('DATABASE')
        username = config.get('DATANAME')
        password = config.get('PASSWORD')

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
    config_data = read_config()
    try:
        connection = mysql.connector.connect(
            host=config_data['host'],  # 数据库主机地址
            # port='port',  # 数据库主机地址
            # port=3306,
            database=config_data['database'],  # 数据库名称
            user=config_data['username'],  # 用户名
            password=config_data['password']  # 密码
        )

        if connection.is_connected():
            print("成功连接到MySQL数据库")
            return connection

    except Error as e:
        print(f"连接MySQL时发生错误: {e}")
        return None


def close_connection(connection):
    """
    关闭数据库连接
    """
    if connection and connection.is_connected():
        connection.close()
        print("MySQL连接已关闭")


def execute_query(connection, query):
    """
    执行查询语句
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except Error as e:
        print(f"执行查询时发生错误: {e}")
        return None


# 使用示例
if __name__ == "__main__":
    # 创建连接
    conn = create_connection()

    if conn:
        # 执行查询
        query = "SELECT * FROM operator LIMIT 10"
        results = execute_query(conn, query)

        if results:
            print("查询结果:")
            for row in results:
                print(row)

        # 关闭连接
        close_connection(conn)
