# LoganAllen Basic Game
 Basic Game for CS-120

Step 1 Add a game scene with a background Image
Step 2 Add basic character Sprite
Step 3 Add keyboard Motion to the character sprite
    
    import pygame, simpleGE, random
    initialize pygame
    
    make a subclass called beardMan with the parameters simpleGE.Sprite
        define an init
        super init
        set the image to beardMan.png
        set the size of the image to be 50 x 50
        set the position of the image to be (320,400)
        set the moveSpeed to 5
        
        
        define process with the self parameter
        use an if statement to look for if the left key is currently being pressed down
            self.x -= the movement speed
        use an if statement to look for if the right key is currently being pressed down
            self.y += the movement speed
    
    

    define a subclass called game with the parameters simpleGE.Scene
        initialize the class be defining the Initializer
        super init
        set the image to frogBaby.png
        make an instance of the beardMan class
        call the sprites self.beardMan
        
        