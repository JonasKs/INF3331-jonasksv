from distutils.core import setup, find_packages
from Cython.Build import cythonize
import numpy

setup(
    name = "integrator_package",
    author = "Jonas Kruger Svensson",
    ext_modules=cythonize("*.pyx"),
    packages=find_packages(),
    python_requires='>=3'
    include_dirs = ["."]
)
