from case.base.basepage import BasePage
from case.base import route


class HomePage(BasePage):
    """小程序首页公共方法"""

    locators = {
        "BASE_ELEMENT": "view",
        "BASE_BANNER": "首页banner元素选择器XXX"
    }
    # 首页点击官方补贴的"更多"按钮
    subsidy_more_button = ("跳转页面的元素选择器XXX", "更多")

    """
    校验页面路径
    """
    def check_homepage_path(self):
        self.mini.assertEqual(self.current_path(), route.homepage_route)
    """
    校验页面的基本元素
    """
    def check_homepage_base_element(self):
        # 校验页面是否包含view元素
        self.mini.assertTrue(self.mini.page.element_is_exists(HomePage.locators['BASE_ELEMENT']))
        # 校验页面banner位置
        self.mini.assertTrue(self.mini.page.element_is_exists(HomePage.locators['BASE_BANNER']))
    """
    获取官方补贴，点击"更多"按钮跳转
    """
    def get_subsidy_element(self):
        self.mini.page.get_element(str(self.subsidy_more_button[0]),
                                   inner_text=str(self.subsidy_more_button[1])).click()