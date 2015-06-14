__author__ = 'PyBeaner'

# very slow
def recursive_fib(n):
    if n<=2:
        return n-1
    return recursive_fib(n-1)+recursive_fib(n-2)

def fib(n,max=0):
    a,b = 0,1
    i = 0
    while i<n:
        if max and a>max:
            break
        yield a
        a,b = b,a+b
        i+=1

if __name__=="__main__":
    import time
    max = 1000000
    start = time.clock()
    count = 20
    fibs = list(fib(count))
    print(fibs[-1])
    # for n in fib(20):
    #     print(n,end=" ")
    end = time.clock()
    print()
    #  0.000033 seconds
    print("Fib(yield) spent %f seconds" %(end-start))

    print()
    start = time.clock()
    r = recursive_fib(count)
    print(r)
    end = time.clock()
    print()
    #  0.003518 seconds
    print("Fib(recursive) spent %f seconds" %(end-start))
