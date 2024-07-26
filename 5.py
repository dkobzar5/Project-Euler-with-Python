# dividers = [i for i in range(1, 21)]
#
#
# def isDividing(number):
#     for item in dividers:
#         if number % item != 0:
#             return False
#     return True
#
#
# i = 20
# while True:
#     if isDividing(i):
#         print(i)
#         break
#     i += 1
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


ans = 1
for i in range(1, 21):
    ans = ans * i // gcd(i, ans)
print(ans)
