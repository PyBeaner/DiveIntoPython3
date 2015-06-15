__author__ = 'PyBeaner'

import xml.etree.ElementTree as etree

NSMAP = {None: 'http://www.w3.org/2005/Atom'}
new_feed = etree.Element('{http://www.w3.org/2005/Atom}feed',
                         attrib={'{http://www.w3.org/XML/1998/namespace}lang': 'en'})

print(etree.tostring(new_feed)) #b'<ns0:feed xmlns:ns0="http://www.w3.org/2005/Atom" xml:lang="en" />'

import lxml.etree
new_feed = lxml.etree.Element("feed",nsmap=NSMAP)
print(lxml.etree.tounicode(new_feed))
new_feed.set('{http://www.w3.org/XML/1998/namespace}lang', 'en')
print(lxml.etree.tounicode(new_feed))
# sub element
title = lxml.etree.SubElement(new_feed,"title",attrib={"type":"html"})
print(lxml.etree.tounicode(new_feed))
print(lxml.etree.tounicode(new_feed,pretty_print=True))