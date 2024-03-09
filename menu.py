# Setup Python ----------------------------------------------- #
import pygame, sys, pygwidgets


# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')

# Functions------------------------------------------------------#


class Menu():
    def __init__(self, window):
        self.window = window
        self.width,self.height = window.get_size()
        self.button1 = pygwidgets.TextButton(self.window, (100,100), "Button 1")
        self.button2 = pygwidgets.TextButton(self.window, (100,100), "Button 2")
        self.button3 = pygwidgets.TextButton(self.window, (100,100), "Return Main Menu")
        

    def settings(self, window):
        self.centerWidget(self.button1)
        running = True
        while running:
            window.fill((0,0,0))
    
           
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        
                if self.button1.handleEvent(event):
                    print("Button 1 was clicked!!")
                    
                if self.button2.handleEvent(event):
                    print("Button 2 was clicked!!")
                    
                if self.button3.handleEvent(event):
                    running = False
            
            self.button1.draw()
            self.button2.draw()
            self.button3.draw()
            
            pygame.display.update()
            mainClock.tick(60)

    def centerWidget(self, widget):
        centerX = (self.width - 100) / 2
        centerY = (self.height - 40) / 2
        widget.setLoc((centerX, centerY))