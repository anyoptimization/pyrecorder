import numpy as np
from matplotlib import pyplot as plt

from pyrecorder.recorders.file import File
from pyrecorder.video import Video

with Video(File("wave.mp4", fps=15)) as vid:

    for t in range(200):
        x = np.linspace(0, 4, 1000)
        y = np.sin(2 * np.pi * (x - 0.01 * t))
        plt.plot(x, y)

        vid.record()
