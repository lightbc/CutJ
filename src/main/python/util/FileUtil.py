import os
from PyQt5.QtWidgets import QFileDialog
from entity import DrawProps
from util import AppUtil


def read(path):
    """
    读取文件内容
    :param path: 路径
    :return: 文件内容
    """
    r = None
    try:
        if path and os.path.exists(path):
            file = open(path, encoding='UTF-8')
            ct = file.read()
            file.close()
            r = ct
    except Exception as e:
        raise e
    finally:
        return r


def write(path, content):
    """
    写入文件内容
    :param path: 路径
    :param content 内容
    :return: true-写入成功，false-写入失败
    """
    b = False
    try:
        if path:
            file = open(path, 'w', encoding='UTF-8')
            file.write(content)
            file.close()
            b = True
    except Exception as e:
        raise e
    finally:
        return b


def choose_save_dir(parent=None, dir_path=AppUtil.getTempDir()):
    """
    选择文件夹目录
    :param parent: 父级组件
    :param dir_path: 文件夹路径
    :return: 选择路径
    """
    return QFileDialog.getExistingDirectory(parent, "保存位置", dir_path)


def loadFontsDict():
    """
    加载字体列表项
    :return: 字体字典
    """
    res = {}
    # 加载字体文件路径
    fonts_path = os.path.abspath("../resources/fonts.txt")
    content = read(fonts_path)
    # 处理加载的字体文件内容，将内容转换为字典类型
    if content and content.strip():
        content = content.strip()
        contents = content.split("\n")
        for c in contents:
            if c and c.strip():
                c = c.strip()
                kv = c.split("=")
                res[kv[0]] = kv[1]
    return res


def loadPropsCfg():
    """
    加载再编辑属性配置文件
    :return: 配置内容
    """
    dp = DrawProps.DrawProps()
    cfg_path = AppUtil.getPropsCfgPath()
    rs = read(cfg_path)
    if rs and len(rs) > 0:
        try:
            dt = DrawProps.toDict(rs)
            dp = dp.toObj(dt)
        except Exception as e:
            raise e
    else:
        updatePropsCfg(dp)
    return dp


def updatePropsCfg(o: DrawProps.DrawProps):
    """
    更新再编辑属性配置文件内容
    :param o: 配置信息
    :return: true-更新成功，false-更新失败
    """
    cfg_path = AppUtil.getPropsCfgPath()
    data = o.toJsonStr()
    return write(cfg_path, data)
