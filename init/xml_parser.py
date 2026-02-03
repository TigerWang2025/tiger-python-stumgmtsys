# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
import re
from typing import Dict, Any, Tuple, List


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
                if query_id and sql_elem is not None and sql_elem.text:
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
            # 如果name有值，保留name条件，并将#{name}替换为%s
            query = query.replace('{{if name}}', '').replace('{{/if}}', '')
            query = query.replace('#{name}', '%s')
            values.append(params['name'])
        else:
            query = self._remove_condition_block(query, 'name')

        # 处理id参数
        if 'id' in params and params['id']:
            # 如果id有值，保留id条件,并将#{id}替换为%s
            query = query.replace('{{if id}}', '').replace('{{/if}}', '')
            query = query.replace('#{id}', '%s')
            values.append(params['id'])
        else:
            # 如果id为空，移除id条件块及其后的AND
            query = self._remove_condition_block(query, 'id')

        # # 清理多余的模板标记
        query = query.replace('{{if name}}', '').replace('{{/if}}', '')
        query = query.replace('{{if id}}', '').replace('{{/if}}', '')

        # return query.strip(), values
        # 移除多余的#{name}和#{id}占位符（防止未被条件包含的情况）
        query = query.replace('#{name}', '')
        query = query.replace('#{id}', '')
        # 清理多余空白行
        lines = [line for line in query.split('\n') if line.strip()]
        cleaned_query = '\n'.join(lines)
        return cleaned_query.strip(), values

    def _remove_condition_block(self, query, param_name):
        """移除整个条件块，包括AND关键字"""
        # 使用正则表达式匹配整个条件块，包括AND关键字
        pattern = r'\s*AND\s*[^}]*?#{' + param_name + r'}[^}}]*?(\s*{{if\s+' + param_name + r'}}.*?{{/if}}\s*)?'
        query = re.sub(pattern, '', query, flags=re.DOTALL | re.IGNORECASE)
        # 处理剩余的空条件块标记
        empty_pattern = r'\s*{{if\s+' + param_name + r'}}\s*{{/if}}\s*'
        query = re.sub(empty_pattern, '', query, flags=re.DOTALL)

        return query

    def _cleanup_template_markers(self, query):
        """清理所有残留的模板标记"""
        # 移除所有{{if xxx}}和{{/if}}标记
        query = re.sub(r'\s*{{if\s+\w+}}\s*', '', query)
        query = re.sub(r'\s*{{/if}}\s*', '', query)
        return query

    def process_insert_template(self, query_id: str, params: Dict[str, Any]) -> Tuple[str, List[Any]]:
        """
                处理插入模板，根据参数动态生成SQL
                :param query_id: 查询ID
                :param params: 参数字典
                :return: (SQL语句, 参数值列表)
                """
        template = self.queries.get(query_id)
        if not template:
            raise ValueError(f"未找到ID为'{query_id}'的查询模板")

        processed_sql = template
        values = []

        # 处理所有if-else条件
        if_else_patterns = [
            ('operatorid', 'operatorid'),
            ('operatorname', 'operatorname'),
            ('operatorsex', 'operatorsex'),
            ('operatorbirthdate', 'operatorbirthdate'),
            ('responsibility', 'responsibility'),
            ('operatortel', 'operatortel'),
            ('operatormail', 'operatormail'),
            ('idnumber', 'idnumber'),
            ('createtime', 'createtime'),
            ('updatetime', 'updatetime'),
            ('flag', 'flag'),
            ('isdel', 'isdel')
        ]

        for field, param_key in if_else_patterns:
            pattern = rf'{{{{if {field}.*?}}}}(#{{{field}}}.*?){{{{else}}}}(.*?){{{{/if}}}}'
            matches = re.finditer(pattern, processed_sql, re.DOTALL)

            for match in matches:
                full_match = match.group(0)
                true_part = match.group(1)
                false_part = match.group(2)

                if params.get(param_key) is not None:
                    replacement = true_part.replace(f'#{{{field}}}', '%s')
                    values.append(params[param_key])
                else:
                    replacement = false_part

                processed_sql = processed_sql.replace(full_match, replacement)

        # 清理剩余的模板标记
        processed_sql = re.sub(r'{{if .*?}}|{{else}}|{{/if}}', '', processed_sql)

        return processed_sql.strip(), values
