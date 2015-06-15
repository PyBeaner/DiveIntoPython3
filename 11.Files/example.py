# coding=utf-8
# some chinese: 你好，中文

import locale

__author__ = 'PyBeaner'

# a_file = open("example.py",encoding="utf-8")
a_file = open("example.py")
# example.py
print(a_file.name)
# utf-8
# default:cp936(depends on your Operation System and the language)
print(a_file.encoding)
print(locale.getpreferredencoding()) # cp936
# r
print(a_file.mode)