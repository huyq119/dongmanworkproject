from selenium.webdriver.common.by import By

from dongman_mweb_test.mwebpages.bashpage import BasePage
from dongman_mweb_test.mwebpages.view_page import ViewPage


class RankingPage(BasePage):

    def go_to_ranking_view(self):
        result = self.find(By.CSS_SELECTOR, '.txt_title').text
        return result

    def get_ranking_view_item_name(self):
        _element = self.find(By.CSS_SELECTOR, '#ct > div > a.leader_boar_items.cleFix.active_first'
                                              ' > div.items_content > p.tit_content')
        result = _element.text
        return result

    def go_to_ranking_view_page(self):
        _element = self.find(By.CSS_SELECTOR, '.leader_boar_items.cleFix.active_first')
        _element.click()
        return ViewPage(self._driver)

