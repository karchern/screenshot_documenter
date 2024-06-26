from documenter.coordinates import BoxCoordinates
import tempfile
from subprocess import run
import logging
from PIL import Image
import tkinter as tk
from tkinter.filedialog import asksaveasfile

from pptx import Presentation 
from pptx.util import Inches


def get_screenshot_from_screen(bounding_box: BoxCoordinates = None):
    if not bounding_box:
        raise ValueError('Bounding box must be provided')
    tmp_file = tempfile.NamedTemporaryFile(suffix=".png")
    run(["screencapture", "-R", bounding_box.to_screencapture_string(), tmp_file.name])
    im = Image.open(tmp_file.name)
    return(im)
    
    