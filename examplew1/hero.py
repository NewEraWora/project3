from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import DirectFrame, DirectButton











key_switch_camera = "c"
key_forward = "w"
key_backward = "s"
key_left = "a"
key_right = "d"
key_up = "space"
key_down = "shift"

key_turn_left = "q"
key_turn_right = "e"
key_change_mode = 'z'

class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.mode = True
        self.hero = loader.loadModel('smiley')
        self.start_pos = pos
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
    
    
    def resetPosition(self):
        self.hero.setPos(self.start_pos)
    
    
    
    
    
    
    
        
    def collectItem(self):
        for item in items:
            if self.hero.getDistance(item.model) < 1 and not item.collected:
                item.collect()
                self.collected_items += 1  # Увеличить счетчик собранных предметов
                  
    def checkLevelCompletion(self):
        
        if self.collected_items >= len(items):
            self.showWinMessage()              
    
    def checkCollision(self):
        # Проверка на столкновение с ключом
        for key in self.keys:
            if self.hero.getDistance(key.model) < 1:  # Расстояние для соприкосновения
                key.model.removeNode()  # Удалить модель ключа из сцены
                self.keys.remove(key)  # Удалить ключ из списка
    
    
    
    
    
    
    
    
    
    def fOrward(self):
        
        self.collectItem()
        # Проверить сбор предметов при движении
        angle = self.hero.getH() % 360
        self.move_to(angle)
        self.checkLevelCompletion()  # Проверить завершение уровня после перемещения

        
        
    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def accept_events(self):
        # ? TURN LEFT RIGHT
        base.accept(key_turn_left, self.turn_left)
        base.accept(key_turn_left+'-repeat', self.turn_left)
        base.accept(key_turn_right, self.turn_right)
        base.accept(key_turn_right+'-repeat', self.turn_right)
        # ? W,S,A,D
        base.accept(key_forward, self.forward)
        base.accept(key_forward+'-repeat', self.forward)
        base.accept(key_backward, self.backward)
        base.accept(key_backward+'-repeat', self.backward)
        base.accept(key_left, self.left)
        base.accept(key_left+'-repeat', self.left)
        base.accept(key_right, self.right)
        base.accept(key_right+'-repeat', self.right)
        # ? UP DOWN
        base.accept(key_up, self.up)
        base.accept(key_up+'-repeat', self.up)
        base.accept(key_down, self.down)
        base.accept(key_down+'-repeat', self.down)
        # ? ADDITIONAL OPTIONS
        base.accept(key_change_mode, self.change_mode)
        base.accept(key_switch_camera, self.changeView)
        

    
    
    
    
    
    
    
    
    
    
    def turn_left(self):
        self.hero.setH((self.hero.getH()+5) % 360)

    def turn_right(self):
        self.hero.setH((self.hero.getH()-5) % 360)

    def forward(self):
        angle = self.hero.getH() % 360
        self.move_to(angle)
        

    def backward(self):
        angle = (self.hero.getH()+180) % 360
        self.move_to(angle)
        

    def left(self):
        angle = (self.hero.getH()+90) % 360
        self.move_to(angle)
        

    def right(self):
        angle = (self.hero.getH()+270) % 360
        self.move_to(angle)
        

    def up(self):
        if self.mode:
            self.hero.setZ(self.hero.getZ()+1)

    def down(self):
        if self.mode and self.hero.getZ() > 1:
            self.hero.setZ(self.hero.getZ()-0.1)

    def change_mode(self):
        if self.mode:
            self.mode = False
        else:
            self.mode = True

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

   
    
    
    
    
    
    
    
    
    def try_move(self, angle):
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findHigestEmpty(pos)
            self.hero.setPos(pos)
            
        else:
            pos = pos[0], pos[1], pos[2]+1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)
                
        
        
        
        
 
        
        
        
        
        
        
    def look_at(self, angle):
        x_from = round(self.hero.getX())
        y_from = round(self.hero.getY())
        z_from = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dy
        return x_to, y_to, z_from

    def check_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return (0, -1)
        elif angle <= 65:
            return (1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return (-1, 1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return (0, -1)
    
    