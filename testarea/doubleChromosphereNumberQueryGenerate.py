import requests
import re
import random
import yaml

url = 'http://henanfucai.com/'
resp = requests.get(url)
c = re.findall(
    '<p>双色球[\s\S]*第(.*?)期</p>[\s\S]*<p>开奖号码：<span class="red">([0-9][0-9])</span><span class="red">([0-9][0-9])</span><span class="red">([0-9][0-9])</span><span class="red">([0-9][0-9])</span><span class="red">([0-9][0-9])</span><span class="red">([0-9][0-9])</span><span class="blue">([0-9][0-9])</span></p>',
    resp.text)
print(c)
a = list(c[0])  # c[0]为元组 a=['2021106', '01', '04', '07', '14', '30', '31', '03']
phase = a[0]
del (a[0])  # a = ['17', '20', '22', '23', '26', '28', '06']
a1 = a
lucky_num = 'red: ' + a[0] + ' ' + a[1] + ' ' + a[2] + ' ' + a[3] + ' ' + a[4] + ' ' + a[5] + ' blue: ' + a[6]


# print(lucky_num) red: 01 04 07 14 30 31 blue: 03

# 判断是否中奖的规则：
# 实现方法，将中奖号码和自己的号码放入list中，用for循环进行比对
def query(you_phase, your_lucky_num):
    count = 0
    # your_lucky_num=str(your_lucky_num.spilt(' '))
    flag = False
    if you_phase != phase:
        print('期数错误')
    else:
        if a[6] == your_lucky_num[6]:
            flag = True  # 蓝色球相同
        winningNumbers = list(set(a[0:6]).intersection(set(your_lucky_num[0:6])))
        count = len(winningNumbers)
        print("中奖红色号码为：" + str(winningNumbers))
        #
        # for i in a[0:6]:
        #     for j in your_lucky_num[0:6]:
        #         if i == j:
        #             count = count + 1  # count:1 红球有n个相同，则count=n
        if flag:  # 蓝色球中了
            if count <= 2:
                print('恭喜你，中了六等奖！')
            elif count == 3:
                print('恭喜你，中了五等奖！')
            elif count == 4:
                print('恭喜你，中了四等奖！')
            elif count == 5:
                print('恭喜你，中了三等奖！')
            elif count == 6:
                print('恭喜你，中了一等奖！')
        elif not flag:
            if count <= 3:
                print('很遗憾，你没有中奖！')
            elif count == 4:
                print('恭喜你，中了五等奖！')
            elif count == 5:
                print('恭喜你，中了四等奖！')
            elif count == 6:
                print('恭喜你，中了二等奖！')


# 红球范围是1-33，蓝球范围是1-16
# 从1-33中取出6个数字，从蓝球中取出一个数字


def creatLuckyNum():
    numbers_list = []
    for i in range(5):
        # blueball = random.randint(1, 16)
        blueball = 1
        luckynum1 = ''
        judgement = []
        r = 0
        while r < 6:
            redball = random.randint(1, 33)
            if redball in judgement:
                continue
            judgement.append(redball)
            r += 1
        new_red = sorted(judgement)
        for j in new_red:
            new_ball = j
            if new_ball <= 9:
                new_ball = '0' + str(new_ball)
            luckynum1 += str(new_ball) + ' '
        if blueball <= 9:
            blueball = '0' + str(blueball)
        number_add = str(luckynum1) + str(blueball)
        numbers_list.append(number_add)
        print('红球：' + str(luckynum1) + ' ' + '蓝球：' + str(blueball))

    for j in numbers_list:
        print(j)
    print('祝你好运！')


if __name__ == '__main__':
    i = "y"
    while i == "y":
        print('1.查询最新一期中奖号码')
        print('2.查询最新一期你是否中奖')
        print('3.随机生成一个幸运号码')
        print('4.退出')
        num = input('请输入操作序号')
        if num == '1':
            result = phase+" "+lucky_num
            print(result)
            with open('./result_log.txt', 'a') as log:
                log.write('\n'+result)

        elif num == '2':
            you_phase = input('请输入最新一期期数')
            lottery_list = yaml.safe_load(open("./lotterynumberlist.yml"))
            for number in lottery_list:
                your_lucky_num = number
                b = your_lucky_num.split(' ')
                query(you_phase, b)

        elif num == '3':
            creatLuckyNum()

        elif num == '4':
            break

        i = input("是否继续？")
