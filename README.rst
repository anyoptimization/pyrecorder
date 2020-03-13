pyrecorder
====================================================================

You can find the detailed documentation here: https://www.egr.msu.edu/coinlab/blankjul/pyrecorder/


|travis| |python| |license|


.. |travis| image:: https://travis-ci.com/julesy89/pyrecorder.svg?branch=master
   :alt: build status
   :target: https://travis-ci.com/julesy/pyrecorder

.. |python| image:: https://img.shields.io/badge/python-3.6-blue.svg
   :alt: python 3.6

.. |license| image:: https://img.shields.io/badge/license-apache-orange.svg
   :alt: license apache
   :target: https://www.apache.org/licenses/LICENSE-2.0



Installation
============

The framework is available at the PyPi Repository:

.. code-block:: bash

    pip install -U pyrecorder


Usage
=====

It's as simple as it can be. Initialize an `Video` object with a `Recorder` and record the current
plots be calling `record()`. Finally, close the video object with `close()` and you are good to go
and watch your video.

.. code-block:: bash

    import numpy as np
    import matplotlib.pyplot as plt

    from pyrecorder.video import Video
    from pyrecorder.recorders.file import File

    fname = "example.mp4"
    vid = Video(File(fname))

    for k in range(10):
        X = np.random.random((100, 2))
        plt.scatter(X[:, 0], X[:, 1])
        vid.record()

    vid.close()



Contact
=======


Feel free to contact me if you have any question:

::

    Julian Blank (blankjul [at] egr.msu.edu)
    Michigan State University
    Computational Optimization and Innovation Laboratory (COIN)
    East Lansing, MI 48824, USA


