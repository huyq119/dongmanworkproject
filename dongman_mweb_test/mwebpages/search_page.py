from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from dongman_mweb_test.mwebpages.bashpage import BasePage
from dongman_mweb_test.mwebpages.view_page import ViewPage


class SearchPage(BasePage):

    def goto_viewpage(self, name):

        el = self.find(By.CSS_SELECTOR, "#searchForm > fieldset > p:nth-child(2) > input")
        el.send_keys(name)
        el.send_keys(Keys.ENTER)
        self.find(By.CSS_SELECTOR, '[id^="title_li_"]').click()

        return ViewPage(self._driver)

    def goto_viewpage_invalid(self, name):
        el = self.find(By.CSS_SELECTOR, "#searchForm > fieldset > p:nth-child(2) > input")
        el.send_keys(name)
        el.send_keys(Keys.ENTER)
        result = self.find(By.CSS_SELECTOR, '#ct > div.search_result._searchResultArea > div > p').text

        return result
