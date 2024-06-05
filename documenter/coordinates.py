class BoxCoordinates:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def to_screencapture_string(self):
        return f"{round(self.x1)},{round(self.y1)},{round(self.x2 - self.x1)},{round(self.y2 - self.y1)}"