import configparser
import json
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():

    def get_config(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        config = configparser.ConfigParser()
        config.read(os.path.join(BASE_DIR, 'dongman.ini'))
        return config

    def __init__(self, _base_driver=None):
        _config = self.get_config()
        try:
            using_headless = os.environ["using_headless"]
        except KeyError:
            using_headless = None
            # print('没有配置环境变量 using_headless, 按照有界面方式运行自动化测试')
        _chrome_options = Options()
        if using_headless is not None and using_headless.lower() == 'true':
            # print('使用无界面方式运行')
            _chrome_options.add_argument("--headless")
            _chrome_options.add_argument("--disable-extensions")
            _chrome_options.add_argument("--display-gpu")
            _chrome_options.add_argument("--no-sandbox")
        _base_driver: WebDriver
        if _base_driver is None:

            # _chrome_options.add_experimental_option("w3c", False)
            self._driver = webdriver.Chrome(options=_chrome_options)
            self._driver.maximize_window()
            self._driver.implicitly_wait(4)
            # self._get_cookies_dongman()
            self._cookie_login()
        else:
            self._driver = _base_driver

    def _get_cookies_dongman(self):

        self._driver.get("https://qa.dongmanmanhua.cn/")
        above = self._driver.find_element(By.CSS_SELECTOR, "#wrap > div.youthModeFirstWin.youthModeFirstWin_01 "
                                                           "> div.FirstWinBtn")
        ActionChains(self._driver).move_to_element(above).perform()
        self._driver.find_element(By.CSS_SELECTOR, "#wrap > div.youthModeFirstWin."
                                                   "youthModeFirstWin_01 > div.FirstWinBtn "
                                                   "> a.meKnowBtn").click()

        WebDriverWait(self._driver, 5).until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, "#btnLogin")))
        self._driver.find_element(By.CSS_SELECTOR, "#btnLogin").click()
        above_login = self._driver.find_element(By.CSS_SELECTOR, "#formLogin")
        ActionChains(self._driver).move_to_element(above_login).perform()

        self._driver.find_element(By.CSS_SELECTOR, "#phoneEmailId").send_keys("13301199951")
        WebDriverWait(self._driver, 3)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys("qa123@@")
        WebDriverWait(self._driver, 3)
        self._driver.find_element(By.CSS_SELECTOR, "#layerMy > div.loginbox_cont > "
                                                   "div.sel_privacy_icon_c > "
                                                   "span.sel_privacy_btn_black.sel_privacy_btn"
                                                   ".sel_privacy_btn_null").click()
        self._driver.find_element(By.CSS_SELECTOR, "#btnLogIn").click()
        sleep(2)
        _cookies = self._driver.get_cookies()
        with open("../pagefile/cookies.json", "w") as f:
            json.dump(_cookies, f)

    def _cookie_login(self):
        self._driver.get("https://qa.dongmanmanhua.cn/")
        above_youth = self._driver.find_element(By.CSS_SELECTOR, "#wrap > div.youthModeFirstWin.youthModeFirstWin_01 "
                                                                 "> div.FirstWinBtn")
        ActionChains(self._driver).move_to_element(above_youth).perform()
        self._driver.find_element(By.CSS_SELECTOR, "#wrap > div.youthModeFirstWin."
                                                   "youthModeFirstWin_01 > div.FirstWinBtn "
                                                   "> a.meKnowBtn").click()
        WebDriverWait(self._driver, 5).until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, "#btnLogin")))
        self._driver.find_element(By.CSS_SELECTOR, "#btnLogin").click()
        with open(f"../pagefile/cookies.json", "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self._driver.add_cookie(cookie)
        self._driver.get("https://qa.dongmanmanhua.cn/")
        sleep(3)

    def find(self, by, value):
        return self._driver.find_element(by=by, value=value)

    def quit_page(self):
        self._driver.quit()
