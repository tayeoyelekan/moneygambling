import pytest
from assertpy import assert_that
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from webdriver.custom_wait import CustomWait


class BasePage:

    def __init__(self, selenium, base_url):
        self.base_url = base_url
        self._selenium = selenium
        self._device = "desktop"
        self._os = "windows"
        self.wait = CustomWait(self._selenium)

    @property
    def _ng_app(self):
        return self._selenium.find_element(By.XPATH, '//body')

    def open(self, **kwargs):
        pass

    def set_viewport_size(self, width, height):
        window_size = self._selenium.execute_script("""
            return [window.outerWidth - window.innerWidth + arguments[0],
              window.outerHeight - window.innerHeight + arguments[1]];
            """, width, height)
        self._selenium.set_window_size(*window_size)

    def move_to_element(self,element):
        ActionChains(self._selenium).move_to_element(element).perform()

    def url_checker(self, url, timeout=30):
        while timeout > 0:
            if self._selenium.current_url.lower() == url.lower():
                break
            else:
                time.sleep(0.5)
                timeout = timeout-0.5

    def is_loaded(self, **kwargs):
        self.wait.static_wait(2)
        expected_url = self.base_url + '/' + kwargs['page_url']
        self.wait.wait_for_element_visible(value='//body', time_to_wait=10)
        self.url_checker(expected_url)
        assert_that(self._selenium.current_url).is_equal_to_ignoring_case(self.base_url + '/' + kwargs['page_url'])
