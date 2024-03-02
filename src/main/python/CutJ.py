import pystray
import threading
from PIL import Image
from actions import AboutAction, SettingsAction
from listener import KeyListener
from util import AppUtil


def settings():
    """展示程序配置对话框"""
    SettingsAction.show_settings()


def about():
    """展示程序描述信息对话框"""
    AboutAction.show_about()


class CutJ:
    """截屏工具CutJ主程"""

    def __init__(self):
        self.app = None
        """开启守护线程，监听截屏快捷键"""
        td = threading.Thread(target=KeyListener.CutKeyListener, daemon=True)
        td.start()
        self.tray_menu()

    def tray_menu(self):
        """托盘菜单"""
        im = Image.open(AppUtil.app_icon)
        tray_menu = (
            pystray.MenuItem("设置", settings),
            pystray.MenuItem("关于", about),
            pystray.MenuItem("退出", lambda: self.exit_sys()),
            # pystray.MenuItem("打开截图", action=KeyListener.showCutWin, default=True, visible=False)
        )
        self.app = pystray.Icon("CutJ", im, "CutJ", tray_menu)
        self.app.run()

    def exit_sys(self):
        """退出主程"""
        if self.app:
            self.app.stop()


if __name__ == "__main__":
    CutJ()
