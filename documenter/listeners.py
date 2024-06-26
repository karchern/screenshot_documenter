from pynput import mouse, keyboard
from documenter.coordinates import BoxCoordinates
import logging

class Listener:
    def __init__(self, reset_exit = True):
        self.shortcut = {"Key.cmd" : False, "Key.shift" : False}
        self.mouse_coordinates = dict()
        self.first_corner_logged = False
        self.exit = False

    def reset_listener_attributes(self, listener_name):
        setattr(self, listener_name, None)

    def overwrite_listener_and_start(self, listener_name, inst_method):
        setattr(self, listener_name, inst_method())
        getattr(self, listener_name).start()

    def finish_logging_coordinates(self):
        self.mouse_coordinates['x2'], self.mouse_coordinates['y2'] = [round(pos) for pos in mouse.Controller().position]

    # def breakout(self, key):
    #     if key == keyboard.Key.esc:
    #         logging.info('Escape pressed, exiting program...')
    #         return False

    def listen_to_press(self, key):
        if key == keyboard.Key.esc:
            logging.info('Escape pressed, exiting program...')
            self.exit = True
        try:
            self.shortcut[key.char] = True
        except AttributeError:
            self.shortcut[str(key)] = True
        if all(self.shortcut.values()) and not self.first_corner_logged:
            # Start logging coordinates
            self.mouse_coordinates['x1'], self.mouse_coordinates['y1'] = [round(pos) for pos in mouse.Controller().position]
            self.shortcut = dict((key, False) for key in self.shortcut.keys())
            self.first_corner_logged = True 
        if all(self.shortcut.values()) and self.first_corner_logged:
            self.finish_logging_coordinates()
            self.mouse_coordinates = BoxCoordinates(
                x1 = self.mouse_coordinates['x1'],
                x2 = self.mouse_coordinates['x2'],
                y1 = self.mouse_coordinates['y1'],
                y2 = self.mouse_coordinates['y2']   
                )     

            getattr(self, 'keyboard_listener').stop()

    def instantiate_keyboard_listener(self):
        return(keyboard.Listener(
            on_press = self.listen_to_press
            # on_release = self.on_release
        ))

    # def instantiate_breakout_listener(self):
    #     return(keyboard.Listener(
    #         on_press = self.breakout
    #     ))
