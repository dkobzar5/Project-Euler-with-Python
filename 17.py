ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


# def thousand_compile(number):
#     return 'one thousand', 1000
#
#
# def hundred_compile(number):
#     return ONES[number]+'hundred'
#
#
# def dozen_compile(number):
#     pass
#
#
# def unit_compile(number):
#     pass
#
#
# def main(number):
#     result = ''
#     while number != 0:
#         number_length = len(str(number))
#         str_number = str(number)[0]
#
#         compiled_part = compile_functions[number_length](str_number)
#
#         number -= compiled_part[1]
#         result += compiled_part[0]
#     return result
#
#
# compile_functions = {4: thousand_compile, 3: hundred_compile, 2: dozen_compile, 1: unit_compile}
# print(main(1100))
def compute():
    ans = sum(len(main(i)) for i in range(1, 1001))
    return str(ans)


def main(n):
    if 0 <= n < 20:
        return ONES[n]
    elif 20 <= n < 100:
        return TENS[n // 10] + (ONES[n % 10] if (n % 10 != 0) else "")
    elif 100 <= n < 1000:
        return ONES[n // 100] + 'hundred' + (('and' + main(n % 100) if (n % 100 != 0) else ""))
    elif 1000 <= n < 1000000:
        return main(n // 1000) + "thousand" + (main(n % 1000) if (n % 1000 != 0) else "")


if __name__ == "__main__":
    print(compute())
