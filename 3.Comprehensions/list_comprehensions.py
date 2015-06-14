__author__ = 'PyBeaner'

a_list = [1,9,8,4]
print([elem*2 for elem in a_list])
print(a_list)
a_list = [elem*2 for elem in a_list]
print(a_list)

import os,glob
print(glob.glob("*.py"))
print([os.path.realpath(p) for p in glob.glob("*.py")])
print([os.path.realpath(p) for p in glob.glob("*.py") if os.stat(p).st_size>500])
