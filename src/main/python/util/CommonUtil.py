import time


def getTempImageFileName():
    """
    获取临时截图文件文件名
    :return: 图片文件名
    """
    timestamp = int(time.time())
    return f"{timestamp}.png"
