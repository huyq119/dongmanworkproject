from selenium.webdriver.common.by import By

from dongman_mweb_test.mwebpages.bashpage import BasePage


class NoticeDetailPage(BasePage):

    def get_detail_notice(self):
        _element = self.find(By.CSS_SELECTOR, '#contentsArea')
        result = _element.text
        return result
