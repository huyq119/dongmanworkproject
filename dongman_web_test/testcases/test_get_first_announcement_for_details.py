from dongman_web_test.webpages.main_page import MainPage


class TestGetContentNoticeDetailFirst:
    def setup(self):
        self.main = MainPage()

    def test_get_content_notice_detail_first(self):
        result = self.main.go_to_notice_first_detail().get_content_notice_detail()
        print(result)
        assert '亲爱的咚粉' in result

    def teardown(self):
        self.main.quit_page()
