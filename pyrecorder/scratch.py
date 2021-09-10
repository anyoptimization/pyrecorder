import matplotlib.pyplot as plt
import numpy as np

from pyrecorder.recorder import Recorder
from pyrecorder.writers.video import Video

# create a writer object (here, mp4)
writer = Video("video.mp4")

# use the with statement to close the recorder when done
with Recorder(writer) as rec:

    # record 10 different snapshots
    for t in range(10):

        # create the plot (here, using matplotlib)
        X = np.random.random((50, 2))
        plt.scatter(X[:, 0], X[:, 1], facecolor="none", edgecolor="red")

        # use the record to store the current plot
        rec.record()
