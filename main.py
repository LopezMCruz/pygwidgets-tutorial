import pygame, sys, pygwidgets
from menu import Menu  # Assuming your Menu class is in a file named menu.py

# Constants-------------------------------------------#
WIDTH, HEIGHT = (640,480)
BUTTON_WIDTH, BUTTON_HEIGHT = 100, 40


# Setup Pygame window---------------------------------#
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('game base')
mainClock = pygame.time.Clock()

font = pygame.font.SysFont(None, 20)

# Buttons --------------------------------------------#
settings_button = pygwidgets.TextButton(window,(100,100), "Settings")

# Menu Object-----------------------------------------#
menu = Menu(window)
# Special functions-----------------------------------#
# Function to center the widget
def centerWidget(widget):
    centerX = (WIDTH - BUTTON_WIDTH) / 2
    centerY = (HEIGHT - BUTTON_HEIGHT) / 2
    widget.setLoc((centerX, centerY))



def main_menu():
    # call to function to center the widget
    centerWidget(settings_button)
    click = False
    while True:
        window.fill((0,0,0))
       
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
            # navigation
            if settings_button.handleEvent(event):
                menu.settings(window)
            
            
        settings_button.draw()    
        pygame.display.update()
        mainClock.tick(60)

main_menu()
