from selenium.webdriver import TouchActions, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from dongman_mweb_test.mwebpages.bashpage import BasePage


class ViewerPage(BasePage):

    def get_name_download_alert(self):
        # _actions = TouchActions(self._driver)
        # _actions.scroll(0, 40000).perform()
        WebDriverWait(self._driver, 10)
        self._driver.execute_script("window.scrollBy(0,40000)")
        WebDriverWait(self._driver, 5)
        above = self._driver.find_element(By.CSS_SELECTOR, "#_downloadAppPopupLayer > div.inner")
        ActionChains(self._driver).move_to_element(above).perform()
        _text = self.find(By.CSS_SELECTOR, '.download_app_text').text
        return _text
