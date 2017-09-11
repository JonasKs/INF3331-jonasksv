#!/usr/bin/env python
import sys
import os

string = str(sys.argv[1])
folder = sys.argv[2]
for path, dirs, files in os.walk(folder):
    for f in files:
        if string in str(f):
            print(path + "/" + f)
