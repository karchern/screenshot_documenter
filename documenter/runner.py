from documenter.coordinates import BoxCoordinates
from documenter.listeners import Listener
from documenter.grab_screenshot import get_screenshot_from_screen
import logging

class Runner:
    def __init__(self):
        self.listener = None
        self.screenshots = []

    
    def run(self):
        # TODO: See if there is a better way to do this than a while True loop...
        while True:
        # Instantiate listener if not already
            if not self.listener:
                logging.info('Instantiating listener')
                self.listener = Listener()
            
            if isinstance(self.listener.mouse_coordinates, BoxCoordinates) and self.listener:
                logging.info('Coordinates received, taking screenshot')
                screenshot = get_screenshot_from_screen(self.listener.mouse_coordinates)
                self.screenshots.append(screenshot)
                self.listener = None
            if len(self.screenshots) == 2:
                break
        for screenshot in self.screenshots:
            screenshot.show()

            




    

