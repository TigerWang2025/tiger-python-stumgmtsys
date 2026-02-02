# -*- coding: utf-8 -*-
from pathlib import Path


class Route:
    _config_path = None
    _resource_path = None
    _config_filename = None
    _config_dirname = None

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
        if cls._config_filename is None or cls._config_filename == "":
            cls._config_path = project_dir / cls._config_filename
        else:
            cls._config_path = project_dir / cls._config_dirname / cls._config_filename

        # # 构建资源文件路径
        cls._resource_path = project_dir / 'resource'

        return cls._config_path

    @classmethod
    def get_config_path(cls, dirname=None, filename=None):
        """
        获取配置文件路径，支持每次调用时使用不同的参数
        """
        # 每次调用都重新计算路径，不依赖之前的缓存
        if dirname is not None or filename is not None:
            # 临时构建路径，不修改类的缓存状态
            project_dir = Path(__file__).resolve().parent.parent.absolute()
            if filename is None:
                filename = cls._config_filename
            if dirname is None:
                dirname = cls._config_dirname

            if dirname is None or dirname == "":
                return project_dir / filename
            else:
                return project_dir / dirname / filename
        else:
            # 如果没有传参，使用缓存的路径
            if cls._config_path is None:
                cls.read_config()
            return cls._config_path

    @classmethod
    def get_resource_path(cls):
        if cls._resource_path is None:
            cls.read_config()
        return cls._resource_path

    # @classmethod
    # def clear_cache(cls):
    #     """
    #     清理路径缓存
    #     """
    #     cls._config_path = None
    #     cls._resource_path = None
    #     cls._config_filename = None
    #     cls._config_dirname = None