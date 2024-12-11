from src.main.python.core.driver_utility.base_driver import BaseDriver


class LandingPageBaseTest:
    app = None

    def setup_class(self):
        self.app: BaseDriver = BaseDriver()
        self.app.launch()
        self.app.open_base_page()

    def teardown_class(self):
        self.app.terminate()
