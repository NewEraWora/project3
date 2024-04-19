from random import randint

class Map():
    def __init__(self):
        self.model = 'block'
        self.base_texture = 'block.jpg'
        self.special_texture = 'winn.jpg'
        self.path_color = (1, 1, 1, 1)  # Цвет проходов
        self.startNew()
        
    def startNew(self):
        self.land = render.attachNewNode("Land")
        
    def getColor(self, is_wall):
        return self.wall_color if is_wall else self.path_color
    
    def clear(self):
        self.land.removeNode()
        self.startNew()
        
    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(" ")
                for z in line:
                    for z0 in range(int(z)+1):
                        block = loader.loadModel(self.model)
                        block.setTexture(loader.loadTexture(self.base_texture))  # Используем базовую текстуру для всех блоков
                        block.setPos((x, y, z0))
                        
                        # Если это специальный блок (например, с координатами x=5, y=0, z=0), устанавливаем специальную текстуру
                        if (x, y, z0) == (27, 5, 1):
                            block.setTexture(loader.loadTexture(self.special_texture))
                        
                        color = self.getColor(False)  # Проходы имеют другой цвет
                        block.setColor(color)
                        block.setTag("at", str((x, y, z0)))
                        block.reparentTo(self.land)
                    x += 1
                y += 1 
        return x, y