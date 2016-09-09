# Various recusrive algorithms implemented to observe patterns in how data is handlded in recusrion.
# Python 2.7
# J. Plasmeier | jplasmeier@gmail.com
# MIT License

## Function Definition

# Fibonacci Implementations
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

def fib_0toN(n):
    if n==1 or n==2:
        return 1
    next = fib_0toN(n-1)+fib_0toN(n-2)
    print next
    return next

# Fib memoized, cache empty initially
# Code from http://ujihisa.blogspot.com/2010/11/memoized-recursive-fibonacci-in-python.html
cache = {}
def fib_cache(n):
    if n in cache:
        print 'We found {0} in the cache. Its fib num is {1}'.format(n, cache[n]) 
        return cache[n]
    else:
        print 'We could not find {0} in the cache.'.format(n) 
        cache[n] = n if n < 2 else fib_cache(n-1) + fib_cache(n-2)
        print cache[n]
        return cache[n]

# Fib memoized, internal cache 
def fib_internal(n, cache=None):
    if not cache:
        cache = {}
        cache[1] = 1
        cache[2] = 1
    if n in cache:
        print 'We found {0} in the cache. Its fib num is {1}'.format(n, cache[n]) 
        return cache[n]
    else:
        print 'We could not find {0} in the cache.'.format(n) 
        cache[n] = fib_internal(n-1, cache) + fib_internal(n-2, cache)
        print cache[n]
        return cache[n]
        

# Call our functions
#print fib(10)
#print fib_0toN(10)
#print fib_cache(10)
print fib_internal(10)
