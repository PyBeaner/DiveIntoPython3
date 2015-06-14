__author__ = 'PyBeaner'

class Fib:
    """
    Iterator that yield numbers in the Fibonacci sequence
    """

    def __init__(self,max):
        self.max = max

    def __iter__(self):
        """
        called manually by you or automatically by a for loop
        :return:an iterator should always return an object that implements the __next__ method
        """
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib>self.max:
            raise StopIteration
        self.a,self.b = self.b,self.a+self.b
        return fib  # Do not use yield here(yield is used in generators)

if __name__ == "__main__":
    fib = Fib(1000)
    print(fib,fib.__class__,fib.__doc__)
    for f in fib:
        print(f,end=" ")
