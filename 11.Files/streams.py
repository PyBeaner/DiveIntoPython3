__author__ = 'PyBeaner'

a_string = 'PapayaWhip is the new black.'
import io
a_file = io.StringIO(a_string)
print(a_file.read())
print(len(a_file.read()))

a_file.seek(0)
print(a_file.read(10))
print(a_file.tell())
