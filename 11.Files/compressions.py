__author__ = 'PyBeaner'
import gzip

with gzip.open("out.log.gz",mode="wb") as z_file:
    z_file.write('A nine mile walk is no joke, especially in the rain.'.encode('utf-8'))

import subprocess
o = subprocess.getoutput("dir -l out.log.gz")
print(o)