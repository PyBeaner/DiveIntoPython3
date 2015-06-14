__author__ = 'PyBeaner'

# very slow
def recursive_fib(n):
    if n<=1:
        return n
    return recursive_fib(n-1)+recursive_fib(n-2)

def fib(max):
    a,b = 0,1
    while a<max:
        yield a
        a,b = b,a+b

if __name__=="__main__":
    import time
    max = 1000000
    start = time.clock()
    for n in fib(max):
        print(n,end=" ")
    end = time.clock()
    print()
    #  0.000092.2 seconds
    print("Fib(yield) spent %f.2 seconds" %(end-start))

    print()
    n = 0
    start = time.clock()
    while True:
        f = recursive_fib(n)
        if f>max:
            break
        print(f,end=" ")
        n+=1
    end = time.clock()
    print()
    #  2.408104.2 seconds
    print("Fib(recursive) spent %f.2 seconds" %(end-start))
