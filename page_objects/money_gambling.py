
from selenium.webdriver.common.by import By
from page_objects.header_components import HeaderComponent
from page_objects.registration_components import RegistrationComponent
from page_objects.base_component import BasePage


class MoneyGambling(BasePage):

    def __init__(self, selenium, base_url):
        super().__init__(selenium, base_url)

    @property
    def _main_content(self):
        return self._selenium.find_element(By.XPATH, '//main')

    def open(self, **kwargs):
        self._selenium.get('%s/%s' % (self.base_url, kwargs['page_url']))
        if self._device == 'mobile' and self._os == 'android':
            self.get_isi_controller().is_loaded()
            self.get_isi_controller().close_isi_modal()

    def get_header_component(self):
        return HeaderComponent(self._selenium)

    def get_registration_component(self):
        return RegistrationComponent(self._selenium)


class HomePage(MoneyGambling):

    def __init__(self, selenium, base_url):
        super().__init__(selenium, base_url)
        self.page_url = ''

    def open(self, **kwargs):
        super().open(page_url=self.page_url)

    def is_loaded(self, **kwargs):
        super().is_loaded(page_url=self.page_url)


class Registration(MoneyGambling):

    def __init__(self, selenium, base_url):
        super().__init__(selenium, base_url)
        self.page_url = 'sign-up.shtml'

    def open(self, **kwargs):
        super().open(page_url=self.page_url)

    def is_loaded(self, **kwargs):
        super().is_loaded(page_url=self.page_url)
