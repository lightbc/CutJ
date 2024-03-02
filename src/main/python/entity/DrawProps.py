import json


def toDict(sData):
    """将JSON字符串数据转换成字典类型"""
    return json.loads(sData)


class DrawProps(object):
    """绘制图形或添加文本时，需要的属性参数实体类"""

    def __init__(self):
        # 笔刷大小-默认最小
        self.brush = "small"
        # 绘制画笔颜色-默认红色
        self.defaultColor = "255, 0, 0"
        # 文本颜色-默认红色
        self.txtColor = "255, 0, 0"
        # 字体类型-默认微软雅黑
        self.fontFamily = "微软雅黑"
        # 字体大小-默认8
        self.fontSize = "8"
        # 字体加粗-默认不加粗
        self.bold = False
        # 字体斜体-默认非斜体
        self.italic = False
        # 字体下划线-默认无下划线
        self.underLine = False

    def toJsonStr(self):
        """将字典类型转换成JSON字符串"""
        return json.dumps(self.__dict__)

    def toObj(self, dictData):
        """
        将字典类型数据转换成实体对象
        :param dictData: 字典类型数据
        :return: 实体对象
        """
        if dictData:
            for key in self.__dict__.keys():
                # 遍历字典，将字典值赋值对应的实体对象成员变量
                setattr(self, key, dictData[key])
            return self
        return None
