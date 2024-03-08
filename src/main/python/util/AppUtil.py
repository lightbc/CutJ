import os

# 程序名称
app_name = "CutJ"
# 程序保存的根目录名称
app_dir = "CutJ"
# 截屏操作属性配置文件默认名称
props_cfg_name = app_name + "_Props.cfg"
# 图标存放目录
icon_dir = ":/images/resources/images/"
# 程序logo
app_icon = icon_dir + "cut_logo.ico"
# 设置图标
settings_icon = icon_dir + "settings.png"


def getUserPath():
    """获取Windows用户路径"""
    user_path = os.path.expanduser("~")
    return user_path


def getAppDir():
    """获取程序保存内容路径"""
    # 程序保存信息：用户路径+程序路径
    dirPath = getUserPath() + os.sep + app_dir
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    return dirPath


def getTempDir():
    """获取程序缓存目录"""
    tempDir = getAppDir() + os.sep + "temp"
    if not os.path.exists(tempDir):
        os.makedirs(tempDir)
    return tempDir


def getCfgPath():
    """获取配置文件路径"""
    return getAppDir() + os.sep + app_name + ".cfg"


def getPropsCfgPath():
    """获取绘制图形、马赛克、文本内容等的属性配置文件路径"""
    return getAppDir() + os.sep + props_cfg_name
