from PyQt5 import QtCore, QtGui, QtWidgets
from util import AppUtil, WindowUtil, FileUtil, images

# 画笔大小，small-5,middle-10,big-15
brush = ("small", "middle", "big")


def validRGB(inp, v):
    """校验RGB输入框中参数"""
    if not v:
        return
    try:
        if 0 <= int(v) <= 255:
            inp.setText(v)
        elif int(v) > 255:
            inp.setText("255")
        else:
            inp.setText("0")
    except ValueError as e:
        inp.setText("0")


class DrawProps(object):
    """绘制矩形、椭圆、箭头、遮罩时，属性配置"""

    def __init__(self, op=None):
        self.op = op
        # 加载属性配置文件，初始化配置属性
        self.props_cfg = FileUtil.loadPropsCfg()

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.brush_widget = QtWidgets.QWidget(self.widget)
        self.brush_widget.setObjectName("brush_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.brush_widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.small = QtWidgets.QPushButton(self.brush_widget)
        self.small.setStyleSheet("*{border:none;margin:10px;}")
        self.small.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/resources/images/small_normal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.small.setIcon(icon)
        self.small.setIconSize(QtCore.QSize(25, 25))
        self.small.setObjectName("small")
        self.gridLayout_2.addWidget(self.small, 0, 0, 1, 1)
        self.middle = QtWidgets.QPushButton(self.brush_widget)
        self.middle.setStyleSheet("*{border:none;margin:10px;}")
        self.middle.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/resources/images/middle_normal.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.middle.setIcon(icon1)
        self.middle.setIconSize(QtCore.QSize(25, 25))
        self.middle.setObjectName("middle")
        self.gridLayout_2.addWidget(self.middle, 0, 1, 1, 1)
        self.big = QtWidgets.QPushButton(self.brush_widget)
        self.big.setStyleSheet("*{border:none;margin:10px;}")
        self.big.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/resources/images/big_normal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.big.setIcon(icon2)
        self.big.setIconSize(QtCore.QSize(25, 25))
        self.big.setObjectName("big")
        self.gridLayout_2.addWidget(self.big, 0, 2, 1, 1)
        self.horizontalLayout.addWidget(self.brush_widget)
        self.color_widget = QtWidgets.QWidget(self.widget)
        self.color_widget.setObjectName("color_widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.color_widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.color_widget)
        self.label.setStyleSheet("*{margin:0 10px;width:10px;height:25px;}")
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 13, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 10, 1, 1)
        self.blue = QtWidgets.QLineEdit(self.color_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blue.sizePolicy().hasHeightForWidth())
        self.blue.setSizePolicy(sizePolicy)
        self.blue.setMinimumSize(QtCore.QSize(0, 0))
        self.blue.setMaximumSize(QtCore.QSize(187, 16777215))
        self.blue.setStyleSheet("*{width:10px;height:25px;}")
        self.blue.setAlignment(QtCore.Qt.AlignCenter)
        self.blue.setObjectName("blue")
        self.gridLayout_3.addWidget(self.blue, 0, 11, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.color_widget)
        self.label_3.setStyleSheet("*{margin:0 10px;width:10px;height:25px;}")
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 9, 1, 1)
        self.color = QtWidgets.QPushButton(self.color_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color.sizePolicy().hasHeightForWidth())
        self.color.setSizePolicy(sizePolicy)
        self.color.setStyleSheet("*{margin:0 20px;border:none;width:70px;height:25px;background-color:red;}")
        self.color.setText("")
        self.color.setIconSize(QtCore.QSize(25, 25))
        self.color.setObjectName("color")
        self.gridLayout_3.addWidget(self.color, 0, 12, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.color_widget)
        self.label_2.setStyleSheet("*{margin:0 10px;width:10px;height:25px;}")
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 8, 1, 1)
        self.green = QtWidgets.QLineEdit(self.color_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.green.sizePolicy().hasHeightForWidth())
        self.green.setSizePolicy(sizePolicy)
        self.green.setMinimumSize(QtCore.QSize(0, 0))
        self.green.setMaximumSize(QtCore.QSize(187, 16777215))
        self.green.setStyleSheet("*{width:10px;height:25px;}")
        self.green.setAlignment(QtCore.Qt.AlignCenter)
        self.green.setObjectName("green")
        self.gridLayout_3.addWidget(self.green, 0, 7, 1, 1)
        self.red = QtWidgets.QLineEdit(self.color_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.red.sizePolicy().hasHeightForWidth())
        self.red.setSizePolicy(sizePolicy)
        self.red.setMinimumSize(QtCore.QSize(0, 0))
        self.red.setMaximumSize(QtCore.QSize(187, 16777215))
        self.red.setStyleSheet("*{width:10px;height:25px;}")
        self.red.setAlignment(QtCore.Qt.AlignCenter)
        self.red.setObjectName("red")
        self.gridLayout_3.addWidget(self.red, 0, 3, 1, 1)
        self.horizontalLayout.addWidget(self.color_widget)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget()
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.ok = QtWidgets.QPushButton(self.widget_2)
        self.ok.setObjectName("ok")
        self.horizontalLayout_2.addWidget(self.ok)
        self.cancel = QtWidgets.QPushButton(self.widget_2)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.widget_2.hide()
        self.ok.setText("Ok")
        self.cancel.setText("Cancel")
        self.label.setStyleSheet("*{width:10px;height:25px;}")
        self.label.setText("红(R):")
        self.red.setText("255")
        self.label_2.setStyleSheet("*{width:10px;height:25px;}")
        self.label_2.setText("绿(G):")
        self.green.setText("0")
        self.label_3.setStyleSheet("*{width:10px;height:25px;}")
        self.label_3.setText("蓝(B):")
        self.blue.setText("0")

        self.brushSize = 5
        if self.props_cfg:
            self.brush = self.props_cfg.brush if self.props_cfg.brush else brush[0]
            self.selectColor = self.props_cfg.defaultColor if self.props_cfg.defaultColor else "255, 0, 0"
            if self.selectColor and self.selectColor.index(",") != -1:
                rgb = self.selectColor.split(",")
                self.red.setText(rgb[0].strip())
                self.green.setText(rgb[1].strip())
                self.blue.setText(rgb[2].strip())

        self.changeBrush(self.brush)
        self.small.clicked.connect(lambda: self.changeBrush(self.small.objectName()))
        self.middle.clicked.connect(lambda: self.changeBrush(self.middle.objectName()))
        self.big.clicked.connect(lambda: self.changeBrush(self.big.objectName()))

        self.changeRGB()
        self.red.textChanged.connect(self.changeRGB)
        self.green.textChanged.connect(self.changeRGB)
        self.blue.textChanged.connect(self.changeRGB)

    def changeBrush(self, name=None):
        """选择笔刷大小，更改选择笔刷图标样式"""
        if name is None:
            self.small.setIcon(WindowUtil.getIcon(AppUtil.icon_dir + "small_select.png"))
        else:
            br = self.getBrush(name)
            br.setIcon(WindowUtil.getIcon(AppUtil.icon_dir + name + "_select.png"))
            for b in brush:
                if not (b == name):
                    self.getBrush(b).setIcon(WindowUtil.getIcon(AppUtil.icon_dir + b + "_normal.png"))
                else:
                    self.props_cfg.brush = b
                    self.updateCfg()

    def getBrush(self, name):
        """获取笔刷大小"""
        if name == brush[1]:
            self.brushSize = 10
            return self.middle
        if name == brush[2]:
            self.brushSize = 20
            return self.big
        self.brushSize = 5
        return self.small

    def changeRGB(self):
        """改变绘制时笔刷颜色"""
        rgb = self.getRGB()

        validRGB(self.red, rgb[0])
        validRGB(self.green, rgb[1])
        validRGB(self.blue, rgb[2])

        rgb = "{0},{1},{2}".format(rgb[0], rgb[1], rgb[2])
        style = "*{margin:0 20px;border:none;width:70px;height:25px;background-color:rgb(" + rgb + ");}"
        self.color.setStyleSheet(style)
        self.props_cfg.defaultColor = str(rgb)
        self.updateCfg()

    def getRGB(self):
        """获取RGB输入框中的RGB数值"""
        r = self.red.text().strip()
        g = self.green.text().strip()
        b = self.blue.text().strip()
        return r, g, b

    def updateCfg(self):
        """更新配置文件，更新绘制工具的实时参数"""
        if self.op:
            if hasattr(self.op, "brushSize"):
                self.getBrush(self.props_cfg.brush)
                self.op.brushSize = self.brushSize
            if hasattr(self.op, "brushColor"):
                self.op.brushColor = self.props_cfg.defaultColor
        FileUtil.updatePropsCfg(self.props_cfg)
