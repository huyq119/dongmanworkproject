'''
双色球彩票号码生成
'''

# _*_ conding=utf-8 _*_
import random

print("欢迎使用双色球随机生成器,祝您好运！")
while input() != 'n':
    for i in range(5):
        red = []
        while len(red) != 6:
            a = random.randint(1, 33)
            if a in red:
                continue
            red.append(a)  # 将随机值添加到red列表
        red.sort()  # 进行排序
        blue = random.randint(1, 16)
        print('红：' + str(red), end="-")
        print('蓝：' + str(blue))
    print("回车继续，n键回车退出")
