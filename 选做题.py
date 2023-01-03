# 定义一个字典变量
dict_data = {'name': 'mike', 'age': 18, 'city': '深圳'}
# 按如下格式打印：dict_data变量内容为：xxx，dict_data变量类型为：yyy
print(f'dict_data变量的内容为：{dict_data}\tdict_data变量类型为：{type(dict_data)}')
# 定义一个列表变量
list_data = ['mike', 18, '深圳']
# 按如下格式打印：list_data变量内容为：xxx，list_data变量类型为：yyy
print(f'list_data的变量内容为{list_data}\tlist_data的变量类型为：{type(list_data)}')
# 定义一个字符串变量
str_data = "{'name': 'mike', 'age': 18, 'city': '深圳'}"
# 通过eval()进行类型转换，打印转换后的内容、转换后的类型
conversion = eval(str_data)
print(f'conversion={conversion},conversion的类型为：{type(conversion)}')
# 定义一个字符串变量
str_data = "['mike', 18, '深圳']"
# 通过eval()进行类型转换，打印转换后的内容、转换后的类型
conversion =eval(str_data)
print(f'conversion={conversion},conversion的类型为：{type(conversion)}')
# 定义一个字符串变量
str_data = "250"
conversion =eval(str_data)
print(f'conversion={conversion},conversion的类型为：{type(conversion)}')
# 通过eval()进行类型转换，打印转换后的内容、转换后的类型

# 用自己语言总结一下eval()的作用
# 1、计算字符串中有效的表达式，并返回结果。
# 2、将字符串转成相应的对象（如list、tuple、dict和string之间的转换）。
# 3、将利用反引号转换的字符串再反转回对象。

# 输入一个成绩
# score = int(input('socre:'))
#
# # 学习成绩 大于等于90分的同学输出A，60-89分之间输出B，60分以下输出C
# if score>=90:
#     print('A')
# elif 89>=score>=60:
#     print('B')
# else:
#     print('C')
"""
1. 编写程序，输入三角形的3条边，判断该三角形是否成立，如果可以打印：该三角形成立，否则，打印：该三角形不成立
2. 成立条件：两边之和大于第三边
"""
# A=int(input('A='))
# B=int(input('B='))
# C=int(input('C='))
# if A+B>C or A+C>B or B+C>A:
#     print('三角形成立！')
# else:
#     print('三角形不成立')


"""
1. 查询水果价格
2. 给定四种水果，分别是苹果（apple）、梨（pear）、桔子（orange）、葡萄（grape）
   单价分别对应为3.00元/公斤、2.50元/公斤、4.10元/公斤、10.20元/公斤。
3. 首先在屏幕上显示以下菜单：
    [1] apple [2] pear [3] orange [4] grape [0] exit
4. 用户可以输入编号1~4查询对应水果的单价。  显示格式：苹果（apple）单价为3.00元/公斤
    当连续查询次数超过5次时，程序应自动退出查询；
    不到5次而用户输入0即退出；
    输入其他编号，显示价格为0。
"""
# i = 1
# while i <= 5:
#     print('[1] apple [2] pear [3] orange [4] grape [0] exit')
#     data = int(input('请输入编号1~4查询对应水果的单价，0为退出查询系统:\n'))
#     if data == 1:
#         print('apple:3.00元/公斤')
#     elif data == 2:
#         print('pear:2.50元/公斤')
#     elif data == 3:
#         print('orange:4.10元/公斤')
#     elif data == 4:
#         print('grape:10.20元/公斤')
#     elif data == 0:
#         break
#     else:
#         print('请重新输入正确数字查询！')
#     i += 1
