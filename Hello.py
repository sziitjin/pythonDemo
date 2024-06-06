list = ['jin', 3, 4, 5, 'suke']
if True:
    print("hello world " + list[0])
else:
    print('hello mini')
for item in list:
    print(item)


def count(a, b):
    if a > b:
        return a - b
    else:
        return a + b


print(count(2, 5))

print(count(5, 2))


