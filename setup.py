import setuptools
from setuptools import setup

from pyrecorder.version import __version__

# ---------------------------------------------------------------------------------------------------------
# GENERAL
# ---------------------------------------------------------------------------------------------------------


__name__ = "pyrecorder"
__author__ = "Julian Blank"
__url__ = "https://www.egr.msu.edu/coinlab/blankjul/pyrecorder/"

data = dict(
    name=__name__,
    version=__version__,
    author=__author__,
    url=__url__,
    python_requires='>=3.6',
    author_email="blankjul@egr.msu.edu",
    description="Video Recording made easy - The tool you need for animations using Matplotlib, Plotly and other "
                "plotting libraries. ",
    license='Apache License 2.0',
    keywords="video,recording,matplotlib,plotly",
    install_requires=['numpy>=1.15', 'opencv-python>=4.0.0.21', 'matplotlib>=3', 'Pillow'],
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Multimedia :: Video'
    ]
)


# ---------------------------------------------------------------------------------------------------------
# OTHER METADATA
# ---------------------------------------------------------------------------------------------------------


# update the readme.rst to be part of setup
def readme():
    with open('README.rst') as f:
        return f.read()


def packages():
    return ["pyrecorder"] + ["pyrecorder." + e for e in setuptools.find_packages(where='pyrecorder')]


data['long_description'] = readme()
data['packages'] = packages()

# ---------------------------------------------------------------------------------------------------------
# SETUP
# ---------------------------------------------------------------------------------------------------------

setup(**data)
