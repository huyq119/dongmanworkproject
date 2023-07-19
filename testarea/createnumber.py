import random

def generate_lottery_numbers():
    # 生成蓝色球的号码（自定义）
    blue_ball = input("请输入蓝色球的号码: ")

    # 生成红色球的号码（随机）
    red_balls = random.sample(range(1, 34), 6)
    sorted_red_balls = sorted(red_balls)

    # 打印生成的彩票号码
    print("双色球彩票号码:")
    print(f"蓝色球: {blue_ball}")
    print("红色球:", end=" ")
    for ball in sorted_red_balls:
        print(ball, end=" ")
    print()

# 调用函数生成彩票号码
generate_lottery_numbers()
