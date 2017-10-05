from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
    name = "integrator_package",
    author = "Jonas Kruger Svensson",
    ext_modules=cythonize("*.pyx"),
)
