def isPalindrom(number):
    if str(number)[::-1] == str(number):
        return True
    return False


result = 0
for a in range(100, 1000):
    for b in range(100, 1000):
        number = a * b
        if isPalindrom(number) and number > result:
            result = number
print(result)