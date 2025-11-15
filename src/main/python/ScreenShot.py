import os
import Editor
from PIL import ImageGrab
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QWidget, QLabel, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QPolygon
from util import WindowUtil, AppUtil, DrawUtil, TxtUtil, CommonUtil, FileUtil


class CustomLabel(QLabel):
    """自定义截图组件"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # 属性配置UI对象
        self.edt = None
        # 截图组件的初始大小
        self.win_width, self.win_height = WindowUtil.screen_width(), WindowUtil.screen_height()
        # 避免需要点击组件后，才能监听鼠标移动
        self.setMouseTracking(True)
        self.setCursor(Qt.CrossCursor)
        # 鼠标当前点击的上一次点击时的横坐标
        self.old_start_x = None
        # 谁奥当前点击的上一次点击时的纵坐标
        self.old_start_y = None
        # 起点横坐标
        self.start_x = None
        # 起点纵坐标
        self.start_y = None
        # 终点横坐标
        self.end_x = None
        # 终点纵坐标
        self.end_y = None
        # 矩形
        self.rect = None
        # 拖拽矩形点击点坐标
        self.move_press_pos = None
        # 拖拽矩形边坐标
        self.side_adjust_pos = None
        # 矩形锚点坐标
        self.anchor_point_pos = None
        # 鼠标左键按下
        self.isLeftPressed = False
        # 矩形区域是否移动
        self.is_rect_move = False
        # 矩形边是否移动
        self.is_side_adjust = False
        # 矩形锚点是否移动
        self.is_anchor_pos_adjust = False
        # 拖拽点正方形一半边长
        self.rct = 4
        self.rect_side_color = "red"
        self.anchor_point_color = "blue"

    # 重写绘制函数
    def paintEvent(self, event):
        # 初始化绘图工具
        qp = QPainter()
        # 开始在窗口绘制
        qp.begin(self)
        # 自定义画点方法
        if self.rect:
            self.drawRect(qp)
        # 结束在窗口的绘制
        qp.end()

    def drawRect(self, qp):
        # 处理起点坐标大于终点坐标时，出现背景填充混乱的问题
        start_x, start_y = self.start_x, self.start_y
        end_x, end_y = self.end_x, self.end_y
        if start_x > end_x:
            start_x, end_x = end_x, start_x
        if start_y > end_y:
            start_y, end_y = end_y, start_y
        if start_x > end_x and start_y > end_y:
            start_x, end_x = end_x, start_x
            start_y, end_y = end_y, start_y
        # 遮罩区域画笔设置
        mask_bg = QColor(0, 0, 0)
        mask_pen = QPen(mask_bg, .01)
        mask_brush = QBrush(mask_bg)
        # 绘制矩形相反遮罩区域
        qp.setPen(mask_pen)
        qp.setBrush(mask_brush)
        qp.setOpacity(.5)
        polygon_top = QPolygon([
            # 屏幕-左上
            QPoint(0, 0),
            # 屏幕-右上
            QPoint(WindowUtil.screen_width(), 0),
            # 矩形-右上
            QPoint(end_x, start_y),
            # 矩形-左上
            QPoint(start_x, start_y)
        ])
        polygon_right = QPolygon([
            # 屏幕-右上
            QPoint(WindowUtil.screen_width(), 0),
            # 矩形-右上
            QPoint(end_x, start_y),
            # 矩形-右下
            QPoint(end_x, end_y),
            # 屏幕-右下
            QPoint(WindowUtil.screen_width(), WindowUtil.screen_height())
        ])
        polygon_bottom = QPolygon([
            # 屏幕-右下
            QPoint(WindowUtil.screen_width(), WindowUtil.screen_height()),
            # 矩形-右下
            QPoint(end_x, end_y),
            # 矩形-左下
            QPoint(start_x, end_y),
            # 屏幕-左下
            QPoint(0, WindowUtil.screen_height())
        ])
        polygon_left = QPolygon([
            # 屏幕-左下
            QPoint(0, WindowUtil.screen_height()),
            # 矩形-左下
            QPoint(start_x, end_y),
            # 矩形-左上
            QPoint(start_x, start_y),
            # 屏幕-左上
            QPoint(0, 0)
        ])
        qp.drawPolygon(polygon_top)
        qp.drawPolygon(polygon_right)
        qp.drawPolygon(polygon_bottom)
        qp.drawPolygon(polygon_left)

        common_bg = QColor(30, 135, 210)
        # 绘制矩形边框
        qp.setOpacity(1)
        pen_line = QPen(common_bg, 1)
        qp.setPen(pen_line)
        rectColor = QColor(0, 0, 0, .01)
        rectBrush = QBrush(rectColor)
        qp.setBrush(rectBrush)
        qp.drawRect(self.rect[0], self.rect[1], self.rect[2], self.rect[3])

        # 绘制矩形上拖拽锚点
        pen_ellipse = QPen(common_bg, 1)
        qp.setPen(pen_ellipse)
        brush_ellipse = QBrush(common_bg)
        qp.setBrush(brush_ellipse)
        # 锚点-左上
        qp.drawRect(self.rect[0] - self.rct / 2, self.rect[1] - self.rct / 2, self.rct, self.rct)
        # 锚点-左下
        qp.drawRect(self.rect[0] - self.rct / 2, self.end_y - self.rct / 2, self.rct, self.rct)
        # 锚点-右上
        qp.drawRect(self.end_x - self.rct / 2, self.rect[1] - self.rct / 2, self.rct, self.rct)
        # 锚点-右下
        qp.drawRect(self.end_x - self.rct / 2, self.end_y - self.rct / 2, self.rct, self.rct)

        # 锚点-上中
        qp.drawRect(self.rect[0] + self.rect[2] / 2 - self.rct / 2, self.rect[1] - self.rct / 2, self.rct, self.rct)
        # 锚点-下中
        qp.drawRect(self.end_x - self.rect[2] / 2 - self.rct / 2, self.end_y - self.rct / 2, self.rct, self.rct)
        # 锚点-左中
        qp.drawRect(self.rect[0] - self.rct / 2, self.rect[1] + self.rect[3] / 2 - self.rct / 2, self.rct, self.rct)
        # 锚点-右中
        qp.drawRect(self.end_x - self.rct / 2, self.rect[1] + self.rect[3] / 2 - self.rct / 2, self.rct, self.rct)

    def mousePressEvent(self, event):
        if self.edt and self.edt.pre_type == -1:
            if self.edt:
                self.edt.hide()

            pos = event.pos()
            self.isLeftPressed = True
            # 鼠标在矩形区域按下
            if self.rect and (self.start_x < pos.x() < self.end_x and self.start_y < pos.y() < self.end_y):
                self.is_rect_move = True
                self.move_press_pos = (pos.x(), pos.y())
            # 鼠标在边框上按下
            elif self.rect and (
                    (pos.x() == self.start_x or pos.x() == self.end_x) and self.start_y < pos.y() < self.end_y) \
                    or ((pos.y() == self.start_y or pos.y() == self.end_y) and self.start_x < pos.x() < self.end_x):
                self.is_side_adjust = True
                self.side_adjust_pos = (pos.x(), pos.y())
            # 鼠标在定位点上按下
            elif self.rect and (((pos.x() == self.start_x or pos.x() == self.rect[0] + self.rect[2] / 2 or pos.x() ==
                                  self.end_x) and pos.y() == self.start_y)
                                or ((pos.x() == self.start_x or pos.x() == self.rect[0] + self.rect[2] / 2 or pos.x() ==
                                     self.end_x) and pos.y() == self.end_y)
                                or ((pos.x() == self.start_x or pos.x() == self.end_x) and pos.y() ==
                                    self.rect[1] + self.rect[3] / 2)):
                self.is_anchor_pos_adjust = True
                self.anchor_point_pos = (pos.x(), pos.y())
            else:
                self.old_start_x, self.old_start_y = self.start_x, self.start_y
                self.start_x = pos.x()
                self.start_y = pos.y()

    def mouseReleaseEvent(self, event):
        if self.edt and self.edt.pre_type == -1:
            pos = event.pos()
            self.isLeftPressed = False
            if self.is_rect_move:
                self.is_rect_move = False
            elif self.is_side_adjust:
                self.is_side_adjust = False
            elif self.is_anchor_pos_adjust:
                self.is_anchor_pos_adjust = False
            elif (self.start_x, self.start_y) != (pos.x(), pos.y()):
                # 处理矩形从右下->左上的方式绘制的问题
                if (self.start_x, self.start_y) > (pos.x(), pos.y()):
                    self.start_x, self.end_x = self.end_x, self.start_x
                    self.start_y, self.end_y = self.end_y, self.start_y
                else:
                    self.end_x = pos.x()
                    self.end_y = pos.y()
            else:
                # 如果只是点击，没有拖拽发生，起点坐标回滚
                self.start_x = self.old_start_x
                self.start_y = self.old_start_y

            if self.edt:
                self.edt.parentRect = self.rect
            self.edt.show()

    def mouseMoveEvent(self, event):
        if self.edt and self.edt.pre_type == -1:
            pos = event.pos()
            if self.rect:
                # 改变鼠标样式
                # 十字带箭头
                if self.rect and (self.start_x < pos.x() < self.end_x and self.start_y < pos.y() < self.end_y):
                    self.setCursor(Qt.SizeAllCursor)
                # 水平双向箭头
                elif self.rect and (pos.x() == self.start_x or pos.x() == self.end_x) \
                        and self.start_y < pos.y() < self.end_y:
                    self.setCursor(Qt.SizeHorCursor)
                # 垂直双向箭头
                elif self.rect and (pos.y() == self.start_y or pos.y() == self.end_y) \
                        and self.start_x < pos.x() < self.end_x:
                    self.setCursor(Qt.SizeVerCursor)
                # 左上-右下方向双向箭头
                elif self.rect and ((pos.x() == self.start_x and pos.y() == self.start_y) or (pos.x() == self.end_x and
                                                                                              pos.y() == self.end_y)):
                    self.setCursor(Qt.SizeFDiagCursor)
                # 右上-左下方向双向箭头
                elif self.rect and ((pos.x() == self.end_x and pos.y() == self.start_y) or (pos.x() == self.start_x and
                                                                                            pos.y() == self.end_y)):
                    self.setCursor(Qt.SizeBDiagCursor)
                # 十字
                else:
                    self.setCursor(Qt.CrossCursor)

            # 拖拽
            if self.isLeftPressed:
                # 拖拽矩形区域移动
                if self.is_rect_move:
                    diff_x = pos.x() - self.move_press_pos[0]
                    diff_y = pos.y() - self.move_press_pos[1]
                    if (self.start_x + diff_x) > 0 and (self.start_y + diff_y) > 0 and (
                            self.end_x + diff_x) < self.win_width and (self.end_y + diff_y) < self.win_height:
                        self.start_x, self.start_y = self.start_x + diff_x, self.start_y + diff_y
                        self.end_x, self.end_y = self.end_x + diff_x, self.end_y + diff_y
                    self.move_press_pos = (pos.x(), pos.y())
                # 拖拽边框伸缩
                elif self.is_side_adjust:
                    # 上边框
                    if self.side_adjust_pos[1] == self.start_y and self.start_x < self.side_adjust_pos[0] < self.end_x:
                        self.setCursor(Qt.SizeVerCursor)
                        self.start_y = pos.y()
                        if pos.y() > self.end_y:
                            self.start_y, self.end_y = self.end_y, self.start_y
                    # 右边框
                    elif self.side_adjust_pos[0] == self.end_x and self.start_y < self.side_adjust_pos[1] < self.end_y:
                        self.setCursor(Qt.SizeHorCursor)
                        self.end_x = pos.x()
                        if pos.x() < self.start_x:
                            self.start_x, self.end_x = self.end_x, self.start_x
                    # 下边框
                    elif self.side_adjust_pos[1] == self.end_y and self.start_x < self.side_adjust_pos[0] < self.end_x:
                        self.setCursor(Qt.SizeVerCursor)
                        self.end_y = pos.y()
                        if pos.y() < self.start_y:
                            self.start_y, self.end_y = self.end_y, self.start_y
                    # 左边框
                    elif self.side_adjust_pos[0] == self.start_x and self.start_y < self.side_adjust_pos[1] < \
                            self.end_y:
                        self.setCursor(Qt.SizeHorCursor)
                        self.start_x = pos.x()
                        if pos.x() > self.end_x:
                            self.start_x, self.end_x = self.end_x, self.start_x
                    self.side_adjust_pos = (pos.x(), pos.y())
                elif self.is_anchor_pos_adjust:
                    # 锚点-左上
                    if self.anchor_point_pos[0] == self.start_x and self.anchor_point_pos[1] == self.start_y:
                        self.setCursor(Qt.SizeFDiagCursor)
                        self.start_x = pos.x()
                        self.start_y = pos.y()
                        if pos.x() > self.end_x:
                            self.start_x, self.end_x = self.end_x, self.start_x
                        if pos.y() > self.end_y:
                            self.start_y, self.end_y = self.end_y, self.start_y
                        if pos.x() > self.end_x and pos.y() > self.end_y:
                            self.start_x, self.end_x = self.end_x, self.start_x
                            self.start_y, self.end_y = self.end_y, self.start_y
                    # 锚点-右上
                    elif self.anchor_point_pos[0] == self.end_x and self.anchor_point_pos[1] == self.start_y:
                        self.setCursor(Qt.SizeBDiagCursor)
                        self.end_x = pos.x()
                        self.start_y = pos.y()
                        if pos.x() < self.start_x:
                            self.start_x, self.end_x = self.end_x, self.start_x
                        if pos.y() > self.start_y:
                            self.start_y, self.end_y = self.end_y, self.start_y
                        if pos.x() < self.start_x and pos.y() > self.start_y:
                            self.start_x, self.end_x = self.end_x, self.start_x
                            self.start_y, self.end_y = self.end_y, self.start_y
                    # 锚点-右下
                    elif self.anchor_point_pos[0] == self.end_x and self.anchor_point_pos[1] == self.end_y:
                        self.setCursor(Qt.SizeFDiagCursor)
                        self.end_x = pos.x()
                        self.end_y = pos.y()
                        if pos.x() < self.start_x:
                            self.start_x, self.end_x = self.end_x, self.start_x
                        if pos.y() < self.start_y:
                            self.start_y, self.end_y = self.end_y, self.start_y
                        if pos.x() < self.start_x and pos.y() < self.start_y:
                            self.start_x, self.end_x = self.end_x, self.start_x
                            self.start_y, self.end_y = self.end_y, self.start_y
                    # 锚点-左下
                    elif self.anchor_point_pos[0] == self.start_x and self.anchor_point_pos[1] == self.end_y:
                        self.setCursor(Qt.SizeBDiagCursor)
                        self.start_x = pos.x()
                        self.end_y = pos.y()
                        if pos.x() > self.end_x:
                            self.start_x, self.end_x = self.end_x, self.start_x
                        if pos.y() < self.end_y:
                            self.start_y, self.end_y = self.end_y, self.start_y
                        if pos.x() > self.end_x and pos.y() < self.start_y:
                            self.start_x, self.end_x = self.end_x, self.start_x
                            self.start_y, self.end_y = self.end_y, self.start_y
                    self.anchor_point_pos = (pos.x(), pos.y())
                    if self.start_x > self.end_x:
                        self.start_x, self.end_x = self.end_x, self.start_x
                    if self.start_y > self.end_y:
                        self.start_y, self.end_y = self.end_y, self.start_y
                    if self.start_x > self.end_x and self.start_y > self.end_y:
                        self.start_x, self.end_x = self.end_x, self.start_x
                        self.start_y, self.end_y = self.end_y, self.start_y
                else:
                    self.setCursor(Qt.CrossCursor)
                    self.end_x = pos.x()
                    self.end_y = pos.y()
                self.rect = (self.start_x, self.start_y, self.end_x - self.start_x, self.end_y - self.start_y)
                self.repaint()


class Window(QMainWindow):
    """截屏主界面窗体"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle(AppUtil.app_name)
        WindowUtil.setIcon(self, AppUtil.app_icon)
        # 设置截屏界面全屏且不显示窗体边框
        self.setMinimumSize(WindowUtil.screen_width(), WindowUtil.screen_height())
        # 窗体去除边框、标题栏、工具栏等，以及窗体始终置顶
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # 窗体透明
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.is_ctrl = False
        self.cutRect = CustomLabel(self)
        self.cutRect.setMinimumSize(WindowUtil.screen_width(), WindowUtil.screen_height())
        self.cutRect.setStyleSheet("background-color:rgba(0, 0, 0, .01);")

        self.edt = Editor.Editor(self)
        self.drawRect = None
        self.drawEllipse = None
        self.drawArrow = None
        self.drawMosaic = None
        self.addTxt = None
        self.create()
        self.cutRect.edt = self.edt

    def create(self):
        self.createDrawRect()
        self.createDrawEllipse()
        self.createDrawArrow()
        self.createDrawMosaic()
        self.createAddTxt()

    def createDrawRect(self):
        """创建绘制矩形图层"""
        self.drawRect = DrawUtil.DrawRect(parent=self)
        self.edt.dr = self.drawRect

    def createDrawEllipse(self):
        """创建绘制椭圆图层"""
        self.drawEllipse = DrawUtil.DrawEllipse(parent=self)
        self.edt.de = self.drawEllipse

    def createDrawArrow(self):
        """创建绘制箭头图层"""
        self.drawArrow = DrawUtil.DrawArrow(parent=self)
        self.edt.da = self.drawArrow

    def createDrawMosaic(self):
        """创建绘制遮罩图层"""
        self.drawMosaic = DrawUtil.DrawMosaic(parent=self)
        self.edt.dm = self.drawMosaic

    def createAddTxt(self):
        """ 创建添加文本图层"""
        self.addTxt = TxtUtil.TextArea(parent=self)
        self.edt.at = self.addTxt

    def keyPressEvent(self, event):
        # 键盘CTRL键按下
        if event.key() == Qt.Key_Control:
            self.is_ctrl = True
        # 键盘CTRL+S组合键按下
        if self.is_ctrl and event.key() == Qt.Key_S:
            self.doCut()
        # 键盘ESC键按下，退出截图
        if event.key() == Qt.Key_Escape:
            self.close()

        if event.key() == Qt.Key_Shift:
            self.drawEllipse.is_press_shift = True

    def keyReleaseEvent(self, event):
        # 键盘CTRL键释放
        if event.key() == Qt.Key_Control:
            self.is_ctrl = False
        if event.key() == Qt.Key_Shift:
            self.drawEllipse.is_press_shift = False

    def doCut(self):
        if self.cutRect.rect:
            # 裁剪截图边框及定位锚点，向内收缩2个单位
            cut_side = 2
            rect = self.cutRect.rect
            bbox = (rect[0] + cut_side, rect[1] + cut_side, rect[0] + rect[2] - cut_side,
                    rect[1] + rect[3] - cut_side)
            im = ImageGrab.grab(bbox)
            save_path = FileUtil.get_save_path() + os.sep + CommonUtil.getTempImageFileName()
            im.save(save_path)
            self.close()
