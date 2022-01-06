import minium


@minium.ddt_class
class TestElement(minium.MiniTest):
    @classmethod
    def setUpClass(cls):
        super(TestElement, cls).setUpClass()
        cls.page = cls.app.redirect_to("")

    @minium.ddt_case(
        (".testclass", 2),
        (".child", 3),
        (".parent .child", 2),
        (".componentclass>>>.componentclass", 3),
    )
    def test_get_elements(self, args):
        [selector, number] = args
        page = self.page.get_element("page")
        elements = page.get_elements(selector, max_timeout=5)
        self.assertEqual(number, len(elements))
