# -*- coding: utf-8 -*-
import pymysql


class QueryExecutor:
    def __init__(self, connection):
        self.connection = connection

    def execute_query(self, sql, params=None):
        """
        执行SQL查询并返回结果
        """
        try:
            print(f"执行SQL: {sql}")
            print(f"参数: {params}")

            with self.connection.cursor() as cursor:
                if params:
                    cursor.execute(sql, params)
                else:
                    cursor.execute(sql)
                results = cursor.fetchall()
                return results

        except Exception as e:
            print(f"执行查询时出错: {e}")
            return []
