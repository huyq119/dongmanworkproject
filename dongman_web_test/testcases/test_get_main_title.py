from dongman_web_test.pagefile.main_page import MainPage


class TestGetMainTitlePage():

    def setup(self):
        self.main = MainPage()

    def test_get_main_title(self):
        result = self.main.get_main_title_name()
        print(result)
        assert '咚漫漫画官网|咚咚手指 看看漫画' == result

    def teardown(self):
        self.main.quit_page()
