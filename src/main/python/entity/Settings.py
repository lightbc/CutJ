import json


class Settings:
    """程序配置项实体"""

    def __init__(self, save_path=None):
        # 保存位置
        self.save_path = save_path

    def __str__(self):
        """
        实体转换json字符串
        :return: json 字符串
        """
        nj = json.dumps(self.__dict__)
        return nj

    def to_dict(self):
        """
        字典类型
        :return: dict
        """
        return self.__dict__

    def from_dict(self, data):
        """
        将dict转换成实体
        :param data: 字典数据
        :return: self 实体
        """
        if data:
            for key in self.__dict__.keys():
                # 遍历字典，将字典值赋值对应的实体对象成员变量
                setattr(self, key, data[key])
            return self
        return None
