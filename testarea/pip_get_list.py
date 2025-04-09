import os
import subprocess


# 定义安装更新包的函数
def install_package(package_name):
    print(f"安装更新包{package_name}")
    cmd = ["pip3", "install", "--upgrade", package_name]
    subprocess.run(cmd, check=True)

# 指定要跳过更新的包名
skip_list = ['tidevice', 'charset-normalizer', 'websocket-client', 'cryptography', 'greenlet', 'python-slugify']

with open("./worktest.txt") as f:
    for num in f:
        i = num.split()
        try:
            a = i[0]
            # b = i[2]
        except IndexError:
            print("列表为空或没有足够的元素")
            continue

        if a not in skip_list:
            install_package(a)