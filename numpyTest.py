import numpy as np

# np.array()：创建数组
arr = np.array([1, 2, 3, 4])
print(arr)
# np.arange()：创建等差数组
arr = np.arange(0, 10, 2)
print(arr)
# np.zeros()：创建元素全为0的数组
arr = np.zeros((3, 4))
print(arr)
# np.ones()：创建元素全为1的数组
arr = np.ones((2, 3))
print(arr)
# np.linspace()：创建等间距数组
arr = np.linspace(1, 6, 3)
print(arr)
# np.eye()：创建对角线为1的矩阵
arr = np.eye(4)
print(arr)
# np.reshape()：改变数组的形状
arr = np.arange(1, 10)
print(arr)
arr = np.reshape(arr, (3, 3))
print(arr)
# arr.flatten()：将多维数组转换为一维数组
arr = np.array([[0, 1, 2, 3, ], [4, 5, 6, 7]])
print(arr)
arr = arr.flatten()
print(arr)
# np.sort()：对数组的元素进行排序
arr = np.array([1, 7, 2, 5, 9, 4])
arr = np.sort(arr)
print(arr)
# np.argmax()：返回数组中最大元素的索引
arr = np.array([1, 7, 2, 5, 9, 4])
index = np.argmax(arr)
print("index:" + str(index))
# np.add()：两个数组相加
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([2, 3, 4, 5])
arr = np.add(arr1, arr2)
print(arr)
# np.dot()：对两个数组进行点乘
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([2, 3, 4, 5])
arr = np.dot(arr1, arr2)
print(arr)