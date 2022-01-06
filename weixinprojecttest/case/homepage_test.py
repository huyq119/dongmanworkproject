# coding=utf-8


from case.base import loader
from case.base.basecase import BaseCase
from case.pages.homepage import HomePage

"""
小程序首页测试
"""


class HomePageTest(BaseCase):  
    def __init__(self, methodName='runTest'):
        super(HomePageTest, self).__init__(methodName)
        self.homePage = HomePage(self)

    """
     case1:测试首页的跳转路径是否正确，跳转路径要使用绝对路径,小程序默认进入就是首页，所以不用再切换进入的路径
    """

    def test_01_home_page_path(self):
        self.homePage.check_homepage_path()

    """
     case2:页面的基本元素是否存在
    """

    def test_02_page_base_element(self):
        self.homePage.check_homepage_base_element()


    """
    case3:检查首页的"官方补贴"模块存在
    """

    def test_03_live_sale(self):
        self.assertTexts(["官方补贴"], "view")
        self.assertTexts(["轻松赚回早餐钱"], "view")


    """
    case4:从首页点击"更多"跳转到直播特卖页面,页面包含"推荐"模块
    """

    def test_04_open_live_sale(self):
        # 点击首页的"更多"按钮的元素
        self.homePage.get_subsidy_element()
        self.page.wait_for(2)
        result = self.page.wait_for("页面元素选择器xxx")  # 等待页面渲染完成
        if result:
            category = self.page.data['categoryList']
            self.assertEquals("美食", category[0]['title'], "接口返回值包含美食模块")
            self.assertEquals("美妆", category[1]['title'], "接口返回值包含美妆模块")
            self.page.wait_for(2)
            self.app.go_home()


if __name__ == "__main__":
    loader.run(module="case.homepage_test", config="../config.json", generate_report=True)