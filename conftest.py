import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(2)
    yield driver
    driver.quit()