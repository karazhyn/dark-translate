# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/nikita/dev/DarkTranslate/scripts/settingsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(358, 284)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsWindow.sizePolicy().hasHeightForWidth())
        SettingsWindow.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SettingsWindow)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(SettingsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.mainTab = QtWidgets.QWidget()
        self.mainTab.setObjectName("mainTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.themeLabel = QtWidgets.QLabel(self.mainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.themeLabel.sizePolicy().hasHeightForWidth())
        self.themeLabel.setSizePolicy(sizePolicy)
        self.themeLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.themeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.themeLabel.setWordWrap(False)
        self.themeLabel.setObjectName("themeLabel")
        self.horizontalLayout.addWidget(self.themeLabel)
        self.themeBox = QtWidgets.QComboBox(self.mainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.themeBox.sizePolicy().hasHeightForWidth())
        self.themeBox.setSizePolicy(sizePolicy)
        self.themeBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.themeBox.setObjectName("themeBox")
        self.horizontalLayout.addWidget(self.themeBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.autoTranslationCheckbox = QtWidgets.QCheckBox(self.mainTab)
        self.autoTranslationCheckbox.setChecked(True)
        self.autoTranslationCheckbox.setTristate(False)
        self.autoTranslationCheckbox.setObjectName("autoTranslationCheckbox")
        self.verticalLayout.addWidget(self.autoTranslationCheckbox)
        self.reTranslationCheckbox = QtWidgets.QCheckBox(self.mainTab)
        self.reTranslationCheckbox.setChecked(True)
        self.reTranslationCheckbox.setObjectName("reTranslationCheckbox")
        self.verticalLayout.addWidget(self.reTranslationCheckbox)
        self.translationServicesCheckbox = QtWidgets.QCheckBox(self.mainTab)
        self.translationServicesCheckbox.setChecked(True)
        self.translationServicesCheckbox.setObjectName("translationServicesCheckbox")
        self.verticalLayout.addWidget(self.translationServicesCheckbox)
        self.highlightTranslationCheckbox = QtWidgets.QCheckBox(self.mainTab)
        self.highlightTranslationCheckbox.setChecked(False)
        self.highlightTranslationCheckbox.setObjectName("highlightTranslationCheckbox")
        self.verticalLayout.addWidget(self.highlightTranslationCheckbox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.tabWidget.addTab(self.mainTab, "")
        self.shortcutsTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shortcutsTab.sizePolicy().hasHeightForWidth())
        self.shortcutsTab.setSizePolicy(sizePolicy)
        self.shortcutsTab.setObjectName("shortcutsTab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.shortcutsTab)
        self.verticalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_shortcuts = QtWidgets.QVBoxLayout()
        self.verticalLayout_shortcuts.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_shortcuts.setObjectName("verticalLayout_shortcuts")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.translateLabel = QtWidgets.QLabel(self.shortcutsTab)
        self.translateLabel.setObjectName("translateLabel")
        self.horizontalLayout_2.addWidget(self.translateLabel)
        self.translateEdit = QtWidgets.QLineEdit(self.shortcutsTab)
        self.translateEdit.setReadOnly(True)
        self.translateEdit.setObjectName("translateEdit")
        self.horizontalLayout_2.addWidget(self.translateEdit, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_shortcuts.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.globaltranslateLabel = QtWidgets.QLabel(self.shortcutsTab)
        self.globaltranslateLabel.setObjectName("globaltranslateLabel")
        self.horizontalLayout_13.addWidget(self.globaltranslateLabel)
        self.globaltranslateEdit = QtWidgets.QLineEdit(self.shortcutsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.globaltranslateEdit.sizePolicy().hasHeightForWidth())
        self.globaltranslateEdit.setSizePolicy(sizePolicy)
        self.globaltranslateEdit.setReadOnly(True)
        self.globaltranslateEdit.setObjectName("globaltranslateEdit")
        self.horizontalLayout_13.addWidget(self.globaltranslateEdit)
        self.verticalLayout_shortcuts.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.swapLabel = QtWidgets.QLabel(self.shortcutsTab)
        self.swapLabel.setObjectName("swapLabel")
        self.horizontalLayout_3.addWidget(self.swapLabel)
        self.swapEdit = QtWidgets.QLineEdit(self.shortcutsTab)
        self.swapEdit.setReadOnly(True)
        self.swapEdit.setObjectName("swapEdit")
        self.horizontalLayout_3.addWidget(self.swapEdit, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_shortcuts.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.copyLabel = QtWidgets.QLabel(self.shortcutsTab)
        self.copyLabel.setObjectName("copyLabel")
        self.horizontalLayout_11.addWidget(self.copyLabel)
        self.copyEdit = QtWidgets.QLineEdit(self.shortcutsTab)
        self.copyEdit.setReadOnly(True)
        self.copyEdit.setObjectName("copyEdit")
        self.horizontalLayout_11.addWidget(self.copyEdit, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_shortcuts.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.srcPronounceLabel = QtWidgets.QLabel(self.shortcutsTab)
        self.srcPronounceLabel.setObjectName("srcPronounceLabel")
        self.horizontalLayout_12.addWidget(self.srcPronounceLabel)
        self.srcPronounceEdit = QtWidgets.QLineEdit(self.shortcutsTab)
        self.srcPronounceEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.srcPronounceEdit.setReadOnly(True)
        self.srcPronounceEdit.setObjectName("srcPronounceEdit")
        self.horizontalLayout_12.addWidget(self.srcPronounceEdit, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_shortcuts.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.destPronounceLabel = QtWidgets.QLabel(self.shortcutsTab)
        self.destPronounceLabel.setObjectName("destPronounceLabel")
        self.horizontalLayout_15.addWidget(self.destPronounceLabel)
        self.destPronounceEdit = QtWidgets.QLineEdit(self.shortcutsTab)
        self.destPronounceEdit.setReadOnly(True)
        self.destPronounceEdit.setObjectName("destPronounceEdit")
        self.horizontalLayout_15.addWidget(self.destPronounceEdit)
        self.verticalLayout_shortcuts.addLayout(self.horizontalLayout_15)
        self.verticalLayout_10.addLayout(self.verticalLayout_shortcuts)
        self.tabWidget.addTab(self.shortcutsTab, "")
        self.infoTab = QtWidgets.QWidget()
        self.infoTab.setObjectName("infoTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.infoTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_4.setContentsMargins(55, -1, 40, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelIcon = QtWidgets.QLabel(self.infoTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelIcon.sizePolicy().hasHeightForWidth())
        self.labelIcon.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.labelIcon.setFont(font)
        self.labelIcon.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelIcon.setObjectName("labelIcon")
        self.horizontalLayout_4.addWidget(self.labelIcon)
        self.labelName = QtWidgets.QLabel(self.infoTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelName.sizePolicy().hasHeightForWidth())
        self.labelName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.labelName.setFont(font)
        self.labelName.setScaledContents(False)
        self.labelName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelName.setObjectName("labelName")
        self.horizontalLayout_4.addWidget(self.labelName)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(40, -1, 72, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelVersionName = QtWidgets.QLabel(self.infoTab)
        self.labelVersionName.setObjectName("labelVersionName")
        self.horizontalLayout_5.addWidget(self.labelVersionName)
        self.labelVersion = QtWidgets.QLabel(self.infoTab)
        self.labelVersion.setObjectName("labelVersion")
        self.horizontalLayout_5.addWidget(self.labelVersion)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(40, -1, 72, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelLicenseName = QtWidgets.QLabel(self.infoTab)
        self.labelLicenseName.setObjectName("labelLicenseName")
        self.horizontalLayout_6.addWidget(self.labelLicenseName)
        self.labelLicense = QtWidgets.QLabel(self.infoTab)
        self.labelLicense.setObjectName("labelLicense")
        self.horizontalLayout_6.addWidget(self.labelLicense)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(40, -1, 71, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.labelAuthorName = QtWidgets.QLabel(self.infoTab)
        self.labelAuthorName.setObjectName("labelAuthorName")
        self.horizontalLayout_9.addWidget(self.labelAuthorName)
        self.labelAuthor = QtWidgets.QLabel(self.infoTab)
        self.labelAuthor.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelAuthor.setTextFormat(QtCore.Qt.RichText)
        self.labelAuthor.setOpenExternalLinks(True)
        self.labelAuthor.setObjectName("labelAuthor")
        self.horizontalLayout_9.addWidget(self.labelAuthor)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(40, -1, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.labelEmailName = QtWidgets.QLabel(self.infoTab)
        self.labelEmailName.setObjectName("labelEmailName")
        self.horizontalLayout_10.addWidget(self.labelEmailName)
        self.labelEmail = QtWidgets.QLabel(self.infoTab)
        self.labelEmail.setObjectName("labelEmail")
        self.horizontalLayout_10.addWidget(self.labelEmail)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.infoTab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setToolTip("")
        self.buttonBox.setToolTipDuration(-1)
        self.buttonBox.setStatusTip("")
        self.buttonBox.setWhatsThis("")
        self.buttonBox.setAccessibleName("")
        self.buttonBox.setAccessibleDescription("")
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.RestoreDefaults|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(SettingsWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Settings"))
        self.themeLabel.setText(_translate("SettingsWindow", "Theme:"))
        self.autoTranslationCheckbox.setText(_translate("SettingsWindow", "Automatically Translation"))
        self.reTranslationCheckbox.setText(_translate("SettingsWindow", "Reverse translation on swap"))
        self.translationServicesCheckbox.setText(_translate("SettingsWindow", "Visible google button"))
        self.highlightTranslationCheckbox.setText(_translate("SettingsWindow", "Translate highlighted text on hotkey"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), _translate("SettingsWindow", "Main"))
        self.translateLabel.setText(_translate("SettingsWindow", "Translate:"))
        self.globaltranslateLabel.setText(_translate("SettingsWindow", "Global translate:"))
        self.swapLabel.setText(_translate("SettingsWindow", "Swap:"))
        self.copyLabel.setText(_translate("SettingsWindow", "Copy:"))
        self.srcPronounceLabel.setText(_translate("SettingsWindow", "Source pronounce:"))
        self.destPronounceLabel.setText(_translate("SettingsWindow", "Destination pronounce:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shortcutsTab), _translate("SettingsWindow", "Shortcuts"))
        self.labelIcon.setText(_translate("SettingsWindow", "Icon"))
        self.labelName.setText(_translate("SettingsWindow", "Dark Translate"))
        self.labelVersionName.setText(_translate("SettingsWindow", "Version:"))
        self.labelVersion.setText(_translate("SettingsWindow", "1.0.0 (alpha)"))
        self.labelLicenseName.setText(_translate("SettingsWindow", "License:"))
        self.labelLicense.setText(_translate("SettingsWindow", "GPL3"))
        self.labelAuthorName.setText(_translate("SettingsWindow", "Author:"))
        self.labelAuthor.setText(_translate("SettingsWindow", "github.com/karazhyn"))
        self.labelEmailName.setText(_translate("SettingsWindow", "E-mail:"))
        self.labelEmail.setText(_translate("SettingsWindow", "h00dinixx12@gmail.com"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.infoTab), _translate("SettingsWindow", "Info"))

