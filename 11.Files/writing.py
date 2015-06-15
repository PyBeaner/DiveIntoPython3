__author__ = 'PyBeaner'

with open("test.log","w") as a_file:
    a_file.write("test succeeded")

with open("test.log") as a_file:
    print(a_file.read())

with open("test.log","a") as a_file:
    a_file.write(" and again")

with open("test.log") as a_file:
    print(a_file.read())