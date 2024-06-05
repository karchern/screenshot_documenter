from documenter.coordinates import BoxCoordinates
from documenter.listeners import Listeners
from documenter.grab_screenshot import get_screenshot_from_screen
import logging
import tkinter as tk
from tkinter import simpledialog
from tkinter.filedialog import asksaveasfile


class Runner:
    def __init__(self):
        self.screenshot_listeners = None
        self.breakout_listener = Listeners()
        self.breakout_listener.add_listener_and_start('breakout_listener', self.breakout_listener.instantiate_breakout_listener)
        self.screenshots = []

    def get_output_file(self):
        root = tk.Tk()
        root.withdraw()
        file = asksaveasfile(mode='w', defaultextension=".txt")
        return file

    def run(self):
        while True:
        # Instantiate listener if not already/
            if not self.screenshot_listeners:
                logging.info('Instantiating listener')
                self.screenshot_listeners = Listeners()
                self.screenshot_listeners.add_listener_and_start('mouse_listener_terminator', self.screenshot_listeners.instantiate_terminator_mouse_listener)
                self.screenshot_listeners.add_listener_and_start('keyboard_listener', self.screenshot_listeners.instantiate_keyboard_listener_screenshot)
            
            if isinstance(self.screenshot_listeners.mouse_coordinates, BoxCoordinates) and self.screenshot_listeners:
                logging.info('Coordinates received, taking screenshot')
                screenshot = get_screenshot_from_screen(self.screenshot_listeners.mouse_coordinates)
                self.screenshots.append(screenshot)
                self.screenshot_listeners = None
            if not self.breakout_listener.breakout_listener.running:
                break
        output_file = self.get_output_file()
        for screenshot in self.screenshots:
            screenshot.show()

            




    

