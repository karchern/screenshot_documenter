from pynput import mouse, keyboard
from documenter.coordinates import BoxCoordinates
import logging

class Listeners:
    def __init__(self):
        #self.mouse_listener_terminator = self.instantiate_terminator_mouse_listener()
        #self.keyboard_listener = self.instantiate_keyboard_listener_screenshot()
        #self.shortcut_start = {"Key.cmd" : False, "Key.shift" : False, "Key.alt" : False, "4" : False}
        self.shortcut_start = {"Key.cmd" : False, "Key.shift" : False}
        self.mouse_coordinates = dict()
        #self.mouse_listener_terminator.start()
        #self.keyboard_listener.start()
    
    def add_listener_and_start(self, listener_name, inst_method):
        setattr(self, listener_name, inst_method())
        getattr(self, listener_name).start()


    def finish_logging_coordinates(self):
        self.mouse_coordinates['x2'], self.mouse_coordinates['y2'] = [round(pos) for pos in mouse.Controller().position]


    def get_bounding_box_on_click(self ,x ,y , button, pressed):
        if all(self.shortcut_start.values()):
            logging.info("keyboard shortcut pressed and mouse clicked, taking screenshot and killing all listeners")
            self.finish_logging_coordinates()
            self.mouse_coordinates = BoxCoordinates(
                x1 = self.mouse_coordinates['x1'],
                x2 = self.mouse_coordinates['x2'],
                y1 = self.mouse_coordinates['y1'],
                y2 = self.mouse_coordinates['y2']   
                )     
            self.keyboard_listener.stop()
            self.mouse_listener_terminator.stop()

    def get_bounding_box_on_press(self, key):
        try:
            self.shortcut_start[key.char] = True
        except AttributeError:
            self.shortcut_start[str(key)] = True
        if all(self.shortcut_start.values()):
            # Start logging coordinates
            self.mouse_coordinates['x1'], self.mouse_coordinates['y1'] = [round(pos) for pos in mouse.Controller().position]

    def instantiate_terminator_mouse_listener(self):
        return(mouse.Listener(
            on_click = self.get_bounding_box_on_click
        ))

    def instantiate_keyboard_listener_screenshot(self):
        return(keyboard.Listener(
            on_press = self.get_bounding_box_on_press
            # on_release = self.on_release
        ))
