import pytest
from pytest_bdd import then, when, parsers, scenarios,given
import page_objects.money_gambling as MoneyGambling
scenarios('../feature/registration.feature',strict_gherkin=False)


@given("I am a new moneygaming.com player")
def new_money_gambler(selenium):
    selenium.maximize_window()


@given(parsers.re("I navigate to '(?P<page_name>.*)'"), converters=dict(page_name=str))
def navigate_top_page(selenium,page_name):
    base_url=pytest.globalDict["base_url"]
    page_class = getattr(MoneyGambling, page_name)
    page_class(selenium, base_url).open()


@then(parsers.re("'(?P<page_name>.*)' page is loaded"), converters=dict(page_name=str))
def url_is_loaded(selenium,page_name):
    pytest.globalDict["page_name"]=page_name
    base_url = pytest.globalDict["base_url"]
    page_class = getattr(MoneyGambling, page_name)
    page_class(selenium, base_url).is_loaded()


@given(parsers.re("'(?P<page_name>.*)' page is loaded"), converters=dict(page_name=str))
def url_loaded(selenium,page_name):
    pytest.globalDict["page_name"]=page_name
    base_url = pytest.globalDict["base_url"]
    page_class = getattr(MoneyGambling, page_name)
    page_class(selenium, base_url).is_loaded()


@when("I Click the JOIN NOW button to open the registration page")
def click_join_button(selenium):
    base_url = pytest.globalDict["base_url"]
    page_class = getattr(MoneyGambling, pytest.globalDict["page_name"])
    page_class(selenium, base_url).get_header_component().click_join_button()


@when("I Select a title value from the dropdown")
def select_title(selenium):
    base_url = pytest.globalDict["base_url"]
    page_class = getattr(MoneyGambling, pytest.globalDict["page_name"])
    page_class(selenium, base_url).get_registration_component().select_title()


@when(parsers.re("I Enter '(?P<name>.*)' in the firstname field"), converters=dict(name=str))
def enter_firstname(selenium,name):
    base_url = pytest.globalDict["base_url"]
    page_class = getattr(MoneyGambling, pytest.globalDict["page_name"])
    page_class(selenium, base_url).get_registration_component().enter_first_name(name)


@when(parsers.re("I Enter '(?P<name>.*)' in the surname field"), converters=dict(name=str))
def enter_lastname(selenium,name):
    base_url = pytest.globalDict["base_url"]
    page_class = getattr(MoneyGambling, pytest.globalDict["page_name"])
    page_class(selenium, base_url).get_registration_component().enter_surname(name)


@when("I Check the checkbox with text 'I accept the Terms and Conditions and certify that I am over the age of 18.'")
def click_checkbox(selenium):
    base_url = pytest.globalDict["base_url"]
    page_class = getattr(MoneyGambling, pytest.globalDict["page_name"])
    page_class(selenium, base_url).get_registration_component().click_money_gambling_checkbox()


@when("I Submit the form by clicking the JOIN NOW button")
def submit_form(selenium):
    base_url = pytest.globalDict["base_url"]
    page_class = getattr(MoneyGambling, pytest.globalDict["page_name"])
    page_class(selenium, base_url).get_registration_component().click_join_button()


@then(parsers.re("Validate that a validation message with text '(?P<message>.*)' appears under the date of birth box"),
      converters=dict(message=str))
def validate_message(selenium,message):
    base_url = pytest.globalDict["base_url"]
    page_class = getattr(MoneyGambling, pytest.globalDict["page_name"])
    page_class(selenium, base_url).get_registration_component().validate_dob_error_message(message)
