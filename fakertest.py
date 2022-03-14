'''
zh_CN
zh_TW
th_TH
ru_RU
en_US
ko_KR
ja_JP
'''
from typing import List

from faker import Faker
import pyperclip
import json

fake = Faker(['zh_CN'])
text_loc = []
for i in range(1):
    text_loc.append(str(fake.phone_number()))
content = json.dumps(text_loc)
print(content)



