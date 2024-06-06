import cmath

print('平方计算')
a = input('输入第一个数：')
b = input('输入第一个数的平方值：')
square = int(a) ** int(b)
print('平方: {0} ** {1} = {2}'.format(a, b, square))

print('平方根计算')
c = input('输入开平方数：')
square2 = int(c) ** 0.5
print('平方根: {0} ** 0.5 = {1}'.format(c, square2))

print('平方根计算2')
d = input('输入开平方数：')
square3 = cmath.sqrt(int(d))
print('平方根: {0} ** 0.5 = {1}'.format(d, square3.real))
