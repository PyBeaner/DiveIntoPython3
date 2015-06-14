__author__ = 'PyBeaner'

print(eval("1+1==2"))

import subprocess
print(eval("subprocess.getoutput('dir')"))
# Eval is Evil!
# print(eval("rm /some/random/file"))

# event if module not imported
print(eval("__import__('os').listdir(r'c:\')"))

# Keep eval safe
# print(eval("os.listdir(r'c:\')",None))  # os is undefined
# but __import__ still works..
print(eval("__import__('os').listdir(r'e:\')",None))
# disable builtins
# print(eval("__import__('os').listdir(r'e:\')",{"__builtins__":{}}))

# even we disable the builtins,something else may still harm your server
a = 0
eval("a=2**2147483647",{"__builtins__":{}})
print(a)