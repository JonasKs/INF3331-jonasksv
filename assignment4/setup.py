from setuptools import setup, find_packages
from Cython.Build import cythonize
import numpy

setup(
    name = "Assignment4",
    ext_modules=cythonize("assignment4/*.pyx"), #not needed if already compiled
    include_dirs=[numpy.get_include(), "."],
    packages = find_packages(),
)
