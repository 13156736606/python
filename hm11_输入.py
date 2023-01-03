"""
输入：在 Python 中接收用户输入的数据的过程为程序的输入
语法格式：
    字符串变量 = input('提示信息：')
注意：
# 1. input()会等待用户的输入，按回车才会往下执行(专业叫法：阻塞)
# 2. 无论输入什么内容，接收的内容都是字符串类型

需求：
1. 提示用户输入两个数字
2. 使用获取到的数据进行加法运算
3. 在控制台输出计算结果， 格式要求： xx + xx = xx
"""
# data =input()
# print(f'内容：{data},类型：{type(data)}')

num1 = input('第一个数字：')
num2 = input('第二个数字：')
result = int(num1) + int(num2)
print(f'{num1}+{num2}={result}')