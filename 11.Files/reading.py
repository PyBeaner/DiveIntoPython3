# coding=utf-8
__author__ = 'PyBeaner'

a_file = open("example.py",encoding='utf-8')
s = a_file.read()
print(s)
print("at end:",len(a_file.read()))  # 0(end)

# re-read
print("re-reading..")
a_file.seek(32) # if we seek 33（the byte in the middle of a chinese char,then decode error would occur）
print(a_file.read(1)) # 你
print(a_file.read(1)) # 好
print(a_file.tell()) # 38？ because Chinese char requires multiple bytes to encode in utf-8,but English char requires only one
print(len("你好".encode("utf-8")),"你好".encode("utf-8"))

# close
a_file.close()
# I/O operation on closed file.
# a_file.read()
print(a_file.closed)
# close again(no-op)
a_file.close()


# runtime context
with open("example.py",encoding="utf-8") as a_file:
    a_file.seek(32)
    a_char = a_file.read(1)
    print(a_char)

print(a_file.closed) # True

with open("example.py",encoding="utf-8") as a_file:
    line_number = 0
    for line in a_file:
        line_number+=1
        print("{:>4} {}".format(line_number,line))