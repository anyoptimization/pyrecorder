import cv2
import imageio
from PIL import Image

from pyrecorder.writer import Writer


class GIF(Writer):

    def __init__(self,
                 fname,
                 optimize=False,
                 duration=1,
                 loop=0
                 ):
        super().__init__()
        self.fname = fname
        self.buffer = []
        self.optimize = optimize
        self.duration = duration
        self.loop = loop

    def write(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        img = Image.fromarray(frame, 'RGB')
        self.buffer.append(img)

    def close(self):
        imageio.mimsave(self.fname, self.buffer, duration=self.duration, loop=self.loop)

