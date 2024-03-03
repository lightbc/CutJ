import math
from PyQt5 import QtGui, QtWidgets


class TextArea(QtWidgets.QLabel):
    """添加文本"""

    def __init__(self, fontFamily="黑体", fontSize=12, bold=False, italic=False, underline=False, fontColor="255, 0, 0",
                 parent=None):
        super().__init__(parent)
        self.hide()
        # 文本域
        self.textEdit = None
        # 鼠标点击坐标
        self.startPoint = None
        # 字体类型
        self.fontFamily = fontFamily
        # 字体大小
        self.fontSize = fontSize
        # 加粗
        self.bold = bold
        # 斜体
        self.italic = italic
        # 下划线
        self.underline = underline
        # 字体颜色
        self.fontColor = fontColor

    def mousePressEvent(self, event):
        """在鼠标点击位置创建文本域"""
        pos = event.pos()
        self.startPoint = pos
        # 移除历史文本域的边框及背景色，以及设置不可再次编辑
        if self.textEdit:
            self.textEdit.setEnabled(False)
            self.textEdit.setStyleSheet("*{border:none;background-color:rgba(255, 255, 255, 0);}")
        self.textEdit = TextEdit(self)
        # 获取文本域最大尺寸
        self.textEdit.maxSize = self.getMaxSize()
        self.textEdit.startPoint = pos
        self.textEdit.move(pos)
        self.textEdit.setPlainText("")
        # 文本域获取焦点
        self.textEdit.setFocus(True)
        self.textEdit.show()

    def getMaxSize(self):
        """
        获取文本域最大尺寸
        :return:
        """
        if self.startPoint:
            return self.width() - self.startPoint.x(), self.height() - self.startPoint.y()
        return None


class TextEdit(QtWidgets.QTextEdit):
    """文本域"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pt = parent
        self.hide()
        self.setTxtStyle()
        # 最大尺寸
        self.maxSize = None
        self.document = self.document()
        self.textChanged.connect(self.change)
        # 不自动换行
        self.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setStyleSheet(
            "*{width:auto;height:auto;border: 2px dashed rgba(255, 255, 255, .5);"
            "background-color:rgba(255, 255, 255, 0);resize:none;}")
        self.setObjectName("textEdit")

        # 不显示垂直滚动条
        self.verticalScrollBar().setStyleSheet("width:0;")
        # 不显示水平滚动条
        self.horizontalScrollBar().setStyleSheet("width:0;")
        self.initParams()

    def initParams(self):
        """初始化文本域参数"""
        # 单行最大输入字数
        self.max_line_words = 0
        # 最大行数
        self.max_lines = 0
        # 当前行数
        self.current_lines = 1
        # 当前行数上次换行记录行数
        self.current_lines_record = 0
        # 文本域本次行字数变化前一次记录
        self.pre_words = None
        # 文本域本次行数变化前一次记录
        self.pre_lines = None

    def setTxtStyle(self):
        """设置文本显示样式"""
        if self.pt:
            self.setFontFamily(self.pt.fontFamily)
            self.setFontPointSize(self.pt.fontSize)
            if self.pt.bold:
                self.setFontWeight(QtGui.QFont.Bold)
            else:
                self.setFontWeight(QtGui.QFont.Normal)
            self.setFontItalic(self.pt.italic)
            self.setFontUnderline(self.pt.underline)
            rgb = self.pt.fontColor.split(",")
            color = QtGui.QColor(int(rgb[0].strip()), int(rgb[1].strip()), int(rgb[2].strip()))
            self.setTextColor(color)

    def change(self):
        """文本域文本输入效果"""
        wi = 5
        hi = 15
        txt = self.toPlainText()
        if len(txt) == 0:
            self.initParams()
        if txt and self.max_line_words:
            self.current_lines = math.ceil(len(txt) / self.max_line_words)
            # 当当前行数大于前一次记录时，换行
            if self.current_lines > self.current_lines_record:
                self.current_lines_record = self.current_lines
                # 换行符添加位置下标
                index = (self.current_lines - 1) * self.max_line_words
                txt = txt[:index] + "\n" + txt[index:]
                self.setText(txt)
                # 设置光标位置
                self.moveCursor(QtGui.QTextCursor.End)

        self.document.adjustSize()
        newWidth = self.document.size().width() + wi
        newHeight = self.document.size().height() + hi
        # 增加宽度
        if self.maxSize and newWidth >= self.maxSize[0]:
            # 达到限制宽度后，不再增加宽度
            if not self.max_line_words:
                self.setFixedWidth(self.maxSize[0])
                self.max_line_words = len(txt) - 1
        else:
            self.setFixedWidth(newWidth)

        # 当输入内容在最大字数下，且逐步减少时，削减宽度
        if self.pre_words and 1 < len(txt) < self.pre_words:
            newWidth = self.document.size().width() - wi
            self.setFixedWidth(newWidth)

        # 增加高度
        if self.maxSize and newHeight >= self.maxSize[1]:
            # 达到限制高度后，不再增加高度
            if not self.max_lines:
                self.setFixedHeight(self.maxSize[1])
                self.max_lines = math.ceil(len(txt) / self.max_line_words)
        else:
            self.setFixedHeight(newHeight)

        # 当文本行数在最大行数下，且逐步减少时，削减高度
        if self.pre_lines and 1 < self.current_lines < self.pre_lines:
            newHeight = self.document.size().width() - hi
            self.setFixedHeight(newHeight)

        # 设置最新的行数和列数
        self.pre_words = len(txt)
        self.pre_lines = self.current_lines
