# coding=utf-8
__author__ = 'PyBeaner'

import pickletools
import pickle
with open("entry.pickle","rb") as f:
    r = pickletools.dis(f)
    print(r)