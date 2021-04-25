from selenium.webdriver.common.by import By
from assertpy import assert_that
from page_objects.base_component import BasePage


class RegistrationComponent(BasePage):

    def __init__(self, selenium, device="desktop", os="windows", filtering="", name=""):
        super().__init__(selenium, device)

    @property
    def _component_container(self):
        return self._selenium.find_element(By.CLASS_NAME, 'container')

    @property
    def _money_gambling_title(self):
        return self._component_container.find_element(By.XPATH, "//select[@id='title']")

    @property
    def _money_gambling_fname(self):
        return self._component_container.find_element(By.XPATH, "//input[@id='forename']")

    @property
    def _money_gambling_sname(self):
        return self._component_container.find_element(By.XPATH, "//input[@name='map(lastName)']")

    @property
    def _money_gambling_checkbox(self):
        return self._component_container.find_element(By.XPATH, "//input[@name='map(terms)']")

    @property
    def _money_gambling_join(self):
        return self._component_container.find_element(By.XPATH, "//input[@id='form']")

    @property
    def _error_money_gambling_dob(self):
        return self._component_container.find_element(By.XPATH, "//label[@for='dob']")

    def enter_first_name(self,fname):
        super().move_to_element(self._money_gambling_fname)
        self._money_gambling_fname.send_keys(fname)

    def enter_surname(self,sname):
        super().move_to_element(self._money_gambling_sname)
        self._money_gambling_sname.send_keys(sname)

    def click_join_button(self):
        super().move_to_element(self._money_gambling_join)
        self._money_gambling_join.click()

    def click_money_gambling_checkbox(self):
        super().move_to_element(self._money_gambling_checkbox)
        self._money_gambling_checkbox.click()

    def select_title(self):
        super().move_to_element(self._money_gambling_title)
        self._money_gambling_title.find_elements(By.TAG_NAME,"option")[1].click()

    def validate_dob_error_message(self,validation_message):
        self.wait.wait_for_element_visible(value="//label[@for='dob']", time_to_wait=10)
        assert_that(self._error_money_gambling_dob.get_attribute('innerHTML')).is_equal_to(validation_message)

    def is_loaded(self):
        self.wait.wait_for_element_visible(value='.container', time_to_wait=60)
        self.wait.wait_for_the_attribute_contain_value(self._money_gambling_logo, 'title', 'MoneyGaming', time_to_wait=30)