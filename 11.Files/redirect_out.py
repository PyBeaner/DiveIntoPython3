__author__ = 'PyBeaner'

import sys

class RedirectStdoutTo:
    def __init__(self,new_out):
        self.new_out = new_out

    def __enter__(self):
        # when entering a context£¨with£©
        self.old_out = sys.stdout
        sys.stdout = self.new_out

    def __exit__(self, *args):
        # when exiting a context(end with)
        sys.stdout = self.old_out


print("A")
with open('out.log',mode="a",encoding="utf-8") as out, RedirectStdoutTo(out):
    print("B")
print("C")