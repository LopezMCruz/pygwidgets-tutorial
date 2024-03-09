import pygame, sys, pygwidgets

# Constants-------------------------------------------#
WIDTH, HEIGHT = (640,480)

''' coordinates are set to (0,0) which maps the button to the 
    top left of the window'''
BUTTON_X, BUTTON_Y = (0,0)

# Setup Pygame window---------------------------------#
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Buttons Tutorial')
mainClock = pygame.time.Clock()

'''In Pygwidgets we define a button1 by passing a window object, as well as the x and y coordinates.
    All three we predefined above. We also pass the text we want displayed on the button
    for this example we've defined it as 'Button 1' '''
button1 = pygwidgets.TextButton(window, (BUTTON_X, BUTTON_Y), "Button 1")

def main_menu():
    while True:
        
        window.fill((255,255,255)) 
       
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ''' The button will need to be drawn for every frame,
            We can do this by calling the button we defined above.
            because the button we defined is now and instance of the Textbutton
            class (see pygwidget documentation for more info), we can utilize the
            pygwidget draw() function to draw the button for us.'''
        
        button1.draw()
        
        pygame.display.update()
        mainClock.tick(60)

main_menu()