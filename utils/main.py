# -*- coding: utf-8 -*-
import os
import pymysql

from init.route import Route
from init.xml_parser import DynamicQueryBuilder
from query_executor import QueryExecutor


def get_database_connection():
    """获取数据库连接"""
    db_config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '123456',
        'database': 'student',
        'charset': 'utf8mb4'
    }

    try:
        connection = pymysql.connect(**db_config)
        print("数据库连接成功")
        return connection
    except Exception as e:
        print(f"数据库连接失败: {e}")
        return None


def main():
    """主函数 - 演示动态SQL查询的完整流程"""
    # 获取XML文件路径
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # xml_file_path = os.path.join(current_dir, 'operatorQuery.xml')
    xml_file_path = Route.get_config_path(dirname='dbscript', filename='operatorQuery.xml')

    # 检查XML文件是否存在
    if not os.path.exists(xml_file_path):
        print(f"XML配置文件不存在: {xml_file_path}")
        return

    # 获取数据库连接
    connection = get_database_connection()
    if not connection:
        return

    try:
        # 步骤1: 初始化查询构建器(解析XML)
        query_builder = DynamicQueryBuilder(xml_file_path)
        print("步骤1: XML查询解析完成")

        # 测试不同参数组合

        # 测试1: name和id都有值
        print("\n=== 测试1: name和id都有值 ===")
        sql, params = query_builder.build_query('findOperator', name="Admin", id="GMgR2KCLiFCr3wRPEP20GMygzEoWJKHz")
        print(f"生成的SQL: {sql}")
        print(f"参数: {params}")

        executor = QueryExecutor(connection)
        results = executor.execute_query(sql, params)
        print(f"查询结果: {results}")

        # 测试2: 只有name
        print("\n=== 测试2: 只有name ===")
        sql, params = query_builder.build_query('findOperator', name="Test001")
        print(f"生成的SQL: {sql}")
        print(f"参数: {params}")

        results = executor.execute_query(sql, params)
        print(f"查询结果: {results}")

        # 测试3: 只有id
        print("\n=== 测试3: 只有id ===")
        sql, params = query_builder.build_query('findOperator', id="pr8jK0Nb6tlJVQavaElJXil60J6S4LNc")
        print(f"生成的SQL: {sql}")
        print(f"参数: {params}")

        results = executor.execute_query(sql, params)
        print(f"查询结果: {results}")

        # 测试4: 都没有参数
        print("\n=== 测试4: 都没有参数 ===")
        sql, params = query_builder.build_query('findOperator')
        print(f"生成的SQL: {sql}")
        print(f"参数: {params}")

        results = executor.execute_query(sql, params)
        print(f"查询结果: {results}")

    except Exception as e:
        print(f"程序执行出错: {e}")
    finally:
        # 关闭数据库连接
        if connection:
            connection.close()
            print("数据库连接已关闭")


if __name__ == "__main__":
    main()
