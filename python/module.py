from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtCore import QSettings
from settingsWindow import Ui_SettingsWindow
from userProfile import SETTINGS_DEFAULT, SETTINGS_CUSTOM, SHORTCUTS_DEFAULT, SHORTCUTS_CUSTOM


def themeLoader(self): #function that settings current theme
    if self.theme == '':
        try:
            if self.settings.value('theme') != None:
                self.theme = self.settings.value('theme')
            else: self.theme = 'darkTheme'
        except:
            self.theme = 'darkTheme'
    else: 
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/%s/headphones.png"%self.theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.destPronounceButton.setIcon(icon)
        self.ui.srcPronounceButton.setIcon(icon)


    #change icons according to the chosen theme
    icon = QtGui.QIcon() 
    icon.addPixmap(QtGui.QPixmap("../icons/%s/left-arrow.png"%self.theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.ui.previousButton.setIcon(icon)
    icon.addPixmap(QtGui.QPixmap("../icons/%s/right-arrow.png"%self.theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.ui.nextButton.setIcon(icon)
    icon.addPixmap(QtGui.QPixmap("../icons/%s/gear.png"%self.theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.ui.toolButton.setIcon(icon)
    icon.addPixmap(QtGui.QPixmap("../icons/%s/copy.png"%self.theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.ui.copyButton.setIcon(icon)
    # icon.addPixmap(QtGui.QPixmap("../icons/%s/adjust.png"%self.theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    # self.ui.preferencesButton.setIcon(icon)
    icon.addPixmap(QtGui.QPixmap("../icons/%s/swap.png"%self.theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.ui.swapButton.setIcon(icon)
    icon.addPixmap(QtGui.QPixmap("../icons/%s/click.png"%self.theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.ui.translateButton.setIcon(icon)
    icon.addPixmap(QtGui.QPixmap("../icons/%s/google.png"%self.theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.ui.googleButton.setIcon(icon)
    icon.addPixmap(QtGui.QPixmap("../icons/%s/logoDark.png"%self.theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.settingsWindow.ui.labelIcon.setPixmap(QtGui.QPixmap("../icons/%s/logoDark.png"%self.theme).scaled(60,60, transformMode=QtCore.Qt.SmoothTransformation))
    self.settingsWindow.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Save).setIcon(QtGui.QIcon())
    self.setWindowIcon(QtGui.QIcon('../icons/%s/logoDark.png'%self.theme))


    if self.theme == 'darkTheme': #change text style etc. according to the chosen theme
        QtWidgets.QPushButton.setStyleSheet(self, open('darkStyle.css').read()) #theme css profile

        for item in range(self.ui.horizontalLayout_3.count()):
            self.ui.horizontalLayout_3.itemAt(item).widget().setStyleSheet('background-color: #202020; color: #ffffff;')
        for item in [0,1,3]:
            self.ui.horizontalLayout_4.itemAt(item).widget().setStyleSheet('background-color: #202020; color: #ffffff;')
        for item in range(self.ui.horizontalLayout_2.count()):
            self.ui.horizontalLayout_2.itemAt(item).widget().setStyleSheet('background-color: #202020; color: #ffffff;')
        self.settingsWindow.ui.horizontalLayout.itemAt(0).widget().setStyleSheet('color: #ffffff;')
        self.settingsWindow.ui.horizontalLayout.itemAt(1).widget().setStyleSheet('background-color: #202020; color: #ffffff;')
        self.settingsWindow.ui.buttonBox.setStyleSheet('background-color: #202020; color: #ffffff;')
        self.settingsWindow.setStyleSheet(open('darkStyle.css').read())
        self.color = '#b6b6b6'
        self.colorAdd = '#b6b6b6'
        self.colorSolid = '#ffffff'
        self.settingsWindow.ui.themeBox.setCurrentIndex(0)
        

    if self.theme == 'lightTheme': 
        QtWidgets.QPushButton.setStyleSheet(self, open('lightStyle.css').read()) #theme css profile

        for item in range(self.ui.horizontalLayout_3.count()):
            self.ui.horizontalLayout_3.itemAt(item).widget().setStyleSheet('background-color: #f5f5f5; color: #000000;')
        for item in [0,1,3]:
            self.ui.horizontalLayout_4.itemAt(item).widget().setStyleSheet('background-color: #f5f5f5; color: #000000;')
        for item in range(self.ui.horizontalLayout_2.count()):
            self.ui.horizontalLayout_2.itemAt(item).widget().setStyleSheet('background-color: #f5f5f5; color: #000000;')
        self.settingsWindow.ui.horizontalLayout.itemAt(0).widget().setStyleSheet('color: #000000;')
        self.settingsWindow.ui.horizontalLayout.itemAt(1).widget().setStyleSheet('background-color: #f5f5f5; color: #000000;')
        self.settingsWindow.ui.buttonBox.setStyleSheet('background-color: #f5f5f5; color: #000000;')
        self.settingsWindow.setStyleSheet(open('lightStyle.css').read())
        self.color = '#505050'
        self.colorAdd = '#707070'
        self.colorSolid = '#000000'
        self.settingsWindow.ui.themeBox.setCurrentIndex(1)
    
    # if self.theme == 'systemTheme': (...)


    if self.ui.toTranslateBox.currentIndex() == 0: #handle status bar bug
        self.destLanguage = 'en' #default destination language is English
        self.ui.toTranslateBox.setCurrentText("English")

    #status bar color etc.
    self.ui.status.setText('<font color=\'%s\'>&nbsp;%s | <u>%s</u>><u>%s</u></font>' 
                        %(self.color, self.ui.googleButton.text(), self.ui.fromTranslateBox.currentText(),
                            self.ui.toTranslateBox.currentText()))



def loadData(self): #function that loads settings saved to .conf fil
    #closeEvent almost the same so it can be optimized

    self.settings = QSettings('darktranslate', 'darktranslate') # .conf file. Saves settings after closing

    mainCheckbox = ['autoTranslationCheckbox', 'reTranslationCheckbox', 'translationServicesCheckbox']

    try: #load main settings
        self.resize(self.settings.value('windowSize'))
        self.move(self.settings.value('windowPosition'))
        self.destLanguage = self.settings.value('destLanguage')

        self.destInd = self.settings.value('destInd')

        self.ui.toTranslateBox.setCurrentIndex(int(self.destInd))

        for name in mainCheckbox:
            if self.settings.value(name) == 'True':
                SETTINGS_CUSTOM[name] = True
            else:
                SETTINGS_CUSTOM[name] = False

        if self.settings.value('highlightTranslationCheckbox') == 'False':
            SETTINGS_CUSTOM['highlightTranslationCheckbox'] = False
        else: SETTINGS_CUSTOM['highlightTranslationCheckbox'] = True
    except: #default config
        self.resize(400, 300)
        self.move(500,400)
        self.destLanguage = "en"
        self.destInd = 21
        self.ui.toTranslateBox.setCurrentIndex(0)
        for name in mainCheckbox:
            SETTINGS_CUSTOM[name] = True
        SETTINGS_CUSTOM['highlightTranslationCheckbox'] = False


    try: #load cache
        self.cache = self.settings.value('cache')
        if self.cache == None:
            self.cache = []
    except: 
        self.cache = []


    for name in SHORTCUTS_DEFAULT:  #load SHORTCUTS_CUSTOM
        self.settings.beginReadArray('Shortcuts') 
        if self.settings.value(name) != None:
            # print(name)
            SHORTCUTS_CUSTOM[name] = self.settings.value(name) #SHORTCUTS_CUSTOM is equal to saved .conf values 
        else:
            SHORTCUTS_CUSTOM[name] = SHORTCUTS_DEFAULT[name] #if .conf does not contain saved shortcut, then custom=default
        self.settings.endArray()


    #set shortcuts widgets text to saved values + installEventFilter
    for [shortcut, index] in zip(SHORTCUTS_CUSTOM.values(), [i for i in range(len(self.settingsWindow.ui.verticalLayout_shortcuts))]): 
        self.settingsWindow.ui.verticalLayout_shortcuts.itemAt(index).itemAt(1).widget().setText(shortcut)
        self.settingsWindow.ui.verticalLayout_shortcuts.itemAt(index).itemAt(1).widget().installEventFilter(self)


    #load check marks
    self.settingsWindow.ui.autoTranslationCheckbox.setChecked(SETTINGS_CUSTOM.get('autoTranslationCheckbox', SETTINGS_DEFAULT.get('autoTranslationCheckbox', True))) #set autoTranslateCheckbox as custom\as default
    self.settingsWindow.ui.reTranslationCheckbox.setChecked(SETTINGS_CUSTOM.get('reTranslationCheckbox', SETTINGS_DEFAULT.get('reTranslationCheckbox', True))) #set reTranslationCheckbox as custom\as default
    self.settingsWindow.ui.translationServicesCheckbox.setChecked(SETTINGS_CUSTOM.get('translationServicesCheckbox', SETTINGS_DEFAULT.get('translationServicesCheckbox', True))) #set autoTranslateCheckbox as custom\as default
    self.settingsWindow.ui.highlightTranslationCheckbox.setChecked(SETTINGS_CUSTOM.get('highlightTranslationCheckbox', SETTINGS_DEFAULT.get('highlightTranslationCheckbox', False))) #set highlightTranslationCheckbox as custom\as default

