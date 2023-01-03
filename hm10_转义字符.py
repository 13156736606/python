"""
转义字符为不可见字符，不能直接输出转义字符，转义字符串有特殊用途
\n: 换行
\t: tab健
# 默认打印完，自动换行，函数默认自带 end='\n' 这个换行结束符
"""
print("###############\n###############", end='')
print('are you okay\t i m very okay\t')
print('are you okay\\n i m very okay\\t')
print(r'are you okay\n i m very okay\t')
print(r'are you okay\n i m very okay\t')
print('Are you okay')
print('Are you okay')
