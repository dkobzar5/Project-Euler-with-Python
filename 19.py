import re

days_in_monthes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def main():
    cur_day = 1
    count = 0
    for year in range(1900, 2001):

        if re.match(r'\d{2}00', str(year)) and year % 400 == 0:
            days_in_monthes[1] = 29
        elif year % 4 == 0 and not re.match(r'\d{2}00', str(year)):
            days_in_monthes[1] = 29
        else:
            days_in_monthes[1] = 28
        p = []
        for month in days_in_monthes:
            cur_day = (month + cur_day) % 7
            p.append(cur_day)
            if cur_day == 0:
                count += 1
                print(year)

        print(p, year)
        print('____________________________')
    return count


result = main()
print(result)
