from selenium.webdriver.common.by import By

from dongman_web_test.pagefile.basepage import BasePage


class ViewPage(BasePage):

    def goto_self(self):
        # title_name = self.find(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div[2]/h1').text
        title_name = self.find(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div[2]/h1').text
        return title_name
