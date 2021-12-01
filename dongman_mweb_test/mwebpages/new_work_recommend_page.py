from selenium.webdriver.common.by import By

from dongman_mweb_test.mwebpages.bashpage import BasePage
from dongman_mweb_test.mwebpages.view_page import ViewPage


class NewWorkRecommendPage(BasePage):

    def get_title_name(self):
        result = self.find(By.CSS_SELECTOR, '.txt_title').text
        return result

    def go_to_view_page(self):
        self.find(By.CSS_SELECTOR, '#ct > div > a:nth-child(1)').click()
        return ViewPage(self._driver)
