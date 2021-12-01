from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


from dongman_web_test.webpages.basepage import BasePage
from dongman_web_test.webpages.view_page import ViewPage


class SearchPage(BasePage):

    def goto_viewpage(self, name):
        self.find(By.CSS_SELECTOR, "#header > div > div > div.search_area._searchArea.NE\=a\:"
                                   "sch > span.input_box > input").send_keys(name)
        above_title = self.find(By.CSS_SELECTOR, "#header > div > div > "
                                                 "div.search_area._searchArea.NE\=a\:sch > ul > ul > li > a")
        ActionChains(self._driver).move_to_element(above_title).perform()
        self.find(By.CSS_SELECTOR, "#header > div > div > div.search_area._searchArea.NE"
                                   "\=a\:sch > ul > ul > li > a > p.subj > strong").click()
        return ViewPage(self._driver)
