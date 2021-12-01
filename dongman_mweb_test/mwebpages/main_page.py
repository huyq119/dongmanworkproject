import time

from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By

from dongman_mweb_test.mwebpages.bashpage import BasePage
from dongman_mweb_test.mwebpages.new_work_recommend_page import NewWorkRecommendPage
from dongman_mweb_test.mwebpages.notice_detail_page import NoticeDetailPage
from dongman_mweb_test.mwebpages.notice_list_page import NoticeListPage
from dongman_mweb_test.mwebpages.ranking_list_page import RankingPage
from dongman_mweb_test.mwebpages.search_page import SearchPage


class MainPage(BasePage):

    def goto_signin(self):
        pass

    def goto_signup(self):
        pass

    def goto_viewpage(self):
        return True

    def go_to_search_page(self):
        self.find(By.CSS_SELECTOR, "#home-header > div.gnb.header_content > a").click()
        return SearchPage(self._driver)

    def go_to_ranking_page(self):
        self.find(By.CSS_SELECTOR, '#ct > h2.title.phbTitle > a').click()
        return RankingPage(self._driver)

    def go_to_recommend_page(self):
        # _element = self.find(By.CSS_SELECTOR, "#ct > h2.title.phbTitle > a")
        # _actions = TouchActions(self._driver)
        # _actions.scroll_from_element(_element, 0, 1500).perform()
        self._driver.execute_script("var q=document.documentElement.scrollTop=100000")
        _text = self.find(By.CSS_SELECTOR, "#ct > h2.title.newWorkRecommendPageTitle > a").click()
        return NewWorkRecommendPage(self._driver)

    def get_name_ranking(self):
        _text = self.find(By.CSS_SELECTOR, '#ct > h2.title.phbTitle > a').text
        return _text

    def get_name_new_work(self):
        # _element = self.find(By.CSS_SELECTOR, "#ct > h2.title.phbTitle > a")
        # _actions = TouchActions(self._driver)
        # _actions.scroll_from_element(_element, 0, 1500).perform()
        self._driver.execute_script("var q=document.documentElement.scrollTop=100000")
        _text = self.find(By.CSS_SELECTOR, "#ct > h2.title.newWorkRecommendPageTitle > a").text
        return _text

    def get_name_notice_first(self):
        # _element = self.find(By.CSS_SELECTOR, "#ct > h2.title.phbTitle > a")
        # _actions = TouchActions(self._driver)
        # _actions.scroll_from_element(_element, 0, 1500).perform()
        # _element = self.find(By.CSS_SELECTOR, "#noticeArea > a.NPI\:a\=notpage\,g\:zh_CN_")
        self._driver.execute_script("var q=document.documentElement.scrollTop=100000")
        time.sleep(4)
        _text = self.find(By.CSS_SELECTOR, "#noticeArea > a.NPI\:a\=notpage\,g\:zh_CN_").text
        return _text

    def go_to_notice_first_detail(self):
        # _element = self.find(By.CSS_SELECTOR, "#ct > h2.title.phbTitle > a")
        # _actions = TouchActions(self._driver)
        # _actions.scroll_from_element(_element, 0, 1500).perform()
        self._driver.execute_script("var q=document.documentElement.scrollTop=100000")
        self.find(By.CSS_SELECTOR, '#noticeArea > a.NPI\:a\=notpage\,g\:zh_CN_').click()
        return NoticeDetailPage(self._driver)

    def go_to_notice_list(self):
        self._driver.execute_script("var q=document.documentElement.scrollTop=100000")
        self.find(By.CSS_SELECTOR, '#noticeArea > a.NPI\=a\:notlist\,g\:zh_CN_ > strong').click()
        return NoticeListPage(self._driver)

    def get_name_main_page_title(self):
        return self._driver.title
