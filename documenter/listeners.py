from pynput import mouse, keyboard
from documenter.coordinates import BoxCoordinates
import logging

class Listener:
    def __init__(self):
        self.mouse_listener_terminator = self.instantiate_terminator_mouse_listener()
        self.keyboard_listener = self.instantiate_keyboard_listener_screenshot()
        #self.shortcut_start = {"Key.cmd" : False, "Key.shift" : False, "Key.alt" : False, "4" : False}
        self.shortcut_start = {"Key.cmd" : False, "Key.shift" : False}
        self.mouse_coordinates = dict()
        self.mouse_listener_terminator.start()
        self.keyboard_listener.start()
    
    # def on_click(self):
    #     logging.info('{0} at {1}'.format(
    #         'Pressed' if pressed else 'Released',
    #         (x, y)))
    #     if pressed:
    #         # Start logging coordinates
    #         self.mouse_coordinates['x1'] = x
    #         self.mouse_coordinates['y1'] = y
    #     if not pressed:
    #         # Finish logging coordinates
    #         self.mouse_coordinates['x2'] = x
    #         self.mouse_coordinates['y2'] = y
    #         # 

    #         self.mouse_coordinates = BoxCoordinatessl
    #             x1 = self.mouse_coordinates['x1'],
    #             x2 = self.mouse_coordinates['x2'],
    #             y1 = self.mouse_coordinates['y1'],
    #             y2 = self.mouse_coordinates['y2']

    #         )
    #         # Stop listener
    #         return False    

    def finish_logging_coordinates(self):
        self.mouse_coordinates['x2'], self.mouse_coordinates['y2'] = [round(pos) for pos in mouse.Controller().position]


    def on_click(self ,x ,y , button, pressed):
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

    def on_press(self, key):
        try:
            self.shortcut_start[key.char] = True
        except AttributeError:
            self.shortcut_start[str(key)] = True
        if all(self.shortcut_start.values()):
            # Start logging coordinates
            self.mouse_coordinates['x1'], self.mouse_coordinates['y1'] = [round(pos) for pos in mouse.Controller().position]

    # def on_release(self, key):
    #     print('{0} released'.format(
    #         key))
    #     if key == keyboard.Key.esc:
    #         # Stop listener
    #         return False

    def instantiate_terminator_mouse_listener(self):
        return(mouse.Listener(
            on_click = self.on_click
        ))

    def instantiate_keyboard_listener_screenshot(self):
        return(keyboard.Listener(
            on_press = self.on_press
            # on_release = self.on_release
        ))