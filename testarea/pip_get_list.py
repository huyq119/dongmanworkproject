
with open("./worktest.txt") as f:
    for num in f:
        i = num.split()
        a = i[0]
        b = i[2]
        if a in ['Jinja2', 'msal-extensions', 'tidevice']:
            continue
        else:
            print(f"{a}=={b}")
