'''
双色球彩票号码生成
'''

# _*_ conding=utf-8 _*_
import random

print("欢迎使用双色球随机生成器,祝您好运！")
while input() != 'n':
    red = []
    while len(red) != 6:
        a = random.randint(1, 33)
        if a in red:
            continue
        red.append(a)  # 将随机值添加到red列表
    red.sort()  # 进行排序
    blue = random.randint(1, 16)

    print(red, end="+")
    print(blue)
    print("回车继续，n键回车退出")
