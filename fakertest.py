"""
zh_CN
zh_TW
th_TH
ru_RU
en_US
ko_KR
ja_JP
"""
from typing import List
from faker import Faker
import pyperclip
import json

fake = Faker(['zh_CN'])
text_loc = []
text_job = []
text_name = []
text_paragraph = []
for i in range(3):
    text_loc.append(str(fake.phone_number()))
    text_job.append(str(fake.job()))
    text_name.append(str(fake.name()))
    text_paragraph.append(fake.paragraph(nb_sentences=5, variable_nb_sentences=False))

content_phone_number = json.dumps(text_loc, ensure_ascii=False)
content_job = json.dumps(text_job, ensure_ascii=False)
content_name = json.dumps(text_name, ensure_ascii=False)
content_paragraph = json.dumps(text_paragraph, ensure_ascii=False)
print(content_phone_number)
print(content_job)
print(content_name)
print(content_paragraph)



