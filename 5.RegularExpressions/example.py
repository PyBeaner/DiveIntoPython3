__author__ = 'PyBeaner'

s = '100 NORTH MAIN ROAD'
print(s.replace("ROAD","RD."))
s = '100 NORTH BROAD ROAD'
print(s.replace("ROAD","RD."))
print(s[:-4]+s[-4:].replace("ROAD","RD."))

import re
s = re.sub("ROAD$","RD.",s)
print(s)


s = "100 BROAD"
print(re.sub("ROAD$","RD.",s)) # 100 BRD.
print(re.sub("\\bROAD$","RD.",s))  #ok
print(re.sub(r"\bROAD$","RD.",s))  # raw(would not be escaped)
print(re.sub(r"\bROAD\b","RD.",s)) # match whether at at the end/beginning/middle
