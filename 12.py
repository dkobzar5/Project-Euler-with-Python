# from math import ceil, sqrt
#
#
# def count_deviders(number):
#     count_of_deviders = 1
#     for divider in range(1, ceil(sqrt(number))):
#         if number % divider == 0:
#             count_of_deviders += 2
#     return count_of_deviders
#
#
# n = 1
# while True:
#     number = sum([i for i in range(1, n + 1)])
#     if count_deviders(number) > 500:
#         print(number)
#         break
#     n += 1
# create a list of vowels
vowel = ['a', 'e', 'i', 'u']

# 'o' is inserted at index 3 (4th position)
vowel.insert(3, 'o')


print('List:', vowel)

# Output: List: ['a', 'e', 'i', 'o', 'u']