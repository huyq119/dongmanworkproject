from dongman_web_test.pagefile.main_page import MainPage


class TestGetNameNoticeFirst():

    def setup(self):
        self.main = MainPage()

    def test_get_name_notice_first(self):
        result = self.main.get_name_notice_first()
        print(result)
        assert '5周年感恩回馈' in result

    def teardown(self):
        self.main.quit_page()