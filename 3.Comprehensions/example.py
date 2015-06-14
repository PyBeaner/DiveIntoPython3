__author__ = 'PyBeaner'

import os

cur_dir = os.path.abspath(os.curdir)
print(os.getcwd())
os.chdir(r"c:")
print(os.getcwd())

print(os.path.join("/User/PyBeaner/Desktop/Examples","humansize.py"))
# /User/PyBeaner/Desktop/Examples\humansize.py (on windows)
print(os.path.join("/User/PyBeaner/Desktop/Examples/","humansize.py"))
print(os.path.expanduser("~"))  # Your home directory
pathname = "/User/PyBeaner/Desktop/Examples/humansize.py"
print(os.path.split(pathname))
dirname,filename = os.path.split(pathname)
print(filename)
shortname,extension = os.path.splitext(filename)
print(extension)

# glob
os.chdir(cur_dir)
os.chdir("../2.Native Datatypes")
import glob
print(glob.glob("*.py"))