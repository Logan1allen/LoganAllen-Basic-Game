import pygame, simpleGE, random
pygame.init()

class beardMan(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("beardMan.png")
        self.setSize(50,50)
        self.position = (320,400)
        self.moveSpeed = 5
    
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
class strawberry(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("strawberry.png")
        self.setSize(50,50)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
              
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("frogBaby.png")
        self.sndstrawberry = simpleGE.Sound("coinsound.MP3")
        self.numstrawberrys = 10
        self.beardMan = beardMan(self)
        self.strawberrys = []
        for i in range(self.numstrawberrys):
            self.strawberrys.append(strawberry(self))
        
        self.sprites = [self.beardMan,
                        self.strawberrys]
        
    def process(self):
        for strawberry in self.strawberrys:
            
            if strawberry.collidesWith(self.beardMan):
                strawberry.reset()
                self.sndstrawberry.play()
            
        
        
def main():
    game = Game()
    game.start()
    
    
if __name__ == "__main__":
    main()