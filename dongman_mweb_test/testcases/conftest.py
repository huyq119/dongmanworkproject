from typing import List

import pytest


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        # 用例的名字
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        # 用例的路径
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")

        if 'login' in item._nodeid:
            item.add_marker(pytest.mark.login)
    items.reverse()

