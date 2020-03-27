import cv2
from PIL import Image

from pyrecorder.recorder import Recorder


class GIF(Recorder):

    def __init__(self,
                 fname,
                 optimize=False,
                 duration=500,
                 loop=0
                 ):
        super().__init__()
        self.fname = fname
        self.frames = []
        self.optimize = optimize
        self.duration = duration
        self.loop = loop

    def do(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        img = Image.fromarray(frame, 'RGB')
        self.frames.append(img)

    def close(self):
        if len(self.frames) > 0:
            self.frames[0].save(self.fname,
                                save_all=True,
                                append_images=self.frames[1:],
                                optimize=self.optimize,
                                duration=self.duration,
                                loop=self.loop)

