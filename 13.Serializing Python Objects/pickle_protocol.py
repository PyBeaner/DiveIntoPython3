# coding=utf-8
__author__ = 'PyBeaner'

import pickletools
import pickle


def protocol_version(file_object):
    maxproto = -1
    for opcode,arg,pos in pickletools.genops(file_object):
        maxproto = max(maxproto,opcode.proto)
    return maxproto

with open("entry.pickle","rb") as f:
    # r = pickletools.dis(f)
    # print(r)  # highest protocol among opcodes = 3
    v = protocol_version(f)
    print(v)  # 3
