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


numbers = []
i = 2
while len(numbers) < 10_001:
    if isPrime(i):
        numbers.append(i)
    i+=1
else:
    print(numbers[-1])