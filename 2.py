#Version 1

fib_list = [1, 2]

while True:
    next_el = fib_list[-2] + fib_list[-1]
    if next_el < 4_000_000:
        fib_list.append(next_el)
    else:
        break

fib_list = list(filter(lambda x: x % 2 == 0, fib_list))
print(sum(fib_list))

#Version 2

# a, b = 1, 2
# answer = 0
# while a < 4_000_000:
#     if a % 2 == 0:
#         answer += a
#     a, b = b, a + b
# print(answer)
