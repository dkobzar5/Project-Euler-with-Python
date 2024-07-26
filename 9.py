from functools import reduce
def foo():
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = (pow(a, 2) + pow(b, 2)) ** 0.5
            res = a + b + c
            if res == 1000:
                return a, b, c
            if res > 1000:
                print('Break', a, b, c, res)
                break
print(reduce(lambda x,y: x*y, foo()))