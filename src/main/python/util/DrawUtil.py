import math
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPainter
from util import WindowUtil


def distance_sides(p, rs):
    """
    计算矩形中任意位置一点到四条边的距离
    :param p: 点坐标
    :param rs: 矩形宽高
    :return: 点距离各个边的距离
    """
    px = p[0]
    py = p[1]

    rw = rs[0]
    rh = rs[1]

    left = px
    top = py
    right = rw - px
    bottom = rh - py

    return left, top, right, bottom


def getPen(color, size):
    """
    获取画笔
    :param color:画笔颜色
    :param size:画笔大小
    :return:设置后的画笔对象
    """
    rgb = color.split(",")
    color = QtGui.QColor(int(rgb[0].strip()), int(rgb[1].strip()), int(rgb[2].strip()))
    pen = QtGui.QPen(color, size)
    return pen


class DrawRect(QtWidgets.QLabel):
    """绘制矩形"""

    def __init__(self, brushSize=5, brushColor="255, 0, 0", parent=None):
        super().__init__(parent)
        # 避免需要点击组件后，才能监听鼠标移动
        self.setMouseTracking(True)
        # 绘制截图区域后，截图区域中的标记矩形
        self.inside_rect = None
        # 起点横坐标
        self.start_x = None
        # 起点纵坐标
        self.start_y = None
        # 终点横坐标
        self.end_x = None
        # 终点纵坐标
        self.end_y = None
        # 鼠标左键是否按下
        self.isLeftPress = False
        # 笔刷大小
        self.brushSize = brushSize
        # 笔刷颜色
        self.brushColor = brushColor

        # 历史标记
        self.rectList = []

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        if self.inside_rect:
            self.drawRect(qp)
        qp.end()

    def drawRect(self, qp):
        # 开启反走样效果
        qp.setRenderHint(qp.Antialiasing)
        # 绘制历史矩形
        if self.rectList and len(self.rectList) > 0:
            for rect in self.rectList:
                qp.setPen(getPen(rect["color"], rect["size"]))
                rt = rect["rect"]
                qp.drawRect(rt[0], rt[1], rt[2], rt[3])

        qp.setPen(getPen(self.brushColor, self.brushSize))
        # 上边框
        qp.drawLine(self.inside_rect[0], self.inside_rect[1], self.end_x, self.inside_rect[1])
        # 右边框
        qp.drawLine(self.end_x, self.inside_rect[1], self.end_x, self.end_y)
        # 下边框
        qp.drawLine(self.inside_rect[0], self.end_y, self.end_x, self.end_y)
        # 左边框
        qp.drawLine(self.inside_rect[0], self.inside_rect[1], self.inside_rect[0], self.end_y)

    def mousePressEvent(self, event):
        self.isLeftPress = True
        self.start_x = event.pos().x()
        self.start_y = event.pos().y()

    def mouseReleaseEvent(self, event):
        pos = event.pos()
        self.isLeftPress = False
        self.end_x = pos.x()
        self.end_y = pos.y()
        self.range(pos)
        if self.inside_rect:
            rectDict = {"size": self.brushSize, "color": self.brushColor, "rect": self.inside_rect}
            self.rectList.append(rectDict)

    def mouseMoveEvent(self, event):
        pos = event.pos()
        if self.isLeftPress and self.start_x and self.start_y:
            self.end_x = pos.x()
            self.end_y = pos.y()
            self.range(pos)
            self.inside_rect = (self.start_x, self.start_y, self.end_x - self.start_x, self.end_y - self.start_y)
        self.repaint()

    def range(self, pos):
        """
        矩形绘制限制区域
        :param pos: 鼠标移动坐标
        :return:
        """
        if pos.x() < 0:
            self.end_x = 0
        if pos.y() < 0:
            self.end_y = 0
        if pos.x() > self.width():
            self.end_x = self.width()
        if pos.y() > self.height():
            self.end_y = self.height()


class DrawEllipse(QtWidgets.QLabel):
    """绘制椭圆"""

    def __init__(self, brushSize=5, brushColor="255, 0, 0", parent=None):
        super().__init__(parent)
        # 避免需要点击组件后，才能监听鼠标移动
        self.setMouseTracking(True)
        # 椭圆中心点横坐标
        self.start_x = None
        # 椭圆中心点纵坐标
        self.start_y = None
        # 鼠标移动横坐标
        self.end_x = None
        # 鼠标移动纵坐标
        self.end_y = None
        # 椭圆横坐标上半长轴
        self.radius_x = None
        # 椭圆纵坐标上半长轴
        self.radius_y = None
        # 鼠标左键按下
        self.isLeftPress = False
        # 键盘shift键按下
        self.is_press_shift = False
        # 笔刷大小
        self.brushSize = brushSize
        # 笔刷颜色
        self.brushColor = brushColor

        # 历史椭圆
        self.ellipseList = []

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawEllipse(qp)
        qp.end()

    def drawEllipse(self, qp):
        # 开启反走样效果
        qp.setRenderHint(qp.Antialiasing)
        # 绘制历史椭圆
        if self.ellipseList and len(self.ellipseList) > 0:
            for ellipse in self.ellipseList:
                qp.setPen(getPen(ellipse["color"], ellipse["size"]))
                ep = ellipse["ellipse"]
                qp.drawEllipse(ep[0], ep[1], ep[2], ep[3])

        rgb = self.brushColor.split(",")
        color = QtGui.QColor(int(rgb[0].strip()), int(rgb[1].strip()), int(rgb[2].strip()))
        pen = QtGui.QPen(color, self.brushSize)
        qp.setPen(pen)

        if self.start_x and self.start_y and self.radius_x and self.radius_y:
            qp.drawEllipse(self.start_x, self.start_y, self.radius_x, self.radius_y)

    def mousePressEvent(self, event):
        self.isLeftPress = True
        self.start_x = event.pos().x()
        self.start_y = event.pos().y()

    def mouseReleaseEvent(self, event):
        pos = event.pos()
        self.isLeftPress = False
        self.end_x = pos.x()
        self.end_y = pos.y()
        self.range(pos)
        if self.start_x and self.start_y and self.radius_x and self.radius_y:
            inside_ellipse = self.start_x, self.start_y, self.radius_x, self.radius_y
            ellipseDict = {"size": self.brushSize, "color": self.brushColor, "ellipse": inside_ellipse}
            self.ellipseList.append(ellipseDict)

    def mouseMoveEvent(self, event):
        pos = event.pos()
        if self.isLeftPress:
            self.end_x = pos.x()
            self.end_y = pos.y()
            self.range(pos)
            self.repaint()

    def keyPressEvent(self, event):
        """绘制椭圆时shift键按下"""
        if event.key() == QtCore.Qt.Key_Shift:
            self.is_press_shift = True

    def keyReleaseEvent(self, event):
        """绘制椭圆时shift键释放"""
        if event.key() == QtCore.Qt.Key_Shift:
            self.is_press_shift = False

    def range(self, pos):
        """
        椭圆绘制限制区域
        :param pos: 鼠标移动坐标
        :return:
        """
        if pos.x() < 0:
            self.end_x = 0
        if pos.y() < 0:
            self.end_y = 0
        if pos.x() > self.width():
            self.end_x = self.width()
        if pos.y() > self.height():
            self.end_y = self.height()
        # 当键盘shift键按下，绘制椭圆时，绘制的为圆形
        if self.is_press_shift:
            self.radius_x = self.radius_y = self.end_x - self.start_x
            # 椭圆绘制中心点到各边的距离
            ds = distance_sides((self.start_x, self.start_y), (self.width(), self.height()))
            ms = min(ds[2], ds[3])
            # 反方向绘制圆时，计算圆可以绘制的最小值，即与左边或上边任意一边相切时
            if self.radius_x < 0:
                ms = min(ds[0], ds[1])
            # 正方向绘制圆是，计算可以绘制的最小值，即与右边或下边任意一边相切时
            if abs(self.radius_x) > ms:
                if self.radius_x < 0:
                    ms = -ms
                self.radius_x = self.radius_y = ms
        else:
            self.radius_x, self.radius_y = (self.end_x - self.start_x), (self.end_y - self.start_y)


def getArrow(x1, y1, x2, y2, arrowSize=5):
    """
    获取绘制箭头的箭头部分
    :param x1: 起点横坐标
    :param y1: 起点纵坐标
    :param x2: 终点横坐标
    :param y2: 终点纵坐标
    :param arrowSize: 箭头尺寸
    :return: 箭头部分直线两侧箭头组成线段的绘制终点坐标
    """
    line = QtCore.QLineF()
    # 箭头长度
    line.setLine(x1, y1, x2, y2)
    # 箭头角度
    angle = math.acos(line.dx() / line.length())
    distanceFromEnd = 5
    arrowStart = line.pointAt(1 - distanceFromEnd / line.length())
    if line.dy() >= 0:
        angle = 2 * math.pi - angle
    arrow1 = arrowStart + QtCore.QPointF(math.sin(angle - math.pi / 3) * arrowSize,
                                         math.cos(angle - math.pi / 3) * arrowSize)
    arrow2 = arrowStart + QtCore.QPointF(math.sin(angle - math.pi + math.pi / 3) * arrowSize,
                                         math.cos(angle - math.pi + math.pi / 3) * arrowSize)
    return arrow1, arrow2


class DrawArrow(QtWidgets.QLabel):
    """绘制箭头"""

    def __init__(self, brushColor="255, 0, 0", parent=None):
        super().__init__(parent)
        # 避免需要点击组件后，才能监听鼠标移动
        self.setMouseTracking(True)
        # 直线起点横坐标
        self.start_x = None
        # 直线起点纵坐标
        self.start_y = None
        # 直线终点横坐标
        self.end_x = None
        # 直线终点纵坐标
        self.end_y = None
        # 鼠标左键按下
        self.isLeftPress = False
        # 笔刷颜色
        self.brushColor = brushColor

        # 历史箭头
        self.arrowList = []

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawArrow(qp)
        qp.end()

    def drawArrow(self, qp):
        # 开启反走样效果
        qp.setRenderHint(qp.Antialiasing)
        # 绘制历史箭头
        if self.arrowList and len(self.arrowList) > 0:
            for arrow in self.arrowList:
                qp.setPen(getPen(arrow["color"], 5))
                a = arrow["arrow"]
                arrow = getArrow(a[0], a[1], a[2], a[3])
                qp.drawLine(a[0], a[1], a[2], a[3])
                qp.drawLine(a[2], a[3], arrow[0].x(), arrow[0].y())
                qp.drawLine(a[2], a[3], arrow[1].x(), arrow[1].y())

        if self.start_x and self.start_y:
            qp.setPen(getPen(self.brushColor, 5))
            arrow = getArrow(self.start_x, self.start_y, self.end_x, self.end_y)
            qp.drawLine(self.start_x, self.start_y, self.end_x, self.end_y)
            qp.drawLine(self.end_x, self.end_y, arrow[0].x(), arrow[0].y())
            qp.drawLine(self.end_x, self.end_y, arrow[1].x(), arrow[1].y())

    def mousePressEvent(self, event):
        self.isLeftPress = True
        self.start_x = event.pos().x()
        self.start_y = event.pos().y()

    def mouseReleaseEvent(self, event):
        pos = event.pos()
        self.isLeftPress = False
        self.end_x = pos.x()
        self.end_y = pos.y()
        self.range(pos)
        arrowDict = {"color": self.brushColor, "arrow": (self.start_x, self.start_y, self.end_x, self.end_y)}
        self.arrowList.append(arrowDict)

    def mouseMoveEvent(self, event):
        pos = event.pos()
        if self.isLeftPress:
            self.end_x = pos.x()
            self.end_y = pos.y()
            self.range(pos)
            self.repaint()

    def range(self, pos):
        """
        箭头绘制限制区域
        :param pos: 鼠标移动坐标
        :return:
        """
        if pos.x() < 0:
            self.end_x = 0
        if pos.y() < 0:
            self.end_y = 0
        if pos.x() > self.width():
            self.end_x = self.width()
        if pos.y() > self.height():
            self.end_y = self.height()


class DrawMosaic(QtWidgets.QLabel):
    """绘制马赛克遮罩"""

    def __init__(self, brushSize=5, parent=None):
        super().__init__(parent)
        # 避免需要点击组件后，才能监听鼠标移动
        self.setMouseTracking(True)
        # 笔刷大小
        self.brushSize = brushSize
        # 起点坐标
        self.lastPoint = QtCore.QPoint()
        # 终点坐标
        self.endPoint = QtCore.QPoint()
        # 设置象图初始大小、颜色
        self.pix = QtGui.QPixmap(WindowUtil.screen_width(), WindowUtil.screen_height())
        self.pix.fill(QtGui.QColor(0, 0, 0, .01))

    def paintEvent(self, event):
        pp = QPainter(self.pix)
        # 开启反走样效果
        pp.setRenderHint(pp.Antialiasing)
        pp.setPen(getPen("255, 0, 0", self.brushSize))
        # 根据鼠标指针前后两个位置绘制直线
        pp.drawLine(self.lastPoint, self.endPoint)

        # 让前一个坐标等于后一个坐标值
        # 这样就能实现出连续的线
        self.lastPoint = self.endPoint
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() and QtCore.Qt.LeftButton:
            self.endPoint = event.pos()
            self.repaint()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.endPoint = event.pos()
