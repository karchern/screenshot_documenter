from documenter.coordinates import BoxCoordinates
from documenter.listeners import Listeners
from documenter.grab_screenshot import get_screenshot_from_screen
import logging

class Runner:
    def __init__(self):
        self.listeners = None
        self.screenshots = []

    
    def run(self):
        # TODO: See if there is a better way to do this than a while True loop...
        while True:
        # Instantiate listener if not already
            if not self.listeners:
                logging.info('Instantiating listener')
                self.listeners = Listeners()
                self.listeners.add_listener_and_start('mouse_listener_terminator', self.listeners.instantiate_terminator_mouse_listener)
                self.listeners.add_listener_and_start('keyboard_listener', self.listeners.instantiate_keyboard_listener_screenshot)
            
            if isinstance(self.listeners.mouse_coordinates, BoxCoordinates) and self.listeners:
                logging.info('Coordinates received, taking screenshot')
                screenshot = get_screenshot_from_screen(self.listeners.mouse_coordinates)
                self.screenshots.append(screenshot)
                self.listeners = None
            if len(self.screenshots) == 2:
                break
        for screenshot in self.screenshots:
            screenshot.show()

            




    

