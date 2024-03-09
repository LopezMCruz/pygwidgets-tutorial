import pygame, sys, pygwidgets

# Constants-------------------------------------------#
WIDTH, HEIGHT = (640,480)

BUTTON_X, BUTTON_Y = (100,100)

# Setup Pygame window---------------------------------#
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Multiple Buttons Tutorial')
mainClock = pygame.time.Clock()

button1 = pygwidgets.TextButton(window, (BUTTON_X, BUTTON_Y), "Button 1")
button2 = pygwidgets.TextButton(window,(BUTTON_X,BUTTON_Y), "Button 2")

button2.setLoc((100,50))

def main_menu():
    while True:
        
        window.fill((255,255,255)) 
       
        ''' inside our while loop, we have a for loop
            to handle events. An even can be a mouseclick,
            keyboard press, or the position of the mouse.'''
        for event in pygame.event.get():
            ''' this event handles when the (X) on the window is clicked.
                This even allows the game to exit gracefully'''
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            '''inside this for loop, we handle events for our buttons.
                we use pygwidgets handleEvent() functions'''
                
            if button1.handleEvent(event):
                print('Button 1 was pressed!!')

            if button2.handleEvent(event):
                print('Button 2 was pressed!!')

            ''' Whent the above buttons are pressed,
            the code in thier code blocks is executed.
            for this example a simple message is passed to the console,
            but you could also execute a function.'''
            
        button1.draw()
        button2.draw()
        
        pygame.display.update()
        mainClock.tick(60)

main_menu()