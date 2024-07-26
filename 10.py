def isPrime(number):
    k = True
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(pow(number, 0.5)) + 1, 2):
        if number % i == 0:
            k = False
            break
    return k

arr = sum([i for i in range(2,2_000_000) if isPrime(i)])
print(arr)