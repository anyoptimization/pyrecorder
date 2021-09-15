import matplotlib.pyplot as plt
import numpy as np

from pyrecorder.converters.matplotlib import Matplotlib
from pyrecorder.recorder import Recorder
from pyrecorder.writers.gif import GIF

# initialize the converter which is creates an image when `record()` is called
converter = Matplotlib()

writer = GIF("medium2.gif", duration=0.5)

rec = Recorder(writer, converter=converter)

for t in range(50):

    # let us create a local figure object with two sub figures
    fig, (ax1, ax2) = plt.subplots(2, figsize=(3, 4))

    X = np.random.random((100, 2))
    ax1.scatter(X[:, 0], X[:, 1], color="green")

    X = np.random.random(5)
    ax2.pie(X)
    # ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # fix the size of figure and legends
    fig.tight_layout()

    # take a snapshot the specific figure object with the recorder
    rec.record(fig=fig)


rec.close()