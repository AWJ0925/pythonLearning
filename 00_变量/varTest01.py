# 1.变量三要素：变量名、变量类型、变量的值
name = "玛丽亚"
print('id：', id(name))  # 变量的内存地址
print('type：', type(name))  # 变量值的数据类型
print('value：', name)  # 变量的值

# 2.变量的操作：访问、修改值
name = "玛丽亚"
print(name, id(name))  # 访问
name = "楚留冰"  # 修改值，再访问
print(name, id(name))

# 函数的使用
age = 18
name = "yuHuan"
# var_1 is var_2：判断地址是否一样
print(age is name)  # False
# var_1 == var_2：判断值相等？
print(age == name)  # False
