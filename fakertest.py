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
text_job = []
for i in range(3):
    text_loc.append(str(fake.phone_number()))
    text_job.append(str(fake.job()))
content_phone_number = json.dumps(text_loc, ensure_ascii=False)
content_job = json.dumps(text_job, ensure_ascii=False)
print(content_phone_number)
print(content_job)



