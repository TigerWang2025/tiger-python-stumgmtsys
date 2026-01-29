# -*- coding: utf-8 -*-
from pathlib import Path


class Route:
    _config_path = None
    _resource_path = None

    @classmethod
    def set_config_filename(cls, dirname, filename):
        """
        设置配置文件名
        """
        cls._config_filename = filename
        cls._config_dirname = dirname
        cls._config_path = None  # 重置配置路径，下次获取时会重新构建

    @classmethod
    def read_config(cls, dirname=None, filename=None):
        if filename:
            cls._config_filename = filename
        if dirname:
            cls._config_dirname = dirname

        # 获取根路径位置
        project_dir = Path(__file__).resolve().parent.parent.absolute()

        # 构建配置文件路径
        # cls._config_path = project_dir / 'config' / 'config.properties'
        if dirname is None or dirname == "":
            cls._config_path = project_dir / cls._config_filename
        else:
            cls._config_path = project_dir / cls._config_dirname / cls._config_filename

        # # 构建资源文件路径
        cls._resource_path = project_dir / 'resource'

        # return cls._config_path, cls._resource_path
        return cls._config_path

    @classmethod
    def get_config_path(cls, dirname=None, filename=None):
        if cls._config_path is None:
            cls.read_config(dirname, filename)
        return cls._config_path

    @classmethod
    def get_resource_path(cls):
        if cls._resource_path is None:
            cls.read_config()
        return cls._resource_path
