#!/usr/bin/env pypy3

import platform
import subprocess

print("execution info:")
print("Python version: {}".format(platform.python_version()))
print("Python implementation: {}".format(platform.python_implementation()))

import numpy
import scipy
import sklearn
import numba
import networkx

print()
print("third party library info:")
print("Numpy: {}".format(numpy.__version__))
print("Scipy: {}".format(scipy.__version__))
print("scikit-learn: {}".format(sklearn.__version__))
print("Numba: {}".format(numba.__version__))
print("NetworkX: {}".format(networkx.__version__))


command = "python3 --version"
result = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).communicate()[0].decode()
print()
print("command \"{}\" result:".format(command))
print(result)