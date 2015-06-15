__author__ = 'PyBeaner'

# For large xml documents, lxml is significantly faster than the built-in ElementTree library
# from lxml import etree
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree

tree = etree.parse("download_feed.xml")
root = tree.getroot()
entries = root.findall('{http://www.w3.org/2005/Atom}entry')
print(len(entries))

entries = tree.findall("//{http://www.w3.org/2005/Atom}*[@href]") #all element with the "href" attr
print(len(entries)) #5
entries = tree.findall("//{http://www.w3.org/2005/Atom}*[@href='http://diveintomark.org/']") #all element with the "href" attr
print(len(entries)) #1

NS = '{http://www.w3.org/2005/Atom}'
authors = tree.findall("//{NS}author[{NS}uri]".format(NS=NS)) #Atom author elements that have an Atom uri element as a child
print(authors) # two authors


