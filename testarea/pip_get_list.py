import os
with open("./worktest.txt") as f:
    for num in f:
        i = num.split()
        a = i[0]
        b = i[2]
        if a in ['Jinja2', 'msal-extensions', 'tidevice']:
            continue
        else:
            print(f"安装更新包{a}=={b}")
            os.system(f"pip3 install --upgrade {a}")
