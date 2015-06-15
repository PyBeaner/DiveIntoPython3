__author__ = 'PyBeaner'

import xml.etree.ElementTree as etree

tree = etree.parse("download_feed.xml")
root = tree.getroot()
print(root) #<Element '{http://www.w3.org/2005/Atom}feed' at 0x02C959F0>
print(root.tag) #'{http://www.w3.org/2005/Atom}feed'
print(len(root)) # elements count

for child in root:
    print(child)

print(root.attrib) #{'{http://www.w3.org/XML/1998/namespace}lang': 'en'}
print(root[4]) # children indexing
print(root[4].attrib) # child is also an ElementTree