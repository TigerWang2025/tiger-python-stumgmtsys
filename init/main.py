# -*- coding: utf-8 -*-
import pymysql
from dynamic_query_builder import DynamicQueryBuilder, OperatorDAO
from init.mysql_connection import create_connection, execute_query, close_connection


def main():
    # 创建XML配置文件
    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<queries>
    <query id="findOperator">
        <description>根据name和id动态查询操作员</description>
        <sql><![CDATA[
            SELECT * FROM operator 
            WHERE 1=1 
            {{if name}}
                AND name = #{name}
            {{/if}}
            {{if id}}
                AND id = #{id}
            {{/if}}
        ]]></sql>
    </query>
</queries>
'''
    with open('query_config.xml', 'w', encoding='utf-8') as f:
        f.write(xml_content)

    # 数据库连接配置
    db_config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'password',
        'database': 'test_db',
        'charset': 'utf8mb4'
    }

    try:
        # connection = pymysql.connect(**db_config)
        connection = create_connection()
        print("数据库连接成功")

        # 初始化查询构建器
        query_builder = DynamicQueryBuilder('query_config.xml')

        # 初始化操作员DAO
        operator_dao = OperatorDAO(connection, query_builder)

        print("\n=== 测试1: 只根据name查询 ===")
        results = operator_dao.find_operators(name="张三")
        print(f"查询结果: {results}")

        print("\n=== 测试2: 只根据id查询 ===")
        results = operator_dao.find_operators(id=1)
        print(f"查询结果: {results}")

        print("\n=== 测试3: name和id都传 ===")
        results = operator_dao.find_operators(name="李四", id=2)
        print(f"查询结果: {results}")

        print("\n=== 测试4: 都不传 ===")
        results = operator_dao.find_operators()
        print(f"查询结果: {results}")

    except Exception as e:
        print(f"程序执行出错: {e}")
    finally:
        if 'connection' in locals():
            # connection.close()
            close_connection(connection)
            print("数据库连接已关闭")


if __name__ == "__main__":
    main()
