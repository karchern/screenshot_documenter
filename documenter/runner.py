from documenter.coordinates import BoxCoordinates
from documenter.listeners import Listener
from documenter.grab_screenshot import get_screenshot_from_screen
import logging
import io

class Runner:
    def __init__(self):
        self.screenshot_listener = Listener()
        self.screenshot_listener.overwrite_listener_and_start('keyboard_listener', self.screenshot_listener.instantiate_keyboard_listener)
        self.exit = False
        self.screenshots = []
        logging.critical('Runner initialized, ready to take input...')

    def get_output_file(self):
        import tkinter as tk
        from tkinter.filedialog import asksaveasfile        
        root = tk.Tk()
        root.withdraw()
        file = asksaveasfile(mode='w', defaultextension=".txt")
        return file

    def save_screenshots_as_powerpoint(self, output_file_path):

        from pptx import Presentation 
        from pptx.util import Inches

        if not output_file_path.endswith('.pptx'):
            output_file_path = output_file_path.split('.')[:-1]
            output_file_path += '.pptx'
        prs = Presentation() 
        blank_slide_layout = prs.slide_layouts[6] 
        left = top = Inches(0)        
        for screenshot in self.screenshots:
            slide_height = 7.5
            slide_width = 10            
            aspect_ratio = screenshot.size[0] / screenshot.size[1]
            if aspect_ratio > 1.25:
                slide_height = 10 / aspect_ratio
            else:
                slide_width = 7.5 * aspect_ratio

            slide = prs.slides.add_slide(blank_slide_layout)
            with io.BytesIO() as output:
                screenshot.save(output, format='PNG')       
                pic = slide.shapes.add_picture(output, left, top, height=Inches(slide_height), width=Inches(slide_width))
        prs.save(output_file_path)
        return 

    def run(self):
        while True:
            if isinstance(self.screenshot_listener.mouse_coordinates, BoxCoordinates):
                logging.info('Rectangle coordinates received, taking screenshot...')
                screenshot = get_screenshot_from_screen(self.screenshot_listener.mouse_coordinates)
                self.screenshots.append(screenshot)
                self.screenshot_listener.__init__()
                self.screenshot_listener.overwrite_listener_and_start('keyboard_listener', self.screenshot_listener.instantiate_keyboard_listener)
            if self.screenshot_listener.exit:
                break
        output_file = self.get_output_file()
        self.save_screenshots_as_powerpoint(output_file.name)

            




    

