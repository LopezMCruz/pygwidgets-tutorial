import pygame
import pygwidgets 
import pyghelpers

X_COORDINATE, Y_COORDINATE = (0,0)

class SceneOne(pyghelpers.Scene):
    
    def __init__(self, window) -> None:
        self.window = window
        self.back_ground_color = (161, 59, 113)
        
        ''' We can create widget and center it on the page'''
        self.title = pygwidgets.DisplayText(self.window, (25, 25), 'This is Page One ',
                                     fontSize=48, textColor=(255,255,255), width=610, justified='center')
        ''' buttons are defined in the manner of previous example, with 'self' as the prefix'''
        self.button1 = pygwidgets.TextButton(self.window, (X_COORDINATE, Y_COORDINATE), "Page 2" )
        self.button2 = pygwidgets.TextButton(self.window, (X_COORDINATE, Y_COORDINATE + 50), "Page 3" )
    
    '''pyghelpers handles the main loop for you 
        so you only need to write the for loop with event listeners'''    
    def handleInputs(self, event_list, key_pressed_list):
        for event in event_list:
            if self.button1.handleEvent(event):
                self.goToScene('scene 2')
                print('Button 1 pressed!')
            if self.button2.handleEvent(event):
                self.goToScene('scene 3')
                print('button 2 pressed!')
    
    ''' all the components you want to draw are in the draw function'''
    def draw(self):
        self.window.fill(self.back_ground_color)
        self.title.draw()
        self.button1.draw()
        self.button2.draw()           

