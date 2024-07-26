from functools import reduce

def reduce_func(a, b):
    a, b = int(a), int(b)
    return a+b
number = 2
n = 1000

result = reduce(reduce_func, list(str(number**n)))
print(result)