import pytest
from selenium import webdriver


@pytest.fixture()
def driver(request):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    # in order to turn off/on headless mode please comment/uncomment a line below
    options.add_argument('headless')
    options.add_argument('disable-infobars')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--verbose')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f'user-agent={user_agent}')
    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd

