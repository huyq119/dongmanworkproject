import os
with open("./worktest.txt") as f:
    for num in f:
        i = num.split()
        a = i[0]
        b = i[2]
        if a in ['tidevice', 'charset-normalizer', 'websocket-client', 'cryptography']:
            continue
        else:
            print(f"安装更新包{a}=={b}")
            os.system(f"pip3 install --upgrade {a}")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        