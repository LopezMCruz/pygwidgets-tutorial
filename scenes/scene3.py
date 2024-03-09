import pygame
import pygwidgets 
import pyghelpers

X_COORDINATE, Y_COORDINATE = (0,0)

class SceneThree(pyghelpers.Scene):
    def __init__ (self,window) -> None:
        self.window =window
        self.title = pygwidgets.DisplayText(self.window, (25, 25), 'This is Page Three ',
                                     fontSize=48, textColor=(255,255,255), width=610, justified='center')
        self.back_ground_color = (120,81,169)
        self.title.setText('This is Page Three')
        self.button1 = pygwidgets.TextButton(self.window, (X_COORDINATE+100, Y_COORDINATE+100), "Page 1" )
        self.button2 = pygwidgets.TextButton(self.window, (X_COORDINATE, Y_COORDINATE + 100), "Page 2" )
        
    def handleInputs(self, event_list, key_pressed_list):
        for event in event_list:
            if self.button1.handleEvent(event):
                self.goToScene('scene 1')
            if self.button2.handleEvent(event):
                self.goToScene('scene 2')

    def draw(self):
        self.window.fill(self.back_ground_color)
        self.title.draw()
        self.button1.draw()
        self.button2.draw()