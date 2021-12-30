# -*-coding:utf-8-*-

# 三、常见的操作：增、删、改、查
# 3.1 查找
name_list = ['Tom', 'Lily', 'Rose']
print(name_list)
print(name_list[1])  # 正向
print(name_list[-2])  # 反向

# 切片
name_list = ['xiao1', 'xiao2', 'xiao3']
print(name_list[0:2])  # 左闭右开


# 2.函数：index(), count(), len()
# index()：序列名.index(数据，[开始位置下标，结束位置下标]），默认在整个序列中查找，返回索引（下标）
# 注意：返回的是第一个匹配值的索引
name_list = ['Tom', 'Lily', 'Rose']
print(name_list.index('Lily'))  # 返回数值1

# 注：序列中不含有该元素则会返回：ValueError: 'Tom' is not in list
print(name_list.index('Tom', 1, 2))  # 不包含结束位置
# 注：查找未在其中的数据会返回：ValueError: 'Tos' is not in list
# print(name_list.index('Tos'))

# count()：统计被查询的数据在序列中出现的次数
print(name_list.count('Lily'))  # 1
print(name_list.count('LI'))  # 0

# len()：访问列表的长度，即列表中元素的个数。常用于循环遍历
print(len(name_list))

# in ：在——True,不在——False和 not in:不在——True，在——False,
name_list = ['Tom', 'Lily', 'Rose']
print('Tom' in name_list)  # True
print('LI' in name_list)  # False
print('Tom' not in name_list)  # False
print('li' not in name_list)  # True


# 应用案列
'''需求分析：注册邮箱。
步骤：
1、用户输入一个账户名；
2、判断这个账户名是否已经存在。如果存在，提示用户重新输入；否则，提示可以注册。'''
name_list = ['Tom', 'Lily', 'Rose']  # 已经存在的数据列表
name = input('请输入您的用户名：')  # 用户输入自己的用户名
if name in name_list:  # 存在
    print(f'您输入的用户名是{name}，该用户名不可以使用！')
else:
    print("您输入的用户名是{}，这个用户名可以使用。".format(name))

# 修改版
name_list = ['Tom', "Rose", "Lily"]
first_name = input("请输入您的用户名：")
while first_name in name_list:
    print('您输入的用户名{}，该用户名已被注册！'.format(first_name))
    first_name = input("请再次输入您的用户名：")

# 回顾 3种常见格式化输出方式
print(f'您输入的用户名是%s。' % first_name)
print(f'您输入的用户名是{first_name}。')
print('您输入的用户名是{}。'.format(name))


# 3.2 增加：append(), extend(), insert()
# 1.append()格式：序列名.append(数据):将数据当做一个元素插入序列的末尾
name_list = ['Tom', "Lily", 'Rose']
name_list.append('小明')  # 增加单个数据
print(name_list)
name_list.append([11, 22])  # 增加一个列表
print(name_list)
'''
总结：
（1）append（）中的参数无论是单个数据还是一个列表，append函数都会将其原封不动的加至原列表的末尾
（2）列表中的数据可变（元素可以增加或减少或修改），所以它是一种可变数据类型
'''

# 2.extend
name_list.extend('liHua')  # 单个数据
print(name_list)
name_list.extend([33, 45])  # 列表
print(name_list)
# 总结：extend()将（—）中的字符串或列表拆开之后，加在列表的结尾

# 3.insert()：指定位置增加元素。语法：列表名.insert（位置下标，数据）
name_list.insert(2, 'xiaoSan')
print(name_list)
name_list.insert(3, [1, 2])  # 不拆开
print(name_list)


# 3.3 删除：del, pop, remove, clear
# 1.del(目标)或del 目标：可以删除单个元素或整个列表
name_list = ['Tom', 'Lily', 'Rose']
del(name_list)  # 删除整个列表,再次打印，则会报错
del name_list

del(name_list[1])  # 删除单个元素
del name_list[1]
print(name_list)

# 2.pop()：只能删除个别的元素，且具有返回值（返回值是被删除的元素）
'''pop() 默认删除 list 末尾的元素，也可用于删除指定下标的数据'''
name_list = ['Tom', 'Lily', 'Rose']
del_name1 = name_list.pop()  # 不指定下标，则删除列表中的最后一个数据
print(del_name1)   # 查看返回值
print(name_list)

# 删除指定下标的元素
del_name2 = name_list.pop(1)
print(del_name2)
print(name_list)

# 3.remove()：移除列表中的第一个匹配项
name_list = ['Tom', 'Lily', 'Rose']
name_list.remove('Rose')
print(name_list)

# clear()：清空列表中的元素
name_list.clear()
print(name_list)
# 删除和清空的区别：删除是直接没有了，清空是清空了列表中的数据


# 3.4 修改：修改指定位置的数据：找到+赋值 -->列表是可变数据类型（列表中的元素是可以修改的）
name_list = ['TOM', 'LILY', 'ROSE']
name_list[2] = 'Wei'  # 找到，赋新值
print(name_list)

# 2.逆序 reverse()
list1 = [1, 2, 3]
list1.reverse()
print(list1)

# 3.排序 sort(),默认升序
list2 = [3, 4, 5]
list2.sort()
print(list2)

list2.sort(reverse=False)  # 顺排序：从小到大
print(list2)
list2.sort(reverse=True)  # 逆排序：从大到小
print(list2)


# 3.5 复制copy()
name_list = ['TOM', 'LILY', 'ROSE']
nameListCopy = name_list.copy()
print(name_list)
print(nameListCopy)

# 复制
copyNameList = name_list[:]

# 四、列表的循环遍历：依次访问列表中的各个元素
# 1.while
name_list = ['TOM', 'LILY', 'ROSE']
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1  # 计数器很重要

# 2.for
nameList = ['TOM', 'LILY', 'ROSE']
for element in name_list:
    print(element)
# 改进
print([element for element in nameList])


# 五，嵌套
# 1 dimension
nameList1D = ['TOM', 'LILY', 'ROSE']
# 2 dimension
nameList2D = [
    ['TOM', 'LILY', 'ROSE'],
    ['小安', '小王', '小黄'],
    ['xiao1', 'xiao2', 'xiao3']
]
print(nameList2D[0])
print(nameList2D[0][1])

# 3dimension
nameList3D = [
    [[1, 2, 3], [4, 5, 6]],
    [[6, 7, 8], [9, 10, 11]],
    [[12, 13, 14], [15, 16, 17]]
]
# 从外到内
print(nameList3D[0][0][0])  # 1


# 六，应用--随机分配办公室
'''
1.准备数据：老师的名字、3个办公室——列表嵌套；[[01],[02],[03]]
2.分配老师到办公室：随机分配，就是把老师的名字写入（列表数据的增加）到办公室的列表——办公室的列表追加老师的名字
3.验证是否分配成功：打印办公室的详细信息：打印办公室的人数和对应的老师的名字
'''
import random as rd  # 导入随机模块并重命名
# 1.准备数据
teacherNames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # 老师
offices = [[], [], []]

# 2.分配老师到办公室：随机分配——遍历老师列表数据
for na in teacherNames:
    id_of = rd.randint(0, 2)
    offices[id_of].append(na)   # 把老师的名字增加至某个办公室
print(offices)

# 3.验证
i = 1
for of in offices:  # 为了知道每个办公室的老师都是谁，要对办公室进行遍历
    print(f'办公室{i}的人数是{len(of)}，老师分别是：', end='  ')
    for na in of:   # 每个办公室人员的遍历
        print(na, end='    ')
    print()
    i += 1
