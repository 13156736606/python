"""
格式化输出：将程序的运行结果按照一定的格式输出
format语法格式：
    # 右边的数据按顺序依次放在左边的{}中
    print('{},{}'.format(数据1，数据2))

需求：
# 1. 定义3个变量，分别保存姓名'mike'，年龄35，城市'sz'
# 2. 格式化输出：姓名：mike，年龄：35，城市：sz
"""

name = 'mike'
age = 18
city ='sz'
print("姓名：{}，年龄：{}，城市：{}".format(name,age,city))
print("我叫{}，今年{}岁，在{}工作".format(name,age,city))
