import pytest

from dongman_mweb_test.mwebpages.main_page import MainPage


class TestGetNameNoticeFirst:

    def setup(self):
        self.main = MainPage()

    @pytest.mark.run(order=1)
    def test_get_name_notice_first(self):
        result = self.main.get_name_notice_first()
        print(result)
        assert '18部作品转为“借阅券”模式' in result

    def teardown(self):
        self.main.quit_page()
