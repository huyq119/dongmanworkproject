import time

from selenium.webdriver.common.by import By

from dongman_web_test.pagefile.basepage import BasePage


class NoticeFirstDetailPage(BasePage):
    def get_content_notice_detail(self):
        _element = self.find(By.CSS_SELECTOR, '#content > div > div.notice_detail > div.notice_cont > p')
        _text = _element.text
        time.sleep(3)
        return _text
