from dongman_web_test.webpages.main_page import MainPage


class TestGetNoticeListName:

    def setup(self):
        self.main = MainPage()

    def test_get_notice_list_name(self):
        result = self.main.go_to_notice_list_page().get_list_name()
        print(result)
        assert '咚漫消息' in result

    def teardown(self):
        self.main.quit_page()