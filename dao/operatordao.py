class OperatorDAO:
    def __init__(self, connection, query_builder):
        self.connection = connection
        self.query_builder = query_builder

    def find_operators(self, name=None, id=None):
        """
        根据name和id查询操作员，使用一个通用SQL语句
        支持参数为空的情况，动态构建查询条件
        """
        try:
            # 构建动态查询
            query, values = self.query_builder.build_query(
                'findOperator',
                name=name,
                id=id
            )

            if not query:
                print("无法构建查询语句")
                return []

            print(f"执行SQL: {query}")
            print(f"参数: {values}")

            with self.connection.cursor() as cursor:
                cursor.execute(query, values)
                results = cursor.fetchall()
                return results

        except Exception as e:
            print(f"查询操作员时出错: {e}")
            return []
