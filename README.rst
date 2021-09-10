|travis| |python| |license|


.. |travis| image:: https://travis-ci.com/julesy89/pyrecorder.svg?branch=master
   :alt: build status
   :target: https://travis-ci.com/julesy/pyrecorder

.. |python| image:: https://img.shields.io/badge/python-3.9-blue.svg
   :alt: python 3.6

.. |license| image:: https://img.shields.io/badge/license-apache-orange.svg
   :alt: license apache
   :target: https://www.apache.org/licenses/LICENSE-2.0


.. |logo| image:: https://github.com/anyoptimization/pyrecorder/blob/master/docs/source/_static/pyrecorder.png
  :target: https://anyoptimization.com/projects/pyrecorder/
  :alt: pyrecorder


.. |animation| image:: https://anyoptimization.com/projects/pyrecorder/_static/github.gif
  :target: https://anyoptimization.com/projects/pyrecorder/
  :alt: animation


|logo|



You can find the detailed documentation here:
https://anyoptimization.com/projects/pyrecorder/



Installation
============

The framework is available at the PyPi Repository:

.. code-block:: bash

    pip install -U pyrecorder


Usage
=====

It's as simple as it should be. Initialize a `Recorder` object with a `Writer` and store plots by calling `record()`.

.. code-block:: bash

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



|animation|


Contact
=======


Feel free to contact me if you have any question:

::

    Julian Blank (blankjul [at] egr.msu.edu)
    Michigan State University
    Computational Optimization and Innovation Laboratory (COIN)
    East Lansing, MI 48824, USA


