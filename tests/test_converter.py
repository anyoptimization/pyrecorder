import os
import unittest

import numpy as np
import plotly.express as px

from pyrecorder.converters.plotly import Plotly
from pyrecorder.recorders.file import File
from pyrecorder.video import Video


class SimpleConverterTest(unittest.TestCase):

    def test_record_simple(self):
        fname = "example.mp4"
        vid = Video(File(fname), converter=Plotly())

        df = px.data.iris()

        for k in range(10):
            rnd = np.random.rand(len(df)) < 0.7
            fig = px.scatter(df.loc[rnd], x="sepal_width", y="sepal_length", color="species", size='petal_length')
            vid.record(fig=fig)

        vid.close()

        self.assertTrue(os.path.exists(fname))
        os.remove(fname)



if __name__ == '__main__':
    unittest.main()
