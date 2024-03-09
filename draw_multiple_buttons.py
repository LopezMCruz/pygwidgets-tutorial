import pygame, sys, pygwidgets

# Constants-------------------------------------------#
WIDTH, HEIGHT = (640,480)

BUTTON_X, BUTTON_Y = (100,100)

# Setup Pygame window---------------------------------#
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Multiple Buttons Tutorial')
mainClock = pygame.time.Clock()

button1 = pygwidgets.TextButton(window, (BUTTON_X, BUTTON_Y), "Button 1")

'''To draw multiple buttons we need to first define a second button'''
button2 = pygwidgets.TextButton(window,(BUTTON_X, BUTTON_Y), "Button 2")

'''Next we need to set a location by calling the setLocation() method from the pygwidget library,
    we also pass the x, and y values of the window to the function. Your button will be limited to
    the height and width we defined above on line 6.'''
button2.setLoc((100,50))

def main_menu():
    while True:
        
        window.fill((255,255,255)) 
       
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        button1.draw()
        
        '''don't forget to draw() your new button'''
        button2.draw()
        
        pygame.display.update()
        mainClock.tick(60)

main_menu()