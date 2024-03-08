import images
import DrawProps
import TxtProps
from PyQt5 import QtCore, QtGui, QtWidgets
from util import WindowUtil


class Editor:
    """截图区域再编辑"""

    def __init__(self, parent=None):
        # 绘制矩形
        self.dr = None
        # 绘制椭圆
        self.de = None
        # 绘制箭头
        self.da = None
        # 绘制遮罩
        self.dm = None
        # 添加文本
        self.at = None

        self.pt = parent
        self.parentRect = None
        self.widget = QtWidgets.QWidget(parent)
        self.normal_width = 600
        self.normal_height = 100
        self.widget.resize(self.normal_width, int(self.normal_width / 2))
        self.widget.hide()

        self.widget.setStyleSheet("background-color:#ffffff;")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.editor_tools = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editor_tools.sizePolicy().hasHeightForWidth())
        self.editor_tools.setSizePolicy(sizePolicy)
        self.editor_tools.setStyleSheet("height:50px")
        self.editor_tools.setObjectName("editor_tools")
        self.gridLayout = QtWidgets.QGridLayout(self.editor_tools)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.rect = QtWidgets.QPushButton(self.editor_tools)
        self.rect.setMinimumSize(QtCore.QSize(0, 0))
        self.rect.setStyleSheet("*{border:none;width:40px;height:50px;}:hover{background-color:rgba(0, 0, 0, .1);}")
        self.rect.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/resources/images/rect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rect.setIcon(icon)
        self.rect.setIconSize(QtCore.QSize(25, 25))
        self.rect.setObjectName("rect")
        self.gridLayout.addWidget(self.rect, 0, 1, 1, 1)
        self.ellipse = QtWidgets.QPushButton(self.editor_tools)
        self.ellipse.setMinimumSize(QtCore.QSize(0, 0))
        self.ellipse.setStyleSheet("*{border:none;width:40px;height:50px;}:hover{background-color:rgba(0, 0, 0, .1);}")
        self.ellipse.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/resources/images/ellipse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ellipse.setIcon(icon1)
        self.ellipse.setIconSize(QtCore.QSize(25, 25))
        self.ellipse.setObjectName("ellipse")
        self.gridLayout.addWidget(self.ellipse, 0, 2, 1, 1)
        self.arrow = QtWidgets.QPushButton(self.editor_tools)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arrow.sizePolicy().hasHeightForWidth())
        self.arrow.setSizePolicy(sizePolicy)
        self.arrow.setMinimumSize(QtCore.QSize(0, 0))
        self.arrow.setStyleSheet("*{border:none;width:40px;height:50px;}:hover{background-color:rgba(0, 0, 0, .1);}")
        self.arrow.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/resources/images/arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.arrow.setIcon(icon2)
        self.arrow.setIconSize(QtCore.QSize(25, 25))
        self.arrow.setObjectName("arrow")
        self.gridLayout.addWidget(self.arrow, 0, 3, 1, 1)
        self.mosaic = QtWidgets.QPushButton(self.editor_tools)
        self.mosaic.setMinimumSize(QtCore.QSize(0, 0))
        self.mosaic.setStyleSheet("*{border:none;width:40px;height:50px;}:hover{background-color:rgba(0, 0, 0, .1);}")
        self.mosaic.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/resources/images/mosaic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mosaic.setIcon(icon3)
        self.mosaic.setIconSize(QtCore.QSize(25, 25))
        self.mosaic.setObjectName("mosaic")
        self.gridLayout.addWidget(self.mosaic, 0, 4, 1, 1)
        self.txt = QtWidgets.QPushButton(self.editor_tools)
        self.txt.setMinimumSize(QtCore.QSize(0, 0))
        self.txt.setStyleSheet("*{border:none;width:40px;height:50px;}:hover{background-color:rgba(0, 0, 0, .1);}")
        self.txt.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/resources/images/txt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.txt.setIcon(icon4)
        self.txt.setIconSize(QtCore.QSize(25, 25))
        self.txt.setObjectName("txt")
        self.gridLayout.addWidget(self.txt, 0, 5, 1, 1)
        self.verticalLayout.addWidget(self.editor_tools)
        self.props = QtWidgets.QWidget(self.widget)
        self.props.setObjectName("props")
        self.verticalLayout.addWidget(self.props)

        self.props_widget = QtWidgets.QWidget(self.props)
        self.props_widget.resize(self.normal_width, int(self.normal_height / 2))

        self.pre_props_widget = None
        self.layout = QtWidgets.QVBoxLayout(self.props_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.rect.setToolTip("矩形")
        self.ellipse.setToolTip("椭圆")
        self.arrow.setToolTip("箭头")
        self.mosaic.setToolTip("马赛克")
        self.txt.setToolTip("文字")

        self.is_toggle = False
        self.pre_type = -1

        self.rect.clicked.connect(self.drawRect)
        self.ellipse.clicked.connect(self.drawEllipse)
        self.arrow.clicked.connect(self.drawArrow)
        self.mosaic.clicked.connect(self.addMosaic)
        self.txt.clicked.connect(self.addTxt)

    def drawRect(self):
        """绘制矩形"""
        self.pt.createDrawRect()
        draw_props = DrawProps.DrawProps(self.dr)
        self.toggle(draw_props.widget, 1)
        self.pt.setCursor(QtCore.Qt.CrossCursor)
        self.setMask(self.dr)

    def drawEllipse(self):
        """绘制椭圆"""
        self.pt.createDrawEllipse()
        draw_props = DrawProps.DrawProps(self.de)
        self.toggle(draw_props.widget, 2)
        self.pt.setCursor(QtCore.Qt.CrossCursor)
        self.setMask(self.de)

    def drawArrow(self):
        """绘制箭头"""
        self.pt.createDrawArrow()
        draw_props = DrawProps.DrawProps(self.da)
        self.toggle(draw_props.color_widget, 3)
        self.pt.setCursor(QtCore.Qt.CrossCursor)
        self.setMask(self.da)

    def addMosaic(self):
        """绘制遮罩"""
        self.pt.createDrawMosaic()
        draw_props = DrawProps.DrawProps(self.dm)
        self.toggle(draw_props.brush_widget, 4)
        self.pt.setCursor(QtCore.Qt.ArrowCursor)
        self.setMask(self.dm)

    def addTxt(self):
        """添加文本"""
        self.pt.createAddTxt()
        txt_props = TxtProps.TxtProps(self.at, self.pt)
        self.toggle(txt_props.widget, 5)
        self.pt.setCursor(QtCore.Qt.IBeamCursor)
        self.setMask(self.at)

    def setMask(self, o):
        """将选择进行操作的图层界面置于顶层"""
        if self.parentRect and o:
            self.widget.setCursor(QtCore.Qt.ArrowCursor)
            o.resize(self.parentRect[2], self.parentRect[3])
            o.move(self.parentRect[0], self.parentRect[1])
            o.show()
            # 使当前操作的组件在最上层显示
            o.raise_()

    def toggle(self, widget, t):
        # 当选择非添加文本操作时，隐藏文本编辑区域边框
        if self.pre_type == 5 and self.at and self.at.textEdit:
            self.at.textEdit.setStyleSheet("*{border:none;background-color:rgba(255, 255, 255, 0);}")
        if self.pre_props_widget:
            self.layout.replaceWidget(self.pre_props_widget, widget)
        else:
            self.layout.addWidget(widget)
        self.pre_props_widget = widget
        # 当前一次操作与本次操作不一致时
        if not self.pre_type == t:
            self.is_toggle = False
        if not self.is_toggle:
            self.showCommonStyle()
            self.is_toggle = True
        else:
            self.hideCommonStyle()
            self.is_toggle = False
        self.pre_type = t

    def showCommonStyle(self):
        """展示操作选择UI"""
        self.widget.resize(self.normal_width, self.normal_height)
        self.move()

    def hideCommonStyle(self):
        """隐藏操作选择UI"""
        self.widget.resize(self.normal_width, int(self.normal_height / 2))
        self.move()

    def show(self):
        self.move()
        self.widget.show()

    def hide(self):
        self.hideCommonStyle()
        self.widget.hide()

    def move(self):
        """判断截图区域的位置，决定属性操作UI的显示位置"""
        endPoint = self.getEndPoint()
        if endPoint:
            self.widget.move(endPoint[0] - self.widget.width(), endPoint[1])

            # 左边屏幕
            if self.parentRect[0] < self.widget.width():
                if self.parentRect[2] < 0 or self.parentRect[3] < 0:
                    self.widget.move(self.parentRect[0] + self.parentRect[2], endPoint[1])
                else:
                    self.widget.move(self.parentRect[0], endPoint[1])
            # 下边屏幕
            if WindowUtil.screen_height() - endPoint[1] < self.widget.height() * 2:
                self.widget.move(self.widget.pos().x(),
                                 self.widget.pos().y() - self.parentRect[3] - self.widget.height())

    def getEndPoint(self):
        """绘制截屏区域的矩形终点坐标"""
        if self.parentRect:
            if self.parentRect[2] < 0 or self.parentRect[3] < 0:
                return self.parentRect[0], self.parentRect[1]
            else:
                return self.parentRect[0] + self.parentRect[2], self.parentRect[1] + self.parentRect[3]
        return None
