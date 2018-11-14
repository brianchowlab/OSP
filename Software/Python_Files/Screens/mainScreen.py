# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'mainScreen_v2.ui'
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

class mainScreen(QtGui.QWidget):
    def __init__(self):
        super(mainScreen, self).__init__()
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
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 421))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.logoButtons_horLayout = QtGui.QHBoxLayout()
        self.logoButtons_horLayout.setObjectName(_fromUtf8("logoButtons_horLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.logoButtons_horLayout.addItem(spacerItem)
        self.logo_verLayout = QtGui.QVBoxLayout()
        self.logo_verLayout.setSpacing(6)
        self.logo_verLayout.setObjectName(_fromUtf8("logo_verLayout"))
        self.logo_label = QtGui.QLabel(self.layoutWidget)
        self.logo_label.setMaximumSize(QtCore.QSize(400, 180))
        self.logo_label.setText(_fromUtf8(""))
        self.logo_label.setPixmap(QtGui.QPixmap(_fromUtf8("Images/final_logo.png")))
        self.logo_label.setScaledContents(True)
        self.logo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_label.setObjectName(_fromUtf8("logo_label"))
        self.logo_verLayout.addWidget(self.logo_label)
        self.logoButtons_horLayout.addLayout(self.logo_verLayout)
        spacerItem1 = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.logoButtons_horLayout.addItem(spacerItem1)
        self.button_verticalLayout = QtGui.QVBoxLayout()
        self.button_verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.button_verticalLayout.setContentsMargins(-1, -1, 10, -1)
        self.button_verticalLayout.setSpacing(10)
        self.button_verticalLayout.setObjectName(_fromUtf8("button_verticalLayout"))
        spacerItem2 = QtGui.QSpacerItem(20, 108, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.button_verticalLayout.addItem(spacerItem2)
        self.start_button = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        self.start_button.setMinimumSize(QtCore.QSize(300, 75))
        self.start_button.setMaximumSize(QtCore.QSize(300, 75))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);\n"
"font: 75 20pt \"Roboto\";"))
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.button_verticalLayout.addWidget(self.start_button)
        self.calibrate_button = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calibrate_button.sizePolicy().hasHeightForWidth())
        self.calibrate_button.setSizePolicy(sizePolicy)
        self.calibrate_button.setMinimumSize(QtCore.QSize(300, 75))
        self.calibrate_button.setMaximumSize(QtCore.QSize(300, 75))
        self.calibrate_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);\n"
"font: 75 20pt \"Roboto\";"))
        self.calibrate_button.setObjectName(_fromUtf8("calibrate_button"))
        self.button_verticalLayout.addWidget(self.calibrate_button)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.plateOut_button = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plateOut_button.sizePolicy().hasHeightForWidth())
        self.plateOut_button.setSizePolicy(sizePolicy)
        self.plateOut_button.setMinimumSize(QtCore.QSize(300, 75))
        self.plateOut_button.setMaximumSize(QtCore.QSize(150, 75))
        self.plateOut_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);\n"
"font: 75 20pt \"Roboto\";"))
        self.plateOut_button.setObjectName(_fromUtf8("plateOut_button"))
        self.horizontalLayout.addWidget(self.plateOut_button)
        self.button_verticalLayout.addLayout(self.horizontalLayout)
        self.logoButtons_horLayout.addLayout(self.button_verticalLayout)
        self.verticalLayout_6.addLayout(self.logoButtons_horLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.settings_horLayout = QtGui.QHBoxLayout()
        self.settings_horLayout.setObjectName(_fromUtf8("settings_horLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        spacerItem4 = QtGui.QSpacerItem(600, 35, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem4)
        self.settings_horLayout.addLayout(self.verticalLayout_4)
        self.settings_verLayout = QtGui.QVBoxLayout()
        self.settings_verLayout.setObjectName(_fromUtf8("settings_verLayout"))
        self.settings_button = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy)
        self.settings_button.setMaximumSize(QtCore.QSize(200, 35))
        self.settings_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Roboto\";"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Images/gear_logo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_button.setIcon(icon)
        self.settings_button.setIconSize(QtCore.QSize(25, 25))
        self.settings_button.setObjectName(_fromUtf8("settings_button"))
        self.settings_verLayout.addWidget(self.settings_button)
        self.settings_horLayout.addLayout(self.settings_verLayout)
        spacerItem5 = QtGui.QSpacerItem(2, 58, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.settings_horLayout.addItem(spacerItem5)
        self.verticalLayout_6.addLayout(self.settings_horLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.show()

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "OSP", None))
        self.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
        self.start_button.setText(_translate("self", "START", None))
        self.calibrate_button.setText(_translate("self", "CALIBRATE ", None))
        self.plateOut_button.setText(_translate("self", "PLATE OUT", None))
        self.settings_button.setText(_translate("self", "SETTINGS", None))

