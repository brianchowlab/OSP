# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'absScreen.ui'
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

class absScreen(QtGui.QWidget):
    def __init__(self):
        super(absScreen, self).__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(800, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(800, 480))
        self.setStyleSheet(_fromUtf8("background-color: rgb(97, 161, 243);"))
        self.layoutWidget = QtGui.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 12, 781, 391))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.back_button = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        self.back_button.setMinimumSize(QtCore.QSize(100, 35))
        self.back_button.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);\n"
"\n"
""))
        self.back_button.setObjectName(_fromUtf8("back_button"))
        self.horizontalLayout_2.addWidget(self.back_button)
        spacerItem = QtGui.QSpacerItem(675, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.line_4 = QtGui.QFrame(self.layoutWidget)
        self.line_4.setFrameShadow(QtGui.QFrame.Plain)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.title_label = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setMaximumSize(QtCore.QSize(555, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(_fromUtf8(""))
        self.title_label.setTextFormat(QtCore.Qt.AutoText)
        self.title_label.setObjectName(_fromUtf8("title_label"))
        self.horizontalLayout.addWidget(self.title_label)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_5 = QtGui.QFrame(self.layoutWidget)
        self.line_5.setFrameShadow(QtGui.QFrame.Plain)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout.addWidget(self.line_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.expTime_label = QtGui.QLabel(self.layoutWidget)
        self.expTime_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.expTime_label.setFont(font)
        self.expTime_label.setObjectName(_fromUtf8("expTime_label"))
        self.horizontalLayout_3.addWidget(self.expTime_label)
        self.expTime_singWave_spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.expTime_singWave_spinBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expTime_singWave_spinBox.sizePolicy().hasHeightForWidth())
        self.expTime_singWave_spinBox.setSizePolicy(sizePolicy)
        self.expTime_singWave_spinBox.setMinimumSize(QtCore.QSize(0, 45))
        self.expTime_singWave_spinBox.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.expTime_singWave_spinBox.setFont(font)
        self.expTime_singWave_spinBox.setStyleSheet(_fromUtf8("background-color: rgb(255,255,255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 1px;"))
        self.expTime_singWave_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.expTime_singWave_spinBox.setPrefix(_fromUtf8(""))
        self.expTime_singWave_spinBox.setMinimum(1)
        self.expTime_singWave_spinBox.setMaximum(1000000)
        self.expTime_singWave_spinBox.setProperty("value", 1)
        self.expTime_singWave_spinBox.setObjectName(_fromUtf8("expTime_singWave_spinBox"))
        self.horizontalLayout_3.addWidget(self.expTime_singWave_spinBox)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtGui.QSpacerItem(20, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem5)
        self.line_8 = QtGui.QFrame(self.layoutWidget)
        self.line_8.setFrameShadow(QtGui.QFrame.Plain)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.verticalLayout_2.addWidget(self.line_8)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.set_button = QtGui.QPushButton(self.layoutWidget)
        self.set_button.setMaximumSize(QtCore.QSize(150, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.set_button.setFont(font)
        self.set_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);\n"
"\n"
""))
        self.set_button.setObjectName(_fromUtf8("set_button"))
        self.horizontalLayout_4.addWidget(self.set_button)
        spacerItem7 = QtGui.QSpacerItem(40, 75, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.show()

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "OSP", None))
        self.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
        self.back_button.setText(_translate("self", "Back", None))
        self.title_label.setText(_translate("self", "<html><head/><body><p align=\"center\">ABSORBANCE</p></body></html>", None))
        self.expTime_label.setText(_translate("self", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Exposure Time : </span></p></body></html>", None))
        self.expTime_singWave_spinBox.setSuffix(_translate("self", " ms", None))
        self.set_button.setText(_translate("self", "SET", None))

