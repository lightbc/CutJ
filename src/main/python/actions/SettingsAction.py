import sys
import json
import Settings
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication
from util import FileUtil, AppUtil
from entity import Settings as cfg

# 程序配置文件路径
cfg_path = AppUtil.getCfgPath()


def default_config():
    """加载默认配置项参数"""
    save_path = AppUtil.getTempDir()
    return cfg.Settings(save_path)


def load_settings():
    """加载配置项参数"""
    cfg_json = default_config()
    config = FileUtil.read(cfg_path)
    has_cfg = False
    if config:
        try:
            cJson = json.loads(config)
            if len(cJson) > 0:
                st = cfg.Settings()
                cfg_json = st.from_dict(cJson)
                has_cfg = True
        except Exception as e:
            raise e
    if not has_cfg:
        FileUtil.write(cfg_path, cfg_json.__str__())
    return cfg_json


def save_settings(data):
    """保存配置项参数"""
    FileUtil.write(cfg_path, data)


class SettingsAction(QDialog, Settings.Ui_Form):
    """
    程序相关配置项对话框
    """

    def __init__(self):
        super(SettingsAction, self).__init__()
        self.setupUi(self)
        # 不显示帮助按钮
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        configs = load_settings()
        self.save_path = configs.save_path
        # 显示默认截图保存文件夹路径
        self.show_path.setText(self.save_path)
        self.select_file_btn.clicked.connect(self.show_save_path)

    def show_save_path(self):
        """反显选择的截图缓存文件夹路径，并保存配置项参数"""
        path = FileUtil.choose_save_dir(self, self.save_path)
        if path and path.strip():
            path = path.strip()
            self.show_path.setText(path)
            self.save_path = path
            st = cfg.Settings(path)
            save_settings(json.dumps(st.to_dict()))


def show_settings():
    """显示设置对话框，显示配置项"""
    app = QApplication(sys.argv)
    dialog = SettingsAction()
    dialog.show()
    dialog.exec_()
