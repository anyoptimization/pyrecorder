import matplotlib.pyplot as plt
import numpy as np

from pyrecorder.recorders.gif import GIF
from pyrecorder.video import Video

with Video(GIF("test.gif")) as vid:
    for t in range(2):
        X = np.random.random((100, 2))
        plt.scatter(X[:, 0], X[:, 1], color="yellow")
        vid.record()
