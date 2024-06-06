list = [1, 3, 5, 'A', 'B', 3, 5.4, 6.5]

print('list 长度：{0}'.format(len(list)))
print('list ：{0}'.format(list))
print('list[0] = {0}'.format(list[0]))
print('list[2] = {0}'.format(list[2]))
print('list[-1] = {0}'.format(list[-1]))
print('list[-3] = {0}'.format(list[-3]))
list.append('jin')
print('list add "jin" ：{0}'.format(list))
list.insert(1, 2)
print('list insert 1,2 ：{0}'.format(list))
list.extend(['x', 'y', 'z'])
print('list extend x,y,z ：{0}'.format(list))
print('list index jin ：{0}'.format(list.index('jin')))
# print('list index etc ：{0}'.format(list.index('etc')))
print('etc in list ：{0}'.format('etc' in list))
list.remove(3)  # 会删除首次出现的item值3
print('list remove 3 ：{0}'.format(list))
print('list.pop 删除：{0}'.format(list.pop()))  # 会删除List最后item值，并返回删除的值
print('list ：{0}'.format(list))
list = list + [8, 9]
print('list + [8,9] ：{0}'.format(list))
list = list * 2
print('list * 2 ：{0}'.format(list))

params = {'name': 'jin', 'age': '18', 'sex': 'man', 'live': 'woman'}
print('params：{0}'.format(params))
print('params.keys：{0}'.format(params.keys()))
print('params.values：{0}'.format(params.values()))
print('params.items：{0}'.format(params.items()))
newList = [k for k, v in params.items()]
print('newList：{0}'.format(newList))
newList = [v for k, v in params.items()]
print('newList：{0}'.format(newList))
newList = ['%s=%s' % (k, v) for k, v in params.items()]
print('newList：{0}'.format(newList))
str = ';'.join(newList)
print(';.join(newList)：{0}'.format(str))
newList = str.split(';')
print('str.split(;)：{0}'.format(newList))
newList = str.split(';', 1)
print('str.split(;,1)：{0}'.format(newList))
list2 = [1, 3, 5, 7, 9]
print('list2：{0}'.format(list2))
list2 = [elem * 2 for elem in list2]
print('list2：{0}'.format(list2))
list2 = [elem for elem in list2 if elem > 3]
print('list2：{0}'.format(list2))
