# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'protocolSelectScreen.ui'
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

class protocolSelectScreen(QtGui.QWidget):
    def __init__(self):
        super(protocolSelectScreen, self).__init__()
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
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 401))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.abs_button = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.abs_button.sizePolicy().hasHeightForWidth())
        self.abs_button.setSizePolicy(sizePolicy)
        self.abs_button.setMinimumSize(QtCore.QSize(250, 75))
        self.abs_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);\n"
"font: 75 20pt \"Roboto\";"))
        self.abs_button.setObjectName(_fromUtf8("abs_button"))
        self.horizontalLayout.addWidget(self.abs_button)
        self.flr_button = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flr_button.sizePolicy().hasHeightForWidth())
        self.flr_button.setSizePolicy(sizePolicy)
        self.flr_button.setMinimumSize(QtCore.QSize(250, 75))
        self.flr_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);\n"
"font: 75 20pt \"Roboto\";"))
        self.flr_button.setObjectName(_fromUtf8("flr_button"))
        self.horizontalLayout.addWidget(self.flr_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.aux_button = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aux_button.sizePolicy().hasHeightForWidth())
        self.aux_button.setSizePolicy(sizePolicy)
        self.aux_button.setMinimumSize(QtCore.QSize(250, 75))
        self.aux_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);\n"
"font: 75 20pt \"Roboto\";"))
        self.aux_button.setObjectName(_fromUtf8("aux_button"))
        self.horizontalLayout_6.addWidget(self.aux_button)
        self.kinetic_button = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kinetic_button.sizePolicy().hasHeightForWidth())
        self.kinetic_button.setSizePolicy(sizePolicy)
        self.kinetic_button.setMinimumSize(QtCore.QSize(250, 75))
        self.kinetic_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);\n"
"font: 75 20pt \"Roboto\";"))
        self.kinetic_button.setObjectName(_fromUtf8("kinetic_button"))
        self.horizontalLayout_6.addWidget(self.kinetic_button)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.line_2 = QtGui.QFrame(self.layoutWidget)
        self.line_2.setFrameShadow(QtGui.QFrame.Plain)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.new_plate_button = QtGui.QPushButton(self.layoutWidget)
        self.new_plate_button.setMinimumSize(QtCore.QSize(200, 50))
        self.new_plate_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);\n"
"font: 75 20pt \"Roboto\";"))
        self.new_plate_button.setObjectName(_fromUtf8("new_plate_button"))
        self.horizontalLayout_4.addWidget(self.new_plate_button)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.load_button = QtGui.QPushButton(self.layoutWidget)
        self.load_button.setMinimumSize(QtCore.QSize(200, 50))
        self.load_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);\n"
"font: 75 20pt \"Roboto\";"))
        self.load_button.setObjectName(_fromUtf8("load_button"))
        self.horizontalLayout_5.addWidget(self.load_button)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.review_button = QtGui.QPushButton(self.layoutWidget)
        self.review_button.setMinimumSize(QtCore.QSize(200, 50))
        self.review_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);\n"
"font: 75 20pt \"Roboto\";"))
        self.review_button.setObjectName(_fromUtf8("review_button"))
        self.horizontalLayout_3.addWidget(self.review_button)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.reset_button = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(sizePolicy)
        self.reset_button.setMaximumSize(QtCore.QSize(150, 35))
        self.reset_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Roboto\";"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../PBPR_V2/Images/gear_logo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_button.setIcon(icon)
        self.reset_button.setIconSize(QtCore.QSize(25, 25))
        self.reset_button.setObjectName(_fromUtf8("reset_button"))
        self.horizontalLayout_2.addWidget(self.reset_button)
        spacerItem6 = QtGui.QSpacerItem(400, 35, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.settings_button = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy)
        self.settings_button.setMaximumSize(QtCore.QSize(150, 35))
        self.settings_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Roboto\";"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../Python Files/Images/gear_logo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_button.setIcon(icon1)
        self.settings_button.setIconSize(QtCore.QSize(25, 25))
        self.settings_button.setObjectName(_fromUtf8("settings_button"))
        self.horizontalLayout_2.addWidget(self.settings_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.show()

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "OSP", None))
        self.setWindowIcon(QtGui.QIcon("../Python Files/Images/logo_icon.png"))
        self.abs_button.setText(_translate("self", "Absorbance", None))
        self.flr_button.setText(_translate("self", "Fluorescence", None))
        self.aux_button.setText(_translate("self", "Auxiliary Control", None))
        self.kinetic_button.setText(_translate("self", "Kinetic Toggle", None))
        self.new_plate_button.setText(_translate("self", "New Plate Configuration", None))
        self.load_button.setText(_translate("self", "Load Protocol Sequence", None))
        self.review_button.setText(_translate("self", "Review", None))
        self.reset_button.setText(_translate("self", "RESET", None))
        self.settings_button.setText(_translate("self", "SETTINGS", None))

