import pytest
from collections import defaultdict

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    return chrome_options

def pytest_configure(config):
    pytest.globalDict = defaultdict()
    pytest.globalDict["base_url"]="https://moneygaming.qa.gameaccount.com"
