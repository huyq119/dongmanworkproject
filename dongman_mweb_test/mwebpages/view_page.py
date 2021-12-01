from selenium.webdriver.common.by import By

from dongman_mweb_test.mwebpages.bashpage import BasePage
from dongman_mweb_test.mwebpages.viewer_page import ViewerPage


class ViewPage(BasePage):

    def goto_self(self):
        # title_name = self.find(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div[2]/h1').text
        title_name = self.find(By.CSS_SELECTOR, '#ct > div.detail_info > a > p.subj').text
        return title_name

    def go_to_viewer_page(self):
        self.find(By.CSS_SELECTOR, '.btn_type3').click()
        return ViewerPage(self._driver)
