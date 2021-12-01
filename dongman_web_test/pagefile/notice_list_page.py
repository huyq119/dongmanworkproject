import time

from selenium.webdriver.common.by import By

from dongman_web_test.pagefile.basepage import BasePage


class NoticeListPage(BasePage):

    def get_list_name(self):
        element = self.find(By.CSS_SELECTOR, '#content > div > h3')
        _text = element.text
        time.sleep(4)
        return _text

