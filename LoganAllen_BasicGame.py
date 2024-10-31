import pygame, simpleGE, random
pygame.init()

class beardMan(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("beardMan.png")
        self.setSize(50,50)
              
#class Coin(simpleGE.Sprite):
              
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("frogBaby.png")
        self.beardMan = beardMan(self)
        
        
def main():
    game = Game()
    game.start()
    
    
if __name__ == "__main__":
    main()