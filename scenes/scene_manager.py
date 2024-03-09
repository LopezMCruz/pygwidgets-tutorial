import pygame
import pyghelpers
from scene1 import SceneOne
from scene2 import SceneTwo
from scene3 import SceneThree

# 2 - Define constants
FRAMES_PER_SECOND = 30
WINDOW_WIDTH, WINDOW_HEIGHT = (640,480)

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Instantiate all scenes and store them in a dictionary (as of pyghelpers 1.1)
scenes_dict = {'scene 1': SceneOne(window), 
               'scene 2': SceneTwo(window),
               'scene 3': SceneThree(window)}

# Create the Scene Manager, passing in the scenes list, and the FPS
o_scene_manager = pyghelpers.SceneMgr(scenes_dict, FRAMES_PER_SECOND)

# Tell the Scene Manager to start running
o_scene_manager.run()