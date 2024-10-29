import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def setup(request):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Using chrome driver manager
    chrome_service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # URL
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    request.cls.driver = driver
    yield
    driver.quit()

