#!/usr/bin/env python3
import minium, os


class AppTest(minium.MiniTest):
    def test_screen_shot(self):
        output_path = os.path.join(os.path.dirname(__file__), "outputs/test_screen_shot.png")
        if not os.path.isdir(os.path.dirname(output_path)):
            os.mkdir(os.path.dirname(output_path))
        if os.path.isfile(output_path):
            os.remove(output_path)
        ret = self.app.screen_shot(output_path)
        self.assertTrue(os.path.isfile(output_path))
        os.remove(output_path)
