import pygame, sys

# Constants-------------------------------------------#
WIDTH, HEIGHT = (640,480)

# Setup Pygame window---------------------------------#
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Main Window')
mainClock = pygame.time.Clock()

def main_menu():
    while True:
        window.fill((255,255,255)) 
       
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        mainClock.tick(60)

main_menu()
