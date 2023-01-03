"""
250             int，整型
3.14            float 浮点型
'mike'          str 字符串，只要是''格式的内容就是字符串
"mike"          str 字符串，只要是""格式的内容就是字符串
True, False     bool, 布尔，非0就是真
None            NoneType, 空类型



# 查看数据类型类型
# 语法: type(数据/变量名)
# 注意: type() 函数需要配合 print() 输出函数使用
"""

# 定义变量，无需指定类型，系统会自动推导，自动根据赋值的内容推导这个变量的类型

# 查看数据类型类型
# 语法: type(数据/变量名)
# 注意: type() 函数需要配合 print() 输出函数使用
demo1=250
demo2=3.14
demo3='mike'
dem04="mike"
demo5=True
demo6=None
print(type(demo1))
print(type(demo2))
print(type(demo3))
print(type(dem04))
print(type(demo5))
print(type(demo6))

# 列表  list=[]
name_list=['mike', 'tom','yoyo']
print(name_list)
print(type(name_list))
# 元组 tuple=()
namelist2 = ('mike','tom','yoyo')
print(namelist2)
print(type(namelist2))
# 字典 dict,json格式键值对 {}
info = {'name':'mike','age':18}
print(info)
print((type(info)))


print('age=18')
age = 18
print(age)
age = 19
print(ager)
