# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'plateOptionScreen.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class plateOptionScreen(QtGui.QWidget):
    def __init__(self):
        super(plateOptionScreen, self).__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(800, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(800, 480))
        self.setStyleSheet(_fromUtf8("background-color: rgb(97, 161, 243);"))
        self.layoutWidget = QtGui.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 20, 781, 451))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.back_button = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        self.back_button.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);\n"
"font: 75 20pt \"Roboto\";"))
        self.back_button.setObjectName(_fromUtf8("back_button"))
        self.horizontalLayout_5.addWidget(self.back_button)
        spacerItem = QtGui.QSpacerItem(650, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.title_label = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setStyleSheet(_fromUtf8("font: 75 25pt \"Roboto\";"))
        self.title_label.setTextFormat(QtCore.Qt.AutoText)
        self.title_label.setObjectName(_fromUtf8("title_label"))
        self.horizontalLayout_4.addWidget(self.title_label)
        spacerItem2 = QtGui.QSpacerItem(14, 42, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_2 = QtGui.QFrame(self.layoutWidget)
        self.line_2.setFrameShadow(QtGui.QFrame.Plain)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.plate24_label = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plate24_label.sizePolicy().hasHeightForWidth())
        self.plate24_label.setSizePolicy(sizePolicy)
        self.plate24_label.setMaximumSize(QtCore.QSize(320, 200))
        self.plate24_label.setText(_fromUtf8(""))
        self.plate24_label.setPixmap(QtGui.QPixmap(_fromUtf8("../Python Files/Images/wellPlate24.svg")))
        self.plate24_label.setScaledContents(True)
        self.plate24_label.setObjectName(_fromUtf8("plate24_label"))
        self.horizontalLayout.addWidget(self.plate24_label)
        spacerItem4 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.plate96_label = QtGui.QLabel(self.layoutWidget)
        self.plate96_label.setMaximumSize(QtCore.QSize(320, 200))
        self.plate96_label.setText(_fromUtf8(""))
        self.plate96_label.setPixmap(QtGui.QPixmap(_fromUtf8("../Python Files/Images/wellPlate96.svg")))
        self.plate96_label.setScaledContents(True)
        self.plate96_label.setObjectName(_fromUtf8("plate96_label"))
        self.horizontalLayout.addWidget(self.plate96_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.well24_button = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.well24_button.sizePolicy().hasHeightForWidth())
        self.well24_button.setSizePolicy(sizePolicy)
        self.well24_button.setMaximumSize(QtCore.QSize(150, 250))
        self.well24_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);\n"
"font: 75 20pt \"Roboto\";"))
        self.well24_button.setAutoDefault(True)
        self.well24_button.setDefault(False)
        self.well24_button.setFlat(False)
        self.well24_button.setObjectName(_fromUtf8("well24_button"))
        self.horizontalLayout_2.addWidget(self.well24_button)
        spacerItem5 = QtGui.QSpacerItem(120, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.well96_button = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.well96_button.sizePolicy().hasHeightForWidth())
        self.well96_button.setSizePolicy(sizePolicy)
        self.well96_button.setMaximumSize(QtCore.QSize(150, 250))
        self.well96_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);\n"
"font: 75 20pt \"Roboto\";"))
        self.well96_button.setAutoDefault(True)
        self.well96_button.setFlat(False)
        self.well96_button.setObjectName(_fromUtf8("well96_button"))
        self.horizontalLayout_2.addWidget(self.well96_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.show()

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "OSP", None))
        self.setWindowIcon(QtGui.QIcon("../Python Files/Images/logo_icon.png"))
        self.back_button.setText(_translate("self", "Back", None))
        self.title_label.setText(_translate("self", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">CHOOSE A PLATE SIZE</span></p></body></html>", None))
        self.well24_button.setText(_translate("self", "24 Well", None))
        self.well96_button.setText(_translate("self", "96 Well", None))

