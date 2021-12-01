import time

import pytest

from dongman_mweb_test.mwebpages.main_page import MainPage


class TestGetListNotice:

    def setup(self):
        self.main = MainPage()

    @pytest.mark.run(order=3)
    def test_get_list_notice_name(self):
        result = self.main.go_to_notice_list().get_detail_notice()
        time.sleep(4)
        print(result)
        assert result == '咚漫消息'

    def teardown(self):
        self.main.quit_page()
