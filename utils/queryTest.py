# -*- coding: utf-8 -*-
# 使用示例
from init.mysql_connection import create_connection, execute_query, close_connection

if __name__ == "__main__":
    # 创建连接
    conn = create_connection()

    if conn:
        try:
            # 执行查询
            query = "SELECT VERSION()"
            results = execute_query(conn, query)

            if results:
                print("MySQL版本信息:")
                for row in results:
                    print(row[0])

            # 查询operator表数据总数
            query = "SELECT COUNT(*) FROM operator"
            results = execute_query(conn, query)
            if results:
                print(f"\noperator表记录数: {results[0][0]}")

            # 查询operator表数据详情
            queryDetail = "SELECT * FROM operator"
            resultsDetail = execute_query(conn, queryDetail)
            print("chax jeig :", resultsDetail)



        except Exception as e:
            print(f"执行查询时发生异常: {e}")
        finally:
            # 关闭连接
            close_connection(conn)
    else:
        print("999 未能建立数据库连接")