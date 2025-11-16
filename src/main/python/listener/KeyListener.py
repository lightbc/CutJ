import sys
from util import ScreenShot
from PyQt5.QtWidgets import QApplication
from pynput import keyboard


def showCutWin():
    """显示截屏窗体区域"""
    app = QApplication(sys.argv)
    win = ScreenShot.Window()
    win.show()
    app.exec_()


class CutKeyListener:
    """截屏快捷键监听"""

    def __init__(self):
        # alt键是否按下
        self.is_alt = False
        self.listener()

    def on_press(self, key):
        if key == keyboard.Key.alt_l:
            self.is_alt = True
        # 打开截图(alt + a)
        if self.is_alt and key == keyboard.KeyCode.from_char('a'):
            showCutWin()
            self.is_alt = False

    def on_release(self, key):
        if key == keyboard.Key.alt_l:
            self.is_alt = False

    def listener(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
