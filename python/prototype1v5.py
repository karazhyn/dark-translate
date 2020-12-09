# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/nikita/dev/DarkTranslate/scripts/prototype1v5.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DarkTranslate(object):
    def setupUi(self, DarkTranslate):
        DarkTranslate.setObjectName("DarkTranslate")
        DarkTranslate.setWindowModality(QtCore.Qt.NonModal)
        DarkTranslate.resize(400, 332)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DarkTranslate.sizePolicy().hasHeightForWidth())
        DarkTranslate.setSizePolicy(sizePolicy)
        DarkTranslate.setMinimumSize(QtCore.QSize(0, 0))
        DarkTranslate.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/darkTheme/logoDark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DarkTranslate.setWindowIcon(icon)
        DarkTranslate.setWindowOpacity(1.0)
        DarkTranslate.setSizeGripEnabled(True)
        DarkTranslate.setModal(False)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DarkTranslate)
        self.verticalLayout_2.setContentsMargins(9, 6, 9, 9)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.previousButton = QtWidgets.QPushButton(DarkTranslate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousButton.sizePolicy().hasHeightForWidth())
        self.previousButton.setSizePolicy(sizePolicy)
        self.previousButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/darkTheme/left-arrow-angle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previousButton.setIcon(icon1)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout_4.addWidget(self.previousButton)
        self.nextButton = QtWidgets.QPushButton(DarkTranslate)
        self.nextButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/darkTheme/right-arrow-angle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon2)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_4.addWidget(self.nextButton)
        self.status = QtWidgets.QLabel(DarkTranslate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        self.status.setMinimumSize(QtCore.QSize(50, 0))
        self.status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.status.setText("")
        self.status.setScaledContents(False)
        self.status.setWordWrap(False)
        self.status.setObjectName("status")
        self.horizontalLayout_4.addWidget(self.status)
        self.toolButton = QtWidgets.QToolButton(DarkTranslate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_4.addWidget(self.toolButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.inputText = QtWidgets.QPlainTextEdit(DarkTranslate)
        self.inputText.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputText.sizePolicy().hasHeightForWidth())
        self.inputText.setSizePolicy(sizePolicy)
        self.inputText.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.inputText.setFont(font)
        self.inputText.setAutoFillBackground(False)
        self.inputText.setStyleSheet("")
        self.inputText.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.inputText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.inputText.setPlainText("")
        self.inputText.setOverwriteMode(False)
        self.inputText.setObjectName("inputText")
        self.verticalLayout.addWidget(self.inputText)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.copyButton = QtWidgets.QPushButton(DarkTranslate)
        self.copyButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copyButton.sizePolicy().hasHeightForWidth())
        self.copyButton.setSizePolicy(sizePolicy)
        self.copyButton.setMinimumSize(QtCore.QSize(25, 25))
        self.copyButton.setMaximumSize(QtCore.QSize(25, 16777215))
        self.copyButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.copyButton.setFont(font)
        self.copyButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.copyButton.setCheckable(False)
        self.copyButton.setObjectName("copyButton")
        self.horizontalLayout_3.addWidget(self.copyButton)
        self.fromTranslateBox = QtWidgets.QComboBox(DarkTranslate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fromTranslateBox.sizePolicy().hasHeightForWidth())
        self.fromTranslateBox.setSizePolicy(sizePolicy)
        self.fromTranslateBox.setMinimumSize(QtCore.QSize(50, 0))
        self.fromTranslateBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.fromTranslateBox.setEditable(False)
        self.fromTranslateBox.setMaxVisibleItems(15)
        self.fromTranslateBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.fromTranslateBox.setMinimumContentsLength(12)
        self.fromTranslateBox.setFrame(True)
        self.fromTranslateBox.setObjectName("fromTranslateBox")
        self.fromTranslateBox.addItem("")
        self.horizontalLayout_3.addWidget(self.fromTranslateBox)
        self.swapButton = QtWidgets.QPushButton(DarkTranslate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.swapButton.sizePolicy().hasHeightForWidth())
        self.swapButton.setSizePolicy(sizePolicy)
        self.swapButton.setMinimumSize(QtCore.QSize(30, 25))
        self.swapButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.swapButton.setFont(font)
        self.swapButton.setTabletTracking(False)
        self.swapButton.setText("")
        self.swapButton.setObjectName("swapButton")
        self.horizontalLayout_3.addWidget(self.swapButton)
        self.toTranslateBox = QtWidgets.QComboBox(DarkTranslate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toTranslateBox.sizePolicy().hasHeightForWidth())
        self.toTranslateBox.setSizePolicy(sizePolicy)
        self.toTranslateBox.setMinimumSize(QtCore.QSize(50, 0))
        self.toTranslateBox.setEditable(False)
        self.toTranslateBox.setMaxVisibleItems(15)
        self.toTranslateBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.toTranslateBox.setMinimumContentsLength(12)
        self.toTranslateBox.setObjectName("toTranslateBox")
        self.toTranslateBox.addItem("")
        self.horizontalLayout_3.addWidget(self.toTranslateBox)
        self.translateButton = QtWidgets.QPushButton(DarkTranslate)
        self.translateButton.setMinimumSize(QtCore.QSize(0, 25))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icons/darkTheme/click2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.translateButton.setIcon(icon3)
        self.translateButton.setObjectName("translateButton")
        self.horizontalLayout_3.addWidget(self.translateButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.outputText = QtWidgets.QTextEdit(DarkTranslate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputText.sizePolicy().hasHeightForWidth())
        self.outputText.setSizePolicy(sizePolicy)
        self.outputText.setMinimumSize(QtCore.QSize(0, 0))
        self.outputText.setObjectName("outputText")
        self.verticalLayout.addWidget(self.outputText)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.googleButton = QtWidgets.QPushButton(DarkTranslate)
        self.googleButton.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setKerning(True)
        self.googleButton.setFont(font)
        self.googleButton.setMouseTracking(False)
        self.googleButton.setAutoFillBackground(False)
        self.googleButton.setInputMethodHints(QtCore.Qt.ImhNone)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../icons/darkTheme/google3.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.googleButton.setIcon(icon4)
        self.googleButton.setCheckable(True)
        self.googleButton.setChecked(True)
        self.googleButton.setAutoRepeat(False)
        self.googleButton.setAutoExclusive(True)
        self.googleButton.setAutoDefault(True)
        self.googleButton.setDefault(False)
        self.googleButton.setFlat(False)
        self.googleButton.setObjectName("googleButton")
        self.horizontalLayout_2.addWidget(self.googleButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DarkTranslate)
        QtCore.QMetaObject.connectSlotsByName(DarkTranslate)
        DarkTranslate.setTabOrder(self.outputText, self.previousButton)
        DarkTranslate.setTabOrder(self.previousButton, self.nextButton)
        DarkTranslate.setTabOrder(self.nextButton, self.toolButton)
        DarkTranslate.setTabOrder(self.toolButton, self.copyButton)
        DarkTranslate.setTabOrder(self.copyButton, self.fromTranslateBox)
        DarkTranslate.setTabOrder(self.fromTranslateBox, self.swapButton)
        DarkTranslate.setTabOrder(self.swapButton, self.toTranslateBox)
        DarkTranslate.setTabOrder(self.toTranslateBox, self.googleButton)

    def retranslateUi(self, DarkTranslate):
        _translate = QtCore.QCoreApplication.translate
        DarkTranslate.setWindowTitle(_translate("DarkTranslate", "DarkTranslate"))
        self.toolButton.setText(_translate("DarkTranslate", "..."))
        self.fromTranslateBox.setCurrentText(_translate("DarkTranslate", "Auto"))
        self.fromTranslateBox.setItemText(0, _translate("DarkTranslate", "Auto"))
        self.toTranslateBox.setItemText(0, _translate("DarkTranslate", "Auto"))
        self.translateButton.setText(_translate("DarkTranslate", "Translate"))
        self.googleButton.setText(_translate("DarkTranslate", "Google"))

