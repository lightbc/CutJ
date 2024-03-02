import uuid


def getUUID():
    """UUID:移除-"""
    uid = uuid.uuid1()
    return str(uid).replace("-", "")


def getTempImageFileName():
    """
    获取临时截图文件文件名
    :return: 图片文件名
    """
    return getUUID() + ".png"
