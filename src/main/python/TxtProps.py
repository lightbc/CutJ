import DrawProps
from PyQt5 import QtCore, QtGui, QtWidgets
from util import AppUtil, FileUtil, WindowUtil

# 字体类型名称
font_names = []
# 字体大小可选列表项
font_size = ["8", "10", "12", "14", "16", "18", "20", "22", "24", "26", "28"]


def addTxtProps(cfg, op):
    """添加文本，文本属性配置"""
    if op:
        if hasattr(op, "fontFamily"):
            op.fontFamily = cfg.fontFamily
        if hasattr(op, "fontSize"):
            op.fontSize = int(cfg.fontSize)
        if hasattr(op, "bold"):
            op.bold = cfg.bold
        if hasattr(op, "italic"):
            op.italic = cfg.italic
        if hasattr(op, "underline"):
            op.underline = cfg.underLine
        if hasattr(op, "fontColor"):
            op.fontColor = cfg.txtColor
        if hasattr(op, "textEdit") and op.textEdit:
            # 当更新文本属性项时，文本域文本实时变化样式，如文本样式属性改变，文本内容不重新添加，则不显示实时效果
            op.textEdit.setTxtStyle()
            txt = op.textEdit.toPlainText()
            op.textEdit.setText("")
            op.textEdit.setText(txt)


def update(cfg, op):
    """保存属性配置，更新实时属性效果"""
    addTxtProps(cfg, op)
    FileUtil.updatePropsCfg(cfg)


class TxtProps(object):
    """文本属性配置UI"""

    def __init__(self, op=None):
        self.op = op
        self.props_cfg = FileUtil.loadPropsCfg()
        addTxtProps(self.props_cfg, op)

        self.widget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("height:20px;")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(20, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.bold = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bold.sizePolicy().hasHeightForWidth())
        self.bold.setSizePolicy(sizePolicy)
        self.bold.setStyleSheet("*{margin-left:10px;border:none;}\n"
                                ":hover{background-color:rgba(0,0,0,.1);}")
        self.bold.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/images/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bold.setIcon(icon)
        self.bold.setIconSize(QtCore.QSize(25, 25))
        self.bold.setObjectName("bold")
        self.gridLayout_2.addWidget(self.bold, 1, 2, 1, 1)
        self.underline = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.underline.sizePolicy().hasHeightForWidth())
        self.underline.setSizePolicy(sizePolicy)
        self.underline.setStyleSheet("*{margin-left:10px;border:none;}\n"
                                     ":hover{background-color:rgba(0,0,0,.1);}")
        self.underline.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../resources/images/underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.underline.setIcon(icon1)
        self.underline.setIconSize(QtCore.QSize(25, 25))
        self.underline.setObjectName("underline")
        self.gridLayout_2.addWidget(self.underline, 1, 4, 1, 1)
        self.fontSize = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontSize.sizePolicy().hasHeightForWidth())
        self.fontSize.setSizePolicy(sizePolicy)
        self.fontSize.setStyleSheet("*{width:20px;height:25px;}")
        self.fontSize.setObjectName("fontSize")
        self.gridLayout_2.addWidget(self.fontSize, 1, 1, 1, 1)
        self.italic = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.italic.sizePolicy().hasHeightForWidth())
        self.italic.setSizePolicy(sizePolicy)
        self.italic.setStyleSheet("*{margin-left:10px;border:none;}\n"
                                  ":hover{background-color:rgba(0,0,0,.1);}")
        self.italic.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../resources/images/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.italic.setIcon(icon2)
        self.italic.setIconSize(QtCore.QSize(25, 25))
        self.italic.setObjectName("italic")
        self.gridLayout_2.addWidget(self.italic, 1, 3, 1, 1)
        self.color = QtWidgets.QPushButton(self.widget)
        self.color.setStyleSheet(
            "*{margin-right:20px;border:none;width:70px;height:25px;background-color:rgb(255, 0, 0)};")
        self.color.setText("")
        self.color.setIconSize(QtCore.QSize(25, 25))
        self.color.setObjectName("color")
        self.gridLayout_2.addWidget(self.color, 1, 5, 1, 1)
        self.font = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.font.sizePolicy().hasHeightForWidth())
        self.font.setSizePolicy(sizePolicy)
        self.font.setStyleSheet("*{width:200px;height:25px;}")
        self.font.setObjectName("font")
        self.gridLayout_2.addWidget(self.font, 1, 0, 1, 1)

        v_s_bar_style = "*{width:20px;background-color:gray;}"
        # 设置下拉选择框的垂直滚动条样式
        self.font.view().verticalScrollBar().setStyleSheet(v_s_bar_style)
        self.fontSize.view().verticalScrollBar().setStyleSheet(v_s_bar_style)

        self.initFontFamily()
        self.fontSize.addItems(font_size)

        if self.props_cfg:
            if self.props_cfg.fontFamily:
                self.font.setCurrentText(str(self.props_cfg.fontFamily))
            if self.props_cfg.fontSize:
                self.fontSize.setCurrentText(str(self.props_cfg.fontSize))
            if self.props_cfg.txtColor:
                self.color.setStyleSheet("*{margin-right:20px;border:none;width:70px;height:25px;background-color:rgb("
                                         + self.props_cfg.txtColor + ")};")
            self.is_bold = True if self.props_cfg.bold else False
            self.is_italic = True if self.props_cfg.italic else False
            self.is_underline = True if self.props_cfg.underLine else False

            self.init()

        self.font.currentIndexChanged.connect(lambda: self.getFontFamily())
        self.fontSize.currentIndexChanged.connect(lambda: self.getFontSize())

        self.bold.clicked.connect(lambda: self.setBold())
        self.italic.clicked.connect(lambda: self.setItalic())
        self.underline.clicked.connect(lambda: self.setUnderLine())
        self.color.clicked.connect(lambda: self.showColorSelector())

    def init(self):
        """初始化参数"""
        if self.is_bold:
            self.bold.setIcon(WindowUtil.getIcon(AppUtil.icon_dir + "bold_select.png"))
        if self.is_italic:
            self.italic.setIcon(WindowUtil.getIcon(AppUtil.icon_dir + "italic_select.png"))
        if self.is_underline:
            self.underline.setIcon(WindowUtil.getIcon(AppUtil.icon_dir + "underline_select.png"))

    def initFontFamily(self):
        """初始化字体类型选择列表项"""
        if len(font_names) == 0:
            fonts = FileUtil.loadFontsDict()
            if fonts and len(fonts) > 0:
                for key in fonts:
                    font_names.append(fonts[key])
        self.font.addItems(font_names)

    def getFontFamily(self):
        """获取当前选择字体类型"""
        self.props_cfg.fontFamily = self.font.currentText()
        self.updateCfg()

    def getFontSize(self):
        """获取当前选择字体大小"""
        self.props_cfg.fontSize = self.fontSize.currentText()
        self.updateCfg()

    def setBold(self):
        """设置加粗选择图标样式"""
        if self.is_bold:
            self.bold.setIcon(WindowUtil.getIcon(AppUtil.icon_dir + "bold.png"))
            self.is_bold = False
        else:
            self.bold.setIcon(WindowUtil.getIcon(AppUtil.icon_dir + "bold_select.png"))
            self.is_bold = True
        self.props_cfg.bold = self.is_bold
        self.updateCfg()

    def setItalic(self):
        """设置斜体选择图标样式"""
        if self.is_italic:
            self.italic.setIcon(WindowUtil.getIcon(AppUtil.icon_dir + "italic.png"))
            self.is_italic = False
        else:
            self.italic.setIcon(WindowUtil.getIcon(AppUtil.icon_dir + "italic_select.png"))
            self.is_italic = True
        self.props_cfg.italic = self.is_italic
        self.updateCfg()

    def setUnderLine(self):
        """设置下划线选择图标样式"""
        if self.is_underline:
            self.underline.setIcon(WindowUtil.getIcon(AppUtil.icon_dir + "underline.png"))
            self.is_underline = False
        else:
            self.underline.setIcon(WindowUtil.getIcon(AppUtil.icon_dir + "underline_select.png"))
            self.is_underline = True
        self.props_cfg.underLine = self.is_underline
        self.updateCfg()

    def showColorSelector(self):
        """显示文本颜色选择器"""
        dialog = ColorSelector(self.color, self.op)
        dialog.exec_()

    def updateCfg(self):
        """更新属性配置"""
        update(self.props_cfg, self.op)


class ColorSelector(QtWidgets.QDialog):
    """颜色选择器"""

    def __init__(self, colorSelector=None, op=None):
        super(ColorSelector, self).__init__()
        self.op = op
        self.props_cfg = FileUtil.loadPropsCfg()
        self.colorSelector = colorSelector
        self.resize(650, 100)
        self.widget = QtWidgets.QWidget(self)
        self.dp = DrawProps.DrawProps()
        self.dp.brush_widget.hide()
        self.dp.widget_2.show()
        self.widget.setLayout(self.dp.verticalLayout)
        self.setWindowTitle("颜色")
        # 不显示帮助按钮
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)

        self.dp.ok.clicked.connect(lambda: self.selectColor())
        self.dp.cancel.clicked.connect(lambda: self.close())

    def selectColor(self):
        """更新添加的最新文本颜色属性"""
        self.colorSelector.setStyleSheet(
            "*{margin-right:20px;border:none;width:70px;height:25px;background-color:rgb(" + str(
                self.dp.selectColor) + ")}")
        self.props_cfg.txtColor = str(self.dp.selectColor)
        self.updateCfg()
        self.close()

    def updateCfg(self):
        """更新属性配置"""
        update(self.props_cfg, self.op)
