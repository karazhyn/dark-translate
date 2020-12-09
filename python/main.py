from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow

import os
import sys
sys.path.append("..")

import re
import threading
import time
import urllib.parse

import pyperclip
import vlc
from googletrans import LANGCODES, LANGUAGES, Translator
from googletrans.gtoken import TokenAcquirer
from pynput import keyboard
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.Qt import QApplication, QClipboard
from PyQt5.QtCore import QSettings

import module
import shortcuts
from prototype1v5 import Ui_DarkTranslate
from settingsWindow import Ui_SettingsWindow
from userProfile import (SETTINGS_CUSTOM, SETTINGS_DEFAULT, SHORTCUTS_CUSTOM,
                         SHORTCUTS_DEFAULT)



class AppContext(ApplicationContext):
    def __init__(self, *args, **kwargs):
        super(AppContent, self).__init__(*args, **kwargs)
        self.window = Window()

    def run(self):
        self.window.show()
        return self.app.exec_()



class myWindow(QtWidgets.QDialog):
    def __init__(self):
        super(myWindow, self).__init__()
        
        self.ui = Ui_DarkTranslate()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('../icons/darkTheme/logoDark.png'))

        self.ui.translateButton.clicked.connect(self.translateButton)# connecting the clicked signal with translateButton slot
        self.ui.copyButton.clicked.connect(self.copyButton)          # same
        self.ui.previousButton.clicked.connect(self.previousButton)    
        self.ui.nextButton.clicked.connect(self.nextButton)                         
        self.ui.swapButton.clicked.connect(self.swapButton)                         
        self.ui.fromTranslateBox.currentIndexChanged.connect(self.fromTranslateBox) 
        self.ui.toTranslateBox.currentIndexChanged.connect(self.toTranslateBox)
        self.ui.toolButton.clicked.connect(lambda: self.settingsWindow.exec_())
        self.ui.googleButton.installEventFilter(self)   #make them able to read events

        self.settingsWindow = QtWidgets.QDialog()
        self.settingsWindow.ui = Ui_SettingsWindow()
        self.settingsWindow.ui.setupUi(self.settingsWindow)

        self.settingsWindow.ui.themeBox.addItem('Dark theme')
        self.settingsWindow.ui.themeBox.addItem('Light theme')
        # self.settingsWindow.ui.themeBox.addItem('System GTK theme')
        self.settingsWindow.ui.themeBox.currentIndexChanged.connect(self.themeBox)
        self.settingsWindow.ui.autoTranslationCheckbox.stateChanged.connect(self.autoTranslationChanged)
        self.settingsWindow.ui.reTranslationCheckbox.stateChanged.connect(self.reTranslationChanged)
        self.settingsWindow.ui.translationServicesCheckbox.stateChanged.connect(self.translationServicesChanged)
        self.settingsWindow.ui.highlightTranslationCheckbox.stateChanged.connect(self.highlightTranslationChanged)

        self.settingsWindow.ui.buttonBox.button(QtWidgets.QDialogButtonBox.RestoreDefaults).clicked.connect(self.restoreDefaults)
        self.settingsWindow.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Save).clicked.connect(self.saveShortcuts)
        self.settingsWindow.ui.labelAuthor.setText('<a href=https://github.com/karazhyn><font color=#1471fc>karazhyn</font></a>')
        self.settingsWindow.ui.labelEmail.setText('<a href="mailto:h00dinixx12@gmail.com"><font color=#1471fc>h00dinixx12@gmail.com</font></a>')

        for lang in LANGCODES: #insert languages to combobox
            self.ui.fromTranslateBox.addItem(lang.title())
            self.ui.toTranslateBox.addItem(lang.title())
        self.ui.toTranslateBox.setStyleSheet('combobox-popup: 0') #fixing maxVisibleItems issue
        self.ui.fromTranslateBox.setStyleSheet('combobox-popup: 0')
        # self.ui.fromTranslateBox.setMaxVisibleItems(10) #does not work with "fusion" gtk style
        self.ui.fromTranslateBox.view().setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded) #activating scrooll bar in comboBox
        self.ui.toTranslateBox.view().setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        
        self.destInd = 0
        self.cache = []
        self.cacheid = 0
        self.srcInfo = ''
        self.srcLanguage = 'auto'
        self.destInfo = ''
        self.destLanguage = 'en'
        self.audioUrl = ''
        self.theme = ''
        self.autoBool = True
        self.textOneSecondAgo = ''
        self.langFromOneSecondAgo = 0
        self.langToOneSecondAgo = 0
                
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.ui.srcPronounceButton = QtWidgets.QPushButton(self) #a Source Pronounce Button 
        self.ui.destPronounceButton = QtWidgets.QPushButton(self) #a Destination Pronounce Button
        self.ui.srcPronounceButton.setSizePolicy(sizePolicy)
        self.ui.destPronounceButton.setSizePolicy(sizePolicy)
        self.ui.srcPronounceButton.setMaximumSize(QtCore.QSize(25, 25))
        self.ui.destPronounceButton.setMaximumSize(QtCore.QSize(25, 25))

        self.ui.srcPronounceButton.setToolTip('Pronounce source text') #tool tips
        self.ui.destPronounceButton.setToolTip('Pronounce translated text')
        self.settingsWindow.ui.buttonBox.button(QtWidgets.QDialogButtonBox.RestoreDefaults).setToolTip('Cache will be cleared')
        self.ui.copyButton.setToolTip('Copy translation to the clipboard')
        self.ui.toolButton.setToolTip('Application settings')
        self.ui.swapButton.setToolTip('Swap languages')
        self.ui.nextButton.setToolTip('Next cached translation')
        self.ui.previousButton.setToolTip('Previous cached translation')
        self.ui.fromTranslateBox.setToolTip('Source language')
        self.ui.toTranslateBox.setToolTip('Destination language')
        self.settingsWindow.ui.highlightTranslationCheckbox.setToolTip("'Global Translate' hotkey translates text from clipboard as default. "
                                                                       "\nIf you turn this checkbox on text highlighted by cursor will be translated "
                                                                       "by 'Global Translate' ")

        module.loadData(self) #call of the function that loads settings saved to .conf file
        module.themeLoader(self) #function that settings current theme
        shortcuts.shortcutsLoader(self) #load shortcuts 

        self.cacheId = len(self.cache) #a nonexistent id yet

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/%s/headphones.png"%self.theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.srcPronounceButton.setIcon(icon2)
        self.ui.destPronounceButton.setIcon(icon2)
        if SETTINGS_CUSTOM.get('translationServicesCheckbox', True): #translation services panel visibility
            self.ui.googleButton.setVisible(True)
        else: self.ui.googleButton.setVisible(False)

        self.ui.srcPronounceButton.setStyleSheet("border: 0px")
        self.ui.destPronounceButton.setStyleSheet("border: 0px")
        self.ui.srcPronounceButton.setObjectName('srcPronounceButton')
        self.ui.destPronounceButton.setObjectName('destPronounceButton')
        self.ui.srcPronounceButton.installEventFilter(self)
        self.ui.destPronounceButton.installEventFilter(self)
        self.ui.srcPronounceButton.clicked.connect(self.srcPronounceButton)
        self.ui.destPronounceButton.clicked.connect(self.destPronounceButton) 

        self.boolSrc = True  #bool srcPronounceButton. Initialize button status as "ready to play"
        self.boolDest = True #bool destPronounceButton. Initialize button status as "ready to play"

        for obj in ['translateEdit', 'globaltranslateEdit', 'swapEdit', 'copyEdit', 'srcPronounceEdit', 'destPronounceEdit']:
            eval(f'self.settingsWindow.ui.{obj}.installEventFilter(self)') #install event filter on every textEdit widget in settings->shortcuts

        self.timer = QtCore.QTimer(self) 
        self.timer.setSingleShot(False)
        self.timer.setInterval(1500) #tries to translate every 1500 milliseconds
        self.timer.timeout.connect(self.autoTranslation) #connects autoTranslation function to the timer
        self.timer.start() 

        self.paintTimer = QtCore.QTimer(self) 
        self.paintTimer.setSingleShot(False)
        self.paintTimer.setInterval(300) #tries to paint pronounce buttons every 300 milliseconds
        self.paintTimer.timeout.connect(self.movePronounceButton) #connects movePronounceButton function to the timer
        self.paintTimer.start() 

        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start() #should start\stop listener every time when shortcut's LineEdit is focused\unfocused?


    def translateButton(self):
        inputText = self.ui.inputText.toPlainText().strip()
        if inputText: #if not empty
            translator = Translator()
            global translatedText

            translatedText = translator.translate(inputText, src=self.srcLanguage, dest=self.destLanguage)
            extraData = translatedText.extra_data

            cache = self.cache
            if cache:   #if not empty                      #for avoiding first launch exception self.cache should have any values
                if self.cacheId != len(cache):             #doesnt save it if you are in the cache now 
                    if inputText != cache[self.cacheId]:   #and translating already cached words 
                        self.cacheId = len(cache)
                        cache.append(inputText) 
                else:                                      #if you are not in the cache now and just translating new words it will works fine
                    self.cacheId = len(cache)              #cacheId should be (the last one+1) due to correct cache navigation
                    cache.append(inputText) 
            else: 
                self.cacheId = len(cache)
                cache.append(inputText) 

            self.ui.outputText.clear()
            self.ui.outputText.insertHtml('<font color=\'%s\'>%s</font>'%(self.colorSolid, translatedText.text))  #insert translated text
            if translatedText.pronunciation != None:
                self.ui.outputText.insertHtml('<br><font color=\'%s\'>/%s/</font>'%(self.colorAdd, translatedText.pronunciation))  #insert translated text

            if self.ui.fromTranslateBox.currentIndex() == 0:
                self.srcInfo = LANGUAGES.get(translatedText.src, None).title()  
                self.ui.fromTranslateBox.setItemText(0, 'Auto (%s)'%self.srcInfo)   #make title for fromTranslateButton's 0 index if chosen
            if self.ui.toTranslateBox.currentIndex() == 0:
                self.destLanguage = 'en' #default destination language is English
                self.ui.toTranslateBox.setCurrentText("English") 
            self.ui.status.setText('<font color=\'%s\'>&nbsp;%s | <u>%s</u>><u>%s</u></font>' 
                                    %(self.color, self.ui.googleButton.text(), self.ui.fromTranslateBox.currentText(),
                                      self.ui.toTranslateBox.currentText()))
           
            extra = extraData.get('all-translations', None)
            definitions = extraData.get('definitions', None)
            examples = extraData.get('examples', None)

            if extra != None:                                   #insert extra translations if exist
                self.ui.outputText.insertHtml('<br><br><font color=\'%s\'><b>%s</b></font> '%(self.colorSolid, extra[0][0])) #insert and format text
                for i in range(len(extra[0][1])):
                    synonym = extra[0][2][i][0] 
                    synonyms = ', '.join(extra[0][2][i][1])
                    self.ui.outputText.insertHtml('<br>&nbsp;&nbsp;&nbsp;&nbsp;<font color=\'%s\'> %s:</font> <font color=\'%s\'><i>%s</i></font>'
                                                    %(self.colorSolid, synonym, self.colorAdd, synonyms)) #insert and format text
            
            if definitions != None:                             #insert definitions if exist
                self.ui.outputText.insertHtml('<br><br><i><font color=\'%s\'>definitions:</font></i>'%self.colorAdd)
                for part in range(len(definitions)):
                    part2 = definitions[part][0]
                    if part2 != '': self.ui.outputText.insertHtml('<br><font color=\'%s\'><b>%s</b></font> '%(self.colorSolid, part2))
                    
                    for i in range(len(definitions[part][1])):
                        example = definitions[part][1][i][0]
                        self.ui.outputText.insertHtml('<br>&nbsp;&nbsp;&nbsp;&nbsp; <font color=\'%s\'><i>%s</i></font>' %(self.colorSolid,example))
            
            if examples != None:                                #insert examples if exist
                self.ui.outputText.insertHtml('<br><br><font color=\'%s\'><b>examples:</b></font>'%self.colorSolid)
                for i in range(len(examples[0])):
                    example = examples[0][i][0]
                    self.ui.outputText.insertHtml('<br>&nbsp;&nbsp;&nbsp;&nbsp;<font color=\'%s\'> <i>%s</i></font>' %(self.colorAdd, example))

    def globalTranslate(self): #slot from shortcuts.py -> globalShortcutsLoader()
        if SETTINGS_CUSTOM.get('highlightTranslationCheckbox', False) == True:
            kb = keyboard.Controller()
            kb.press(keyboard.Key.ctrl)
            kb.press('c')
            kb.release('c')
            kb.release(keyboard.Key.ctrl)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.show()
        self.raise_()
        self.activateWindow()
        self.ui.inputText.setPlainText(pyperclip.paste())
        self.ui.translateButton.click()

    def copyButton(self):
        if 'translatedText' in globals(): QApplication.clipboard().setText(translatedText.text) 
     
    def previousButton(self):
        self.ui.inputText.clear()
        self.cacheId -= 1
        if self.cacheId < 0: #handling Index out of Range Exception
            self.cacheId = 0
        
        if len(self.cache) != 0:
            self.ui.inputText.insertPlainText(self.cache[self.cacheId])

    def nextButton(self):
        self.ui.inputText.clear()
        self.cacheId += 1
        if self.cacheId > len(self.cache)-1:  #handling Index out of Range Exception
            self.cacheId = len(self.cache)-1
       
        if len(self.cache) != 0:
            self.ui.inputText.insertPlainText(self.cache[self.cacheId])

    def fromTranslateBox(self):
        if self.ui.fromTranslateBox.currentIndex() == 0:
            self.srcLanguage = 'auto' #let google(translation service) determine the source language
        else:
            lang = self.ui.fromTranslateBox.currentText().lower()
            self.srcLanguage = LANGCODES.get(lang, None)
            # print('translate from', lang)
        # self.ui.translateButton.click() #push the translateButton
     
    def toTranslateBox(self):
        if self.ui.toTranslateBox.currentIndex() == 0: 
            self.destLanguage = 'en' #default destination language is English
            self.ui.toTranslateBox.setCurrentText("English")
            return
        else:
            lang = self.ui.toTranslateBox.currentText().lower()
            # print('to', lang)
            self.destLanguage = LANGCODES.get(lang, None)
        # self.ui.translateButton.click() #push the translateButton
   
    def themeBox(self):
        if self.settingsWindow.ui.themeBox.currentIndex() == 0:
            self.theme = 'darkTheme'
        elif self.settingsWindow.ui.themeBox.currentIndex() == 1: 
            self.theme = 'lightTheme'
        # else: self.theme = 'systemTheme'

        module.themeLoader(self)
        self.ui.translateButton.click() #push the translateButton in order to change the text colors

    def autoTranslation(self): #tries to autoTranslate every 1.5 seconds (look at self.timer)
        if SETTINGS_CUSTOM.get('autoTranslationCheckbox', True) == True:
            # print('tried to autoTranslate')
            self.textRightNow = self.ui.inputText.toPlainText()
            self.langFromRightNow = self.ui.fromTranslateBox.currentIndex()
            self.langToRightNow = self.ui.toTranslateBox.currentIndex()

            #allows to translate text from one language to another when source\destination language changed but text haven't
            if self.textOneSecondAgo.strip() != self.textRightNow.strip() \
                or self.langToOneSecondAgo != self.langToRightNow \
                or self.langFromOneSecondAgo != self.langFromOneSecondAgo: 
                
                self.translateButton()
                self.textOneSecondAgo = self.textRightNow
                self.langFromOneSecondAgo = self.langFromRightNow
                self.langToOneSecondAgo = self.langToRightNow
                # print('translated by autoTranslation')

    def autoTranslationChanged(self, state): #autoTranslationCheckbox status changed
        if state == QtCore.Qt.Checked:
            SETTINGS_CUSTOM['autoTranslationCheckbox'] = True
        else:
            SETTINGS_CUSTOM['autoTranslationCheckbox'] = False

    def highlightTranslationChanged(self,state):
        if state == QtCore.Qt.Checked:
            SETTINGS_CUSTOM['highlightTranslationCheckbox'] = True
        else:
            SETTINGS_CUSTOM['highlightTranslationCheckbox'] = False

    def reTranslationChanged(self, state): #reverse translation checkbox status changed
        if state == QtCore.Qt.Checked:
            SETTINGS_CUSTOM['reTranslationCheckbox'] = True
        else:
            SETTINGS_CUSTOM['reTranslationCheckbox'] = False

    def translationServicesChanged(self, state): #visible google button checkbox
        if state == QtCore.Qt.Checked:
            SETTINGS_CUSTOM['translationServicesCheckbox'] = True
            self.ui.googleButton.setVisible(True)
        else:
            SETTINGS_CUSTOM['translationServicesCheckbox'] = False
            self.ui.googleButton.setVisible(False)

    def restoreDefaults(self):
        with open(str(self.settings.fileName()), 'w') as f: #reset the darktranslate.conf file
            f.write('')
        module.loadData(self)
        self.theme = 'darkTheme'
        module.themeLoader(self)

        shortcuts.shortcutsDisconnect(self)
        shortcuts.shortcutsDefaultLoader(self)

        python = sys.executable #restart the program in order to load default settings correctly
        os.execl(python, python, * sys.argv)

    def swapButton(self):
        # print(f'Source lang: {self.srcLanguage}')
        if SETTINGS_CUSTOM.get('reTranslationCheckbox', True):
            if 'translatedText' in globals(): 
                self.ui.inputText.clear()
                self.ui.inputText.insertPlainText(translatedText.text)
        srcInd = self.ui.fromTranslateBox.currentIndex() #temp variable to save current fromTranslateBox index
        if srcInd == 0:
            self.ui.fromTranslateBox.setCurrentIndex(self.ui.toTranslateBox.currentIndex()) #set fromTranslateBox index = toTranslateBox index 
            self.ui.toTranslateBox.setCurrentText(self.srcInfo) #set toTranslateBox index = language that google determined on auto
        else:
            self.ui.fromTranslateBox.setCurrentIndex(self.ui.toTranslateBox.currentIndex()) #set fromTranslateBox index = toTranslateBox index 
            self.ui.toTranslateBox.setCurrentIndex(srcInd)  #set toTranslateBox index = fromTranslateBox index
        
    def srcPronounceButton(self):
        try: #temporarily does not work because of 'googletrans' lib issue
            if 'translatedText' in globals():
                inputText = self.ui.inputText.toPlainText()  #get entered text
                if inputText.strip() != '':  #if string is not empty
                    if self.boolSrc == True:
                        token = TokenAcquirer().do(inputText)

                        self.audioUrl = f"https://translate.google.com/translate_tts?ie=UTF-8&q={urllib.parse.quote(inputText)}"\
                                        f"&tl={translatedText.src}&tk={token}&client=webapp" #url to play the sound from source 
                        # print(self.audioUrl)

                        global p #Declare p(player) variable 
                        p = vlc.MediaPlayer(self.audioUrl) #initialize p(player) variable
                        eventP = p.event_manager()
                        eventP.event_attach(vlc.EventType.MediaPlayerEndReached, self.eventEnd) 
                        p.audio_set_volume(100)
                        p.play()

                        icon3 = QtGui.QIcon()
                        icon3.addPixmap(QtGui.QPixmap("../icons/%s/stop.png"%self.theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        self.ui.srcPronounceButton.setIcon(icon3)
                        self.boolSrc = False #change button status to "ready to stop"
                    else: 
                        # p.set_pause(1)
                        p.stop()        #does not work properly. Works only in case with instantly stop (probably due to url request properties)
                        icon2 = QtGui.QIcon()
                        icon2.addPixmap(QtGui.QPixmap("../icons/%s/headphones.png"%self.theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        self.ui.srcPronounceButton.setIcon(icon2)
                        self.boolSrc = True #return button status to "ready to play"
        except: pass

    def destPronounceButton(self):
        try: #temporarily does not work because of 'googletrans' lib issue
            if 'translatedText' in globals():
                if self.ui.outputText.toPlainText().strip() != '':  #if string is not empty
                    if self.boolDest == True:
                        token = TokenAcquirer().do(translatedText.text)

                        self.audioUrl = f"https://translate.google.com/translate_tts?ie=UTF-8&q={urllib.parse.quote(translatedText.text)}"\
                                        f"&tl={translatedText.dest}&tk={token}&client=webapp" #url to play the sound from destination(translated text)
                        # print(self.audioUrl)

                        global p2 #Declare p(player) variable 
                        p2 = vlc.MediaPlayer(self.audioUrl) #initialize p(player) variable
                        eventP = p2.event_manager()
                        eventP.event_attach(vlc.EventType.MediaPlayerEndReached, self.eventEnd2) 
                        p2.audio_set_volume(100)
                        p2.play()

                        icon3 = QtGui.QIcon()
                        icon3.addPixmap(QtGui.QPixmap("../icons/%s/stop.png"%self.theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        self.ui.destPronounceButton.setIcon(icon3)
                        self.boolDest = False #change button status to "ready to stop"
                    else: 
                        # p.set_pause(1)
                        p2.stop()        #does not work properly. Works only in case with instantly stop (probably due to url request properties)
                        icon2 = QtGui.QIcon()
                        icon2.addPixmap(QtGui.QPixmap("../icons/%s/headphones.png"%self.theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        self.ui.destPronounceButton.setIcon(icon2)
                        self.boolDest = True #return button status to "ready to play"
        except: pass

    def movePronounceButton(self): #'bind' pronounce buttons to bottom right corner
        inputTextX = self.ui.inputText.geometry().bottomRight().x()-45
        inputTextY = self.ui.inputText.geometry().bottomRight().y()-30
        outputTextX = self.ui.outputText.geometry().bottomRight().x()-45
        outputTextY = self.ui.outputText.geometry().bottomRight().y()-30
        if self.ui.srcPronounceButton.geometry().topLeft().x() != inputTextX \
            or self.ui.srcPronounceButton.geometry().topLeft().y() != inputTextY: #if buttons are not already in the corner
            self.ui.srcPronounceButton.move(inputTextX, inputTextY) #moves pronounce button to bottom right corner
            self.ui.destPronounceButton.move(outputTextX, outputTextY)

    def saveShortcuts(self):
        shortcuts.shortcutsDisconnect(self)
        shortcuts.shortcutsLoader(self)

        self.saveSettings() #save updated settings locally
        self.settings.sync() #save updated settings to .conf file

        python = sys.executable              #
        os.execl(python, python, * sys.argv) # Reload window. Should be done in order to correct saving new shortcuts

    def saveSettings(self):
        # print(self.settings.fileName()) #path to .conf file
        self.settings.setValue('windowSize', self.size())
        self.settings.setValue('windowPosition', self.pos())

        self.settings.setValue('destLanguage', self.destLanguage) #save last chosen language
        self.settings.setValue('destInd', self.ui.toTranslateBox.currentIndex()) #save last chosen index 

        self.settings.setValue('autoTranslationCheckbox', str(SETTINGS_CUSTOM.get('autoTranslationCheckbox', True)))
        self.settings.setValue('reTranslationCheckbox', str(SETTINGS_CUSTOM.get('reTranslationCheckbox', True)))
        self.settings.setValue('translationServicesCheckbox', str(SETTINGS_CUSTOM.get('translationServicesCheckbox', True)))
        self.settings.setValue('highlightTranslationCheckbox', str(SETTINGS_CUSTOM.get('highlightTranslationCheckbox', False)))
        if self.cache: #if cache is not empty
            self.settings.setValue('cache', self.cache) #save translated words 

        self.settings.setValue('theme', self.theme) #save theme

        self.settings.beginGroup('Shortcuts')
        for shortcutName in SHORTCUTS_DEFAULT: #save shortcuts to .conf
            # print(f'ShortcutName is: {shortcutName}')
            self.settings.setValue(shortcutName, SHORTCUTS_CUSTOM.get(shortcutName,SHORTCUTS_DEFAULT.get(shortcutName)))
            # print(self.settings.value('shortcutName'))

    def eventEnd(self, p): #change pronounce button icon when sound is over. 'p' is player
        self.boolSrc = True
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/%s/headphones.png"%self.theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.srcPronounceButton.setIcon(icon2)
    
    def eventEnd2(self, p): #change pronounce button icon when sound is over. 'p' is player
        self.boolDest = True
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/%s/headphones.png"%self.theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.destPronounceButton.setIcon(icon2)

    def eventFilter(self, object, event):
        obj = object.objectName()
        if event.type() == QtCore.QEvent.Paint: #could be use diff event types: 
                                                #.Move(does not work with hidden element)\.Resize(vertical bug + previous)\.Paint(size reduction bug) 
            self.movePronounceButton()
            
        if event.type() == QtCore.QEvent.HoverEnter: #google\evil button feature
            if obj == "srcPronounceButton":
                self.ui.srcPronounceButton.setStyleSheet("border: 1px solid #d9d9d9")
                return True
            if obj == "destPronounceButton":
                self.ui.destPronounceButton.setStyleSheet("border: 1px solid #d9d9d9")
                return True                
            if obj == 'googleButton':
                self.ui.googleButton.setText('Evil')
                self.ui.status.setText('<font color=\'%s\'>&nbsp;%s | <u>%s</u>><u>%s</u></font>' 
                                        %(self.color, self.ui.googleButton.text(), self.ui.fromTranslateBox.currentText(),
                                          self.ui.toTranslateBox.currentText()))
                return True
           
        if event.type() == QtCore.QEvent.HoverLeave: #google\evil button feature
            if obj == "googleButton":
                self.ui.googleButton.setText('Google')
                self.ui.status.setText('<font color=\'%s\'>&nbsp;%s | <u>%s</u>><u>%s</u></font>'
                                        %(self.color, self.ui.googleButton.text(), self.ui.fromTranslateBox.currentText(),
                                        self.ui.toTranslateBox.currentText()))
                return True
            if obj == "srcPronounceButton":
                self.ui.srcPronounceButton.setStyleSheet("border: 0px")
                return True
            if obj == "destPronounceButton":
                self.ui.destPronounceButton.setStyleSheet("border: 0px")
                return True

        if event.type() == QtCore.QEvent.FocusIn: #text "Press combination" when focusIn LineEdit
            
            if obj in ['translateEdit', 'globaltranslateEdit', 'swapEdit', 'copyEdit', 'srcPronounceEdit', 'destPronounceEdit']:
                eval(f"self.settingsWindow.ui.{obj}.setText('Press combination')")
                
                #its better to turning listener off\on when necessary 
                # with keyboard.Listener( 
                #     on_press=self.on_press,
                #     on_release=self.on_release) as self.listener:
                #     self.listener.join()
                #     self.listener.start()
                return True

        if event.type() == QtCore.QEvent.FocusOut: #show saved shortcut when unFocused
            if obj == 'translateEdit':
                self.settingsWindow.ui.translateEdit.setText(f"{SHORTCUTS_CUSTOM.get('translateButton',SHORTCUTS_DEFAULT.get('translateButton'))}")
                return True
            if obj == 'globaltranslateEdit':
                self.settingsWindow.ui.globaltranslateEdit.setText(f"{SHORTCUTS_CUSTOM.get('globaltranslateButton',SHORTCUTS_DEFAULT.get('globaltranslateButton'))}")
                return True
            if obj == 'swapEdit':
                self.settingsWindow.ui.swapEdit.setText(f"{SHORTCUTS_CUSTOM.get('swapButton',SHORTCUTS_DEFAULT.get('swapButton'))}")
                return True
            if obj == 'copyEdit':
                self.settingsWindow.ui.copyEdit.setText(f"{SHORTCUTS_CUSTOM.get('copyButton',SHORTCUTS_DEFAULT.get('copyButton'))}")
                return True
            if obj == 'srcPronounceEdit':
                self.settingsWindow.ui.srcPronounceEdit.setText(f"{SHORTCUTS_CUSTOM.get('srcPronounceButton',SHORTCUTS_DEFAULT.get('srcPronounceButton'))}")
                return True
            if obj == 'destPronounceEdit':
                self.settingsWindow.ui.destPronounceEdit.setText(f"{SHORTCUTS_CUSTOM.get('destPronounceButton',SHORTCUTS_DEFAULT.get('destPronounceButton'))}")
                return True
        # self.listener.stop()
        return False

    def on_press(self, key):
        if self.settingsWindow.isActiveWindow(): #if settings window is active
            obj = self.settingsWindow.focusWidget().objectName()
            if obj in ['translateEdit', 'globaltranslateEdit', 'swapEdit', 'copyEdit', 'srcPronounceEdit', 'destPronounceEdit']: #if focus on one of this objects
                if key == keyboard.Key.enter: 
                    key = 'Key.return' #change key name in order to fit pynput lib (enter=return)

                try:
                    # if Controller.modifiers
                    eval(f"self.settingsWindow.ui.{obj}.insert('+{str(key.char).capitalize()}')")
                    # print('{0} pressed'.format(key.char))
                    # self.listener.stop()
                except AttributeError:
                    # print(self.settingsWindow.ui.translateEdit.text())
                    if eval(f"self.settingsWindow.ui.{obj}.text()") == 'Press combination':
                        eval(f"self.settingsWindow.ui.{obj}.setText('{str(key).split('.')[1].capitalize()}')") 
                        # print('{0} pressed'.format(key))
                    else: #if any modifiers have alredy pressed
                        eval(f"self.settingsWindow.ui.{obj}.insert('+{str(key).split('.')[1].capitalize()}')") #format shortcuts to fit pynput lib

    def on_release(self, key):
        if self.settingsWindow.isActiveWindow(): #if settings window is active
            obj = self.settingsWindow.focusWidget().objectName()
            if obj in ['translateEdit', 'globaltranslateEdit', 'swapEdit', 'copyEdit', 'srcPronounceEdit', 'destPronounceEdit']:
                name = f"{re.findall('[^A-Z]*', obj)[0]}Button" #get the SHORTCUTS_CUSTOM(dictionary) key attached to this EditLine 
                                                                #(first part of shortcut key and LineEdit object is equal)
                SHORTCUTS_CUSTOM[name] = eval(f"self.settingsWindow.ui.{obj}.text()")
                # print(SHORTCUTS_CUSTOM[name])
                # print('{0} released'.format(key))
                if key == keyboard.Key.esc:
                    # Stop listener if esc pressed
                    return False


    def closeEvent(self, e):
        self.saveSettings()

        # print('CLOSE EVENT')
        # print(self.srcLanguage)
        # print(self.destLanguage)

if __name__ == '__main__':
    ctx = ApplicationContext()
    w = myWindow()
    w.show() 
    ctx.app.exec_()    
 
    
