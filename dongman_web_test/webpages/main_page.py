import time

from selenium.webdriver import TouchActions, ActionChains
from selenium.webdriver.common.by import By

from dongman_web_test.webpages.basepage import BasePage
from dongman_web_test.webpages.first_notice_for_details import NoticeFirstDetailPage
from dongman_web_test.webpages.notice_list_page import NoticeListPage
from dongman_web_test.webpages.search_bar import SearchPage


class MainPage(BasePage):

    def goto_signin(self):
        pass

    def goto_signup(self):
        pass

    def goto_viewpage(self):
        return True

    def go_to_search_page(self):
        self.find(By.CSS_SELECTOR, '#header > div > div > '
                                   'a.btn_search._btnSearch.N\=a\:gnb\.search\,g\:zh_CN_zh-hans').click()
        return SearchPage(self._driver)

    def get_main_title_name(self):
        return self._driver.title

    def get_name_notice_first(self):
        # _element = self.find(By.CSS_SELECTOR, "#dailyTab > li.on ")
        self._driver.execute_script("var q=document.documentElement.scrollTop=100000")
        # _actions = TouchActions(self._driver)
        # _actions.scroll_from_element(_element, 0, 1500).perform()
        time.sleep(5)
        _text = self.find(By.CSS_SELECTOR,
                          '#noticeArea > div > a.notice_cont.NPI\=a\:notpage\,g\:zh_CN_zh-hans > span').text
        return _text

    def go_to_notice_first_detail(self):
        self._driver.execute_script("var q=document.documentElement.scrollTop=100000")
        time.sleep(5)
        self.find(By.CSS_SELECTOR, '#noticeArea > div > a.notice_cont.NPI\=a\:notpage\,g\:zh_CN_zh-hans > span').click()
        return NoticeFirstDetailPage(self._driver)

    def go_to_notice_list_page(self):
        self._driver.execute_script("var q=document.documentElement.scrollTop=100000")
        time.sleep(5)
        self.find(By.CSS_SELECTOR, '#noticeArea > div > a.notice_tit.NPI\=a\:notlist\,g\:zh_CN_zh-hans').click()
        return NoticeListPage(self._driver)
