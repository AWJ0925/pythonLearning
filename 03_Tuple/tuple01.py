# 二、定义
# 1.多个数据的元组
tuple1 = (2, 'anWanJia', [45, 21])
tuple2 = 30, 'yuHuan', ['wanJia', 'String']

# 2.单个数据的元组，单个数据构成的元组之后一定要加逗号
t2 = (10,)  # 元组
print(type(t2))
# 单个数据不加逗号
t3 = (10)  # 整型
print(type(t3))
t4 = ('String')  # 字符串
print(type(t4))
t5 = ('String', )  # 元组
print(type(t5))

# 3. 创建空元组
tuple3 = ()


# 三、常见的操作
t1 = ('a', 'b', 'c', 'd')
# 1.下标：正/反
print(t1[1])
print(t1[-1])

# 2.index
print(t1.index('b'))
print(t1.index('1'))  # ValueError: tuple.index(x): x not in tuple

# 3.count
print(t1.count('a'))
print(t1.count('e'))

# 4.len
print(len(t1))


# 修改：虽然元组中的元素不可变，但是列表中的元素是可变的
t1 = ('A', 'B', ['C', 'D'])
# t1[1] = '1'  # 不可变
print(t1)
print(t1[2][1])
# 修改列表中的元素
t1[2][0] = '22'
print(t1)
# 虽然元组的数据不支持修改，但是元组中列表内的数据是可以修改的，方法是：找到+赋值

#  del 语句来删除整个元组
tuple4 = '紫薇', '盖世', '玄黄', '朱雀'
del tuple4
print(tuple4)  # NameError: name 'tuple3' is not defined
