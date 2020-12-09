from PyQt5.Qt import QShortcut, QKeySequence
from pynput import keyboard
from userProfile import SHORTCUTS_DEFAULT, SHORTCUTS_CUSTOM


def shortcutsDisconnect(self):
    self.translateButtonShortcut.activated.disconnect(self.translateButton)
    self.swapButtonShortcut.activated.disconnect(self.swapButton)
    self.copyButtonShortcut.activated.disconnect(self.copyButton)
    self.srcPronounceButtonShortcut.activated.disconnect(self.srcPronounceButton)
    self.destPronounceButtonShortcut.activated.disconnect(self.destPronounceButton)


def globalShortcutsLoader(self):
    combination = SHORTCUTS_CUSTOM.get("globaltranslateButton",SHORTCUTS_DEFAULT.get("globalTranslateButton")).split('+')
    for i,key in enumerate(combination): #convert keys to match HotKey.parse() method
        if key in ['Ctrl', 'Alt', 'Shift', 'Space']:
            combination[i] = f'<{key.lower()}>'      
        if key == 'Return': combination[i] = '<enter>'

    self.hotkey = keyboard.HotKey(
        keyboard.HotKey.parse('+'.join(combination)),
        self.globalTranslate) #self.globalTranslate() is in main.py 
    
    listener = keyboard.Listener(
            on_press=self.hotkey.press,
            on_release=self.hotkey.release)
    listener.start()


def shortcutsLoader(self): #load shortcuts from dictionary which previously loaded values from .conf file
    globalShortcutsLoader(self)
    
    self.translateButtonShortcut = QShortcut(QKeySequence(SHORTCUTS_CUSTOM.get("translateButton",SHORTCUTS_DEFAULT.get("translateButton"))), self)
    self.translateButtonShortcut.activated.connect(self.translateButton)
    self.swapButtonShortcut = QShortcut(QKeySequence(SHORTCUTS_CUSTOM.get("swapButton", SHORTCUTS_DEFAULT.get("swapButton"))), self)
    self.swapButtonShortcut.activated.connect(self.swapButton)
    self.copyButtonShortcut = QShortcut(QKeySequence(SHORTCUTS_CUSTOM.get("copyButton", SHORTCUTS_DEFAULT.get("copyButton"))), self)
    self.copyButtonShortcut.activated.connect(self.copyButton)
    self.srcPronounceButtonShortcut = QShortcut(QKeySequence(SHORTCUTS_CUSTOM.get("srcPronounceButton", SHORTCUTS_DEFAULT.get("srcPronounceButton"))), self)
    self.srcPronounceButtonShortcut.activated.connect(self.srcPronounceButton)
    self.destPronounceButtonShortcut = QShortcut(QKeySequence(SHORTCUTS_CUSTOM.get("destPronounceButton", SHORTCUTS_DEFAULT.get("destPronounceButton"))), self)
    self.destPronounceButtonShortcut.activated.connect(self.destPronounceButton)


def shortcutsDefaultLoader(self): #default shortcuts connections
    globalShortcutsLoader(self)

    self.translateButtonShortcut = QShortcut(QKeySequence(SHORTCUTS_DEFAULT.get("translateButton")), self)
    self.translateButtonShortcut.activated.connect(self.translateButton)
    self.swapButtonShortcut = QShortcut(QKeySequence(SHORTCUTS_DEFAULT.get("swapButton")), self)
    self.swapButtonShortcut.activated.connect(self.swapButton)
    self.copyButtonShortcut = QShortcut(QKeySequence(SHORTCUTS_DEFAULT.get("copyButton")), self)
    self.copyButtonShortcut.activated.connect(self.copyButton)
    self.srcPronounceButtonShortcut = QShortcut(QKeySequence(SHORTCUTS_DEFAULT.get("srcPronounceButton")), self)
    self.srcPronounceButtonShortcut.activated.connect(self.srcPronounceButton)
    self.destPronounceButtonShortcut = QShortcut(QKeySequence(SHORTCUTS_DEFAULT.get("destPronounceButton")), self)
    self.destPronounceButtonShortcut.activated.connect(self.destPronounceButton)






