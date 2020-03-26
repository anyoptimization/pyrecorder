import os
import unittest

import matplotlib.pyplot as plt
import numpy as np

from pyrecorder.recorders.file import File
from pyrecorder.recorders.gif import GIF
from pyrecorder.recorders.html import HTML
from pyrecorder.recorders.streamer import Streamer
from pyrecorder.video import Video


class SimpleVideoTest(unittest.TestCase):

    def test_record_simple(self):
        fname = "example.mp4"
        vid = Video(File(fname))

        for k in range(10):
            X = np.random.random((100, 2))
            plt.scatter(X[:, 0], X[:, 1])
            vid.record()

        vid.close()

        self.assertTrue(os.path.exists(fname))
        os.remove(fname)

    def test_gif_simple(self):
        fname = "example.gif"
        vid = Video(GIF(fname))

        for k in range(10):
            X = np.random.random((100, 2))
            plt.scatter(X[:, 0], X[:, 1])
            vid.record()

        vid.close()

        self.assertTrue(os.path.exists(fname))
        os.remove(fname)

    def test_html_wrap_simple(self):
        fname = "example.mp4"
        vid = Video(HTML(File(fname)))

        for k in range(10):
            X = np.random.random((100, 2))
            plt.scatter(X[:, 0], X[:, 1])
            vid.record()

        vid.close()

        self.assertTrue(os.path.exists(fname))

        html = fname.replace("mp4", "html")
        self.assertTrue(os.path.exists(html))
        os.remove(fname)
        os.remove(html)

    def test_html_embed_simple(self):
        fname = "example.mp4"
        vid = Video(HTML(File(fname), embedded=True))

        for k in range(10):
            X = np.random.random((100, 2))
            plt.scatter(X[:, 0], X[:, 1])
            vid.record()
        vid.close()

        self.assertTrue(os.path.exists("example.html"))
        os.remove("example.html")

    def test_stream_simple(self):
        vid = Video(Streamer(mode="stream", delay=1000, close_window=True))

        for k in range(3):
            X = np.random.random((100, 2))
            plt.scatter(X[:, 0], X[:, 1])
            vid.record()

        vid.close()


if __name__ == '__main__':
    unittest.main()
