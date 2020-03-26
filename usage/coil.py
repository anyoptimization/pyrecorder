import matplotlib.pyplot as plt
import numpy as np

from pyrecorder.recorders.file import File
from pyrecorder.video import Video

plt.style.use('dark_background')

with Video(File("coil.mp4", fps=15)) as vid:
    for t in range(500):
        a = np.arange(t) * 0.1
        plt.plot(a * np.sin(a), a * np.cos(a))
        plt.xlim(-50, 50)
        plt.ylim(-50, 50)
        plt.axis('off')
        vid.record()

