import pytest
from collections import defaultdict

@pytest.fixture
def chrome_options(chrome_options):
    return chrome_options

def pytest_configure(config):
    pytest.globalDict = defaultdict()
    pytest.globalDict["base_url"]="https://moneygaming.qa.gameaccount.com"
