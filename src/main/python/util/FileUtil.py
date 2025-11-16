import os
from PyQt5.QtWidgets import QFileDialog
from entity import DrawProps
from util import AppUtil
from actions import SettingsAction


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


def get_save_path():
    """获取截图保存路径"""
    return SettingsAction.load_settings().save_path


def choose_save_dir(parent=None, dir_path=AppUtil.getTempDir()):
    """
    选择文件夹目录
    :param parent: 父级组件
    :param dir_path: 文件夹路径
    :return: 选择路径
    """
    return QFileDialog.getExistingDirectory(parent, "保存位置", dir_path)


def loadPropsCfg():
    """
    加载再编辑属性配置文件
    :return: 配置内容
    """
    dp = DrawProps.DrawProps()
    cfg_path = is_valid_path(get_save_path()) if get_save_path() else AppUtil.getPropsCfgPath()
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
    cfg_path = is_valid_path(get_save_path()) if get_save_path() else AppUtil.getPropsCfgPath()
    data = o.toJsonStr()
    return write(cfg_path, data)


def is_valid_path(path):
    """判断路径是否存在"""
    return os.path.exists(path)
