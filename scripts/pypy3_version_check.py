#!/usr/bin/env pypy3

import platform
import subprocess

print("execution info:")
print("Python version: {}".format(platform.python_version()))
print("Python implementation: {}".format(platform.python_implementation()))

command = "pypy3 --version"
result = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).communicate()[0].decode()
print()
print("command \"{}\" result:".format(command))
print(result)