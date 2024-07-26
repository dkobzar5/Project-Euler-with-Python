from functools import reduce
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
def reduce_func(a,b):
    a, b = int(a), int(b)
    return a+b
result = reduce(reduce_func, str(fact(100)))
print(result)