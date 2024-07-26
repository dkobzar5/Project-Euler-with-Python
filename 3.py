def isPrime(number):
    k = True
    if number%2==0:
        return False
    for i in range(3, int(pow(number,0.5))+1, 2):
        if number%i==0:
            k = False
            break
    return k

number = 600851475143

dividers = []
for i in range(2, int(pow(number,0.5))+1):
    if number % i == 0:
        dividers.extend([i, number//i])
dividers = sorted(dividers, reverse=True)


for elem in dividers:
    if isPrime(elem):
        print(elem)
        break
else:
    print('All dividers are not prime')
