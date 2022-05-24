import time

import pytest

from dongman_mweb_test.mwebpages.main_page import MainPage


class TestGetDetailNoticeFirst:

    def setup(self):
        self.main = MainPage()

    @pytest.mark.run(order=2)
    def test_get_detail_notice_first(self):
        result = self.main.go_to_notice_first_detail().get_detail_notice()
        time.sleep(4)
        print(result)
        assert '亲爱的用户' in result

    def teardown(self):
        self.main.quit_page()
