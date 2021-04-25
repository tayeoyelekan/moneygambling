import pytest
from selenium.webdriver.common.by import By
from page_objects.base_component import BasePage


class HeaderComponent(BasePage):

    def __init__(self, selenium, device="desktop", os="windows", filtering="", name=""):
        super().__init__(selenium, device)

    @property
    def _component_container(self):
        return self._selenium.find_element(By.CLASS_NAME, 'header')

    @property
    def _money_gambling_logo(self):
        return self._component_container.find_element(By.CLASS_NAME, 'logo')

    @property
    def _money_gambling_join_button(self):
        return self._component_container.find_element(By.CLASS_NAME, 'newUser')

    def click_join_button(self):
        self._money_gambling_join_button.click()

    def is_loaded(self):
        self.wait.wait_for_element_visible(value="//div[contains(@class, 'header')", time_to_wait=60)
        self.wait.wait_for_the_attribute_contain_value(self._money_gambling_logo, 'title', 'MoneyGaming', time_to_wait=30)
