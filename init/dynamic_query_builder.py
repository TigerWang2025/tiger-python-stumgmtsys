# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET



class DynamicQueryBuilder:
    def __init__(self, xml_file_path):
        self.xml_file_path = xml_file_path
        self.queries = {}
        self._parse_xml()

    def _parse_xml(self):
        """解析XML配置文件，加载查询语句"""
        try:
            tree = ET.parse(self.xml_file_path)
            root = tree.getroot()

            for query_elem in root.findall('query'):
                query_id = query_elem.get('id')
                sql_elem = query_elem.find('sql')
                if query_id and sql_elem is not None:
                    self.queries[query_id] = sql_elem.text.strip()
        except Exception as e:
            print(f"解析XML文件时出错: {e}")

    def build_query(self, query_id, **params):
        """
        根据参数动态构建查询语句
        只使用一个通用SQL语句，根据参数是否为空动态添加条件
        """
        base_query = self.queries.get(query_id)
        if not base_query:
            return None, []

        # 处理条件参数
        query = base_query
        values = []

        # 处理name参数
        if 'name' in params and params['name']:
            # 如果name有值，保留name条件
            query = query.replace('{{if name}}', '').replace('{{/if}}', '')
            values.append(params['name'])
        else:
            # 如果name为空，移除name条件块
            start = query.find('{{if name}}')
            end = query.find('{{/if}}')
            if start != -1 and end != -1:
                query = query[:start] + query[end + 7:]

        # 处理id参数
        if 'id' in params and params['id']:
            # 如果id有值，保留id条件
            query = query.replace('{{if id}}', '').replace('{{/if}}', '')
            values.append(params['id'])
        else:
            # 如果id为空，移除id条件块
            start = query.find('{{if id}}')
            end = query.find('{{/if}}')
            if start != -1 and end != -1:
                query = query[:start] + query[end + 6:]

        # 清理多余的模板标记
        query = query.replace('{{if name}}', '').replace('{{/if}}', '')
        query = query.replace('{{if id}}', '').replace('{{/if}}', '')

        return query.strip(), values


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
