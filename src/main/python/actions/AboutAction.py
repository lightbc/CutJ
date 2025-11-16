import sys
from ui import About
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication
from util import AppUtil, WindowUtil

# 版本信息
version = "v1.0.2"


class AboutAction(QDialog, About.Ui_Dialog):
    """
    程序相关介绍、作者信息等
    """

    def __init__(self):
        super(AboutAction, self).__init__()
        self.setupUi(self)
        WindowUtil.setIcon(self, AppUtil.app_icon)
        self.version.setText(version)
        # 不显示帮助按钮
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)


def show_about():
    """显示关于对话框，展示相关内容"""
    app = QApplication(sys.argv)
    dialog = AboutAction()
    dialog.show()
    dialog.exec_()
