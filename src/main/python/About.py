# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(282, 172)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.version = QtWidgets.QLabel(Dialog)
        self.version.setText("")
        self.version.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.version.setObjectName("version")
        self.gridLayout.addWidget(self.version, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setOpenExternalLinks(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "关于"))
        self.label_4.setText(_translate("Dialog", "博客："))
        self.label_3.setText(_translate("Dialog", "关于CutJ："))
        self.label_2.setText(_translate("Dialog", "作者："))
        self.label.setText(_translate("Dialog", "版本："))
        self.label_6.setText(_translate("Dialog", "lightbc"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p>CutJ是一款离线使用的截图应用程序</p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://www.cnblogs.com/lightbc\"><span style=\" text-decoration: underline; color:#0000ff;\">博客园</span></a></p></body></html>"))
