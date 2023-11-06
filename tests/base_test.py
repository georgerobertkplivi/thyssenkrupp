from seleniumbase import BaseCase


class BaseTest(BaseCase):
    base_url = "https://www.google.com/"
    # base_url = "https://www.thyssenkrupp.com/en/home"

    def setUp(self):
        super().setUp()
        self.open(self.base_url)
        self.maximize_window()

    def tearDown(self):
        self.save_teardown_screenshot()
        super().tearDown()
