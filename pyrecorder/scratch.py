import matplotlib.pyplot as plt
import numpy as np

from pyrecorder.converters.matplotlib import Matplotlib
from pyrecorder.recorder import Recorder
from pyrecorder.writers.gif import GIF

# initialize the converter which is creates an image when `record()` is called
converter = Matplotlib(dpi=120)

writer = GIF("github.gif")

rec = Recorder(writer, converter=converter)

for t in range(10):

    # let us create a local figure object with two sub figures
    fig, (ax1, ax2) = plt.subplots(2, figsize=(3, 4))

    X = np.random.random((100, 2))
    ax1.scatter(X[:, 0], X[:, 1], color="green")

    X = np.random.random((100, 2))
    ax2.scatter(X[:, 0], X[:, 1], color="red")

    # fix the size of figure and legends
    fig.tight_layout()

    # take a snapshot the specific figure object with the recorder
    rec.record(fig=fig)


rec.close()