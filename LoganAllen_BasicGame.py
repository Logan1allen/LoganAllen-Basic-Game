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
#class Coin(simpleGE.Sprite):
              
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("frogBaby.png")
        self.beardMan = beardMan(self)
        self.sprites = [self.beardMan]
        
        
def main():
    game = Game()
    game.start()
    
    
if __name__ == "__main__":
    main()