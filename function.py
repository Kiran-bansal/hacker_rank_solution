def is_leap(year):
    leap = False
    if (year%400==0) and (year%100==0):
        return leap
    elif (year%4==0) and (year%100!=0):
        return leap
    else:
        return False
year = int(input())
print(is_leap(year))
