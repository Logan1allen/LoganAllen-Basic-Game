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

class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)
        
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time Left: 10"
        self.center = (500, 30)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("frogBaby.png")
        self.sndstrawberry = simpleGE.Sound("coinsound.MP3")
        self.numstrawberrys = 10
        self.score = 0
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.lblTime = LblTime()
        
        self.lblScore = LblScore()
        
        self.beardMan = beardMan(self)
        self.strawberrys = []
        for i in range(self.numstrawberrys):
            self.strawberrys.append(strawberry(self))
        
        self.sprites = [self.beardMan,
                        self.strawberrys,
                        self.lblScore,
                        self.lblTime]
        
    def process(self):
        for strawberry in self.strawberrys:
            if strawberry.collidesWith(self.beardMan):
                strawberry.reset()
                self.sndstrawberry.play()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
                
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()
            
class Instructions(simpleGE.Scene):
    def __init__(self, prevScore):
        super().__init__()
        
        self.prevScore = prevScore

        self.setImage("frogBaby.png")
        self.response = "Quit"
        
        self.directions = simpleGE.MultiLabel()
        self.directions.textLines = [
        "You are BeardMan",
        "Move with the Left and Right arrow Keys",
        "Catch as much Strawberry Milk as you can",
        "You only have 10 Seconds"
            ]
        self.directions.center= (320, 240)
        self.directions.size = (500, 250)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100,400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (540,400)
        
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Last Score: 0"
        self.lblScore.center = (320, 400)
        self.lblScore.text = f"Last Score: {self.prevScore}"
        
        self.sprites = [self.directions,
                        self.btnPlay,
                        self.btnQuit,
                        self.lblScore]
        
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
                
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
        
def main():
    keepGoing = True
    lastScore = 0
    
    while keepGoing:
        instructions = Instructions(lastScore)
        instructions.start()
        
        if instructions.response == "Play":
            game = Game()
            game.start()
            lastScore = game.score
        else:
            keepGoing = False
    
    
if __name__ == "__main__":
    main()