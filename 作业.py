# # 将字符串"123"转化为整数，将整数100转化为字符串，分别输出转换后内容和类型
# num = int('123')
#
# str1 = str(100)
#
# print(f'{num}:', type(num))
# print(f'{str1}:', type(str1))
#
# # 3. 案例需求：
#
# #    - 输入姓名 name
# name =input("姓名：")
# #    - 输入苹果的单价 price，类型为浮点型(小数)
# price = float(input('苹果单价：'))
# #    - 输入苹果的重量 weight，类型为整型
# weight= int(input('苹果重量：'))
# #    - 完成总价格的计算：单价乘以重量
# sum_price = price*weight
# #    - 格式化输出：`谁买了xxx斤苹果，单价为xxx元，总价格为xxx元`
# print(f'{name}买了{weight}斤苹果,单价为{price},总价为{sum_price}元')
# #      - 谁，要替换具体输入的姓名
# #      - xxx要替换为具体的值
# #      - 分别使用 format、f字符串 2种方式格式化
# print('{}买了{}斤苹果，单价为{}，总计为{}元'.format(name,weight,price,sum_price))
#
# #    答案：

# 1. 获取用户输入的用户名信息
username = input('输入用户名：')
# 2. 如果用户名信息是 admin, 就在控制台输出出来
if username == 'admin':
    print(username)
# 3. 如果用户名信息不是 admin, 就在控制台输出"用户名错误!"
if username != 'admin':
    print('用户名错误！')