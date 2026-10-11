# Name: Ashutosh Bhati
# Roll No.: 0863CS241045

sum = lambda a, b: a + b
print(sum(20, 30))

sqr = lambda a: a * a
print(sqr(9))

greater = lambda a, b, c: a if a > b and a > c else b
print(greater(20, 30, 40))

l1 = [10, 20, 30, 40, 50]
l2 = list(map(lambda n: n > 30, l1))
print(l2)
print(l2)
