# Name: Ashutosh Bhati
# Roll No.: 0863CS241045

def sum(*all, sign=-1):
    sum = 0
    for a in all:
        sum = sum + a
        return sign * sum


r = sum(10, 20, 30, 40, 50, 60, sign=-1)
print(r)
print(sum())
