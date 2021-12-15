'''
zh_CN
zh_TW
th_TH
ru_RU
en_US
ko_KR
ja_JP
'''

from faker import Faker
import pyperclip

fake = Faker(['ko_KR'])
text_loc = ''
for i in range(5):
    text_loc = text_loc + '\n' + fake.address()
pyperclip.copy(text_loc)
print(text_loc)

# phone_number_list = []
# for i in range(10):
#     phone_number_list.append(fake.phone_number())
# print(phone_number_list)
