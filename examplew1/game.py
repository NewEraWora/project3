from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import DirectFrame, DirectButton
from panda3d.core import CollisionSphere, CollisionNode, CollisionTraverser, CollisionHandlerQueue, BitMask32
from direct.interval.IntervalGlobal import Sequence, Func
from map import Map
from hero import Hero
import sys
from panda3d.core import WindowProperties






class Item():
    def __init__(self, pos, model):
        self.model = model
        self.model.setPos(pos)
        self.model.reparentTo(render)
        self.model.setScale(0.025)
        self.model.setZ(1)










class MyGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.settingsVisible = False
        self.land = Map()
        x,y = self.land.loadLand("land.txt")
        self.hero = Hero((x//2, y//2, 1), self.land)

        base.camLens.setFov(90)
        base.setBackgroundColor(0.2, 0.4, 0.6)
        # create frame for menu 
        self.menuFrame = DirectFrame(frameColor=(0, 0, 0, 0.5), frameSize=(-0.5, 0.5, -0.5, 0.5))
        self.menuFrame.setPos(0, 0, -0.1)
        
        self.againButton = DirectButton(text="Again", scale=0.1, command=self.resetGame)
        self.againButton.setPos(1.2, 0, 0.8)
        
        
        
        # create button "Resume Game"
        self.resumeButton = DirectButton(parent=self.menuFrame, text="Resume Game", scale=0.1, command=self.resumeGame)
        self.resumeButton.setPos(0, 0, 0.2)

        # create button "Exit Game"
        self.exitButton = DirectButton(parent=self.menuFrame, text="Exit Game", scale=0.1, command=self.exitGame)
        self.exitButton.setPos(0, 0, -0.2)

        # button Settings
        self.settingsButton = DirectButton(parent=self.menuFrame, text="Settings", scale=0.1, command=self.showSettings)
        self.settingsButton.setPos(0, 0, 0)  # centered

        # create frame for buttons resolution
        self.resolutionFrame = DirectFrame(parent=self.menuFrame, frameColor=(0, 0, 0, 0.5), frameSize=(-0.5, 0.5, -0.5, 0.5))
        self.resolutionFrame.setPos(0, 0, -0.1)
        self.resolutionFrame.hide()

        # create buttons for swap resolution
        self.resolutionButton1 = DirectButton(parent=self.resolutionFrame, text="800x600", scale=0.1, command=self.changeResolution, extraArgs=[800, 600])
        self.resolutionButton1.setPos(0, 0, 0.2)
        self.resolutionButton1.hide()

        self.resolutionButton2 = DirectButton(parent=self.resolutionFrame, text="1260x1080", scale=0.1, command=self.changeResolution, extraArgs=[1260, 1080])
        self.resolutionButton2.setPos(0, 0, 0)
        self.resolutionButton2.hide()

        self.resolutionButton3 = DirectButton(parent=self.resolutionFrame, text="1920x1080", scale=0.1, command=self.changeResolution, extraArgs=[1920, 1080])
        self.resolutionButton3.setPos(0, 0, -0.2)
        self.resolutionButton3.hide()

        # button "close" 
        self.closeButton = DirectButton(parent=self.resolutionFrame, text="Close", scale=0.1, command=self.hideResolution)
        self.closeButton.setPos(0, 0, -0.4)
        self.closeButton.hide()

        # initially hide menu
        self.menuFrame.hide()

        # download buttons for show menu
        self.menuButton = DirectButton(text="Menu", scale=0.1, command=self.toggleMenu)
        self.menuButton.setPos(-1.2, 0, 0.8)

    
        
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def resetGame(self):
        # Сбросить позицию персонажа к начальной
        self.hero.resetPosition()
        # Другие действия по сбросу игры
    
    
    def toggleMenu(self):
        # show or hide menu
        if self.menuFrame.isHidden():
            self.menuFrame.show()
        else:
            self.menuFrame.hide()

    def resumeGame(self):
        # hide menu and resume game
        self.menuFrame.hide()

    def exitGame(self):
        # finish app
        sys.exit(0)

        

    def showSettings(self):
        # Изменяем состояние переменной settingsVisible
        self.settingsVisible = not self.settingsVisible

        # Показываем или скрываем меню настроек в зависимости от settingsVisible
        if self.settingsVisible:
            self.resolutionFrame.show()
            self.resolutionButton1.show()
            self.resolutionButton2.show()
            self.resolutionButton3.show()
            self.closeButton.show()
        else:
            self.resolutionFrame.hide()
            self.resolutionButton1.hide()
            self.resolutionButton2.hide()
            self.resolutionButton3.hide()
            self.closeButton.hide()

        

    def hideResolution(self):
        # hide windows swap resolution
        self.resolutionFrame.hide()
        self.closeButton.hide()

    def changeResolution(self, width, height):    
        # Создаем объект WindowProperties и устанавливаем новые параметры разрешения
        wp = WindowProperties()
        wp.setSize(width, height)
        wp.setFullscreen(base.win.getProperties().getFullscreen())

    # Применяем новые параметры к окну
        base.win.requestProperties(wp)
        
        

        
        
        
        
game = MyGame()
game.run()

        
        
        
        
        
    

