import unittest

import matplotlib.pyplot as plt
import numpy as np

from pyrecorder.recorders.streamer import Streamer
from pyrecorder.video import Video


class LiveTest(unittest.TestCase):


    def test_stream_simple(self):
        vid = Video(Streamer(mode="stream", delay=1000, close_window=True))

        for k in range(3):
            X = np.random.random((100, 2))
            plt.scatter(X[:, 0], X[:, 1])
            vid.record()

        vid.close()


if __name__ == '__main__':
    unittest.main()
