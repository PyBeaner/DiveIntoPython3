__author__ = 'PyBeaner'
import fractions
import math

def is_it_true(anything):
    if anything:
        print("yes,{0} is true".format(str(anything)))
    else:
        print("no,{0} is false".format(str(anything)))

if __name__=="__main__":
    # <class 'int'>
    print(type(1))

    # True
    print(isinstance(1,int))

    x = fractions.Fraction(1,3)
    print(x)
    print(x*2)
    print(fractions.Fraction(4,6))
    # Error
    # print(fractions.Fraction(0,0))

    print(math.pi)
    print(math.sin(math.pi/2))

    is_it_true(1)
    is_it_true(-1)
    is_it_true(0)
    is_it_true(0.1)
    is_it_true(0.0)

    is_it_true(fractions.Fraction(1,2))
    is_it_true(fractions.Fraction(0,2))