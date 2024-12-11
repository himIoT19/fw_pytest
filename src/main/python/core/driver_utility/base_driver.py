import os
import shutil
import sys

import pytest
from selenium.webdriver.chrome.service import Service
from seleniumbase import BaseCase
from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as CS
from selenium.webdriver.firefox.service import Service as FS
from selenium.webdriver.chromium.service import ChromiumService as ES
from src.main.python.core.common_lib.util.common import singleton


@singleton
class BaseDriver:
    base_url = "https://opensource-demo.orangehrmlive.com/"

    def __init__(self):
        self._wait_timeout = 300
        self.frontend = BaseCase()
        pytest.app_frontend = self.frontend

    def launch(self):
        """
        Launch the driver
        :return:
        """
        # options = ChromeOptions()
        driver_managers = {
            'firefox': GeckoDriverManager,
            'edge': EdgeChromiumDriverManager,
            'chrome': ChromeDriverManager  # Default to Chrome if an empty string or unknown browser is provided
        }
        driver_manager_class = driver_managers.get("chrome", ChromeDriverManager)
        base_path = driver_manager_class().install()
        # Replace the incorrect file name with the ChromeDriver executable
        driver_path = os.path.join(os.path.dirname(base_path), 'chromedriver')
        print(driver_path)
        services = {
            'firefox': FS,
            'edge': ES,
            'chrome': CS  # Default to Chrome if an empty string or unknown browser is provided
        }
        svc = services.get("chrome", CS)
        service = svc(executable_path=driver_path)

        # Get the path to the virtual environment
        venv_path = sys.prefix
        if os.name == 'posix':
            path_venv_scripts = f"{venv_path}/bin"
        else:
            driver_path = driver_path.replace('/', '\\')
            path_venv_scripts = f"{venv_path}/Scripts"

        # Copy the chromedriver executable to the destination folder
        try:
            shutil.copy(driver_path, path_venv_scripts)
        except FileNotFoundError as e:
            print(f"Error : {e}")

        # return service, path_venv_scripts

        # self.frontend.driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Overriding the Seleniumbase get_new_driver method to invoke application
        # self.frontend.get_new_driver = lambda *args, **kwargs: self.frontend
        self.frontend.setUp()

    def open_base_page(self):
        self.frontend.get(self.base_url)

    def terminate(self):
        """
        Kill the app and driver
        :return:
        """
        if self.frontend.driver:
            self.frontend.driver.quit()
