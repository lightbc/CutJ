import images
import pyautogui
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon


def get_pix_map(path):
    """
    获取象图对象
    :param path: 图标路径
    :return: 象图对象
    """
    pxm = QPixmap(path)
    rw = pxm.width() / screen_width()
    rh = pxm.height() / screen_height()
    ration = max(rw, rh)
    pxm.setDevicePixelRatio(ration)
    return pxm


def screen_size():
    """屏幕尺寸"""
    return pyautogui.size()


def screen_width():
    """屏幕宽度"""
    return screen_size().width


def screen_height():
    """屏幕高度"""
    return screen_size().height


def setIcon(target, icon_path):
    """
    设置固定图标
    :param target: 设置目标
    :param icon_path: 图标路径
    """
    icon = QIcon()
    pix_map = get_pix_map(icon_path)
    icon.addPixmap(pix_map, QIcon.Normal, QIcon.Off)
    target.setWindowIcon(icon)


def getIcon(path):
    """
    获取图标
    :param path: 图标路径
    :return: icon
    """
    icon = QIcon()
    icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
    return icon
