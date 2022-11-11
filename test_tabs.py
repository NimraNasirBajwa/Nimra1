import pytest
from selenium import webdriver
class TestMultiplepage:
    @pytest.fixture()
    def test_setUp(self):
        global urlnew , driver
        urlnew = "https://q-host.togee.io/"
        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
        driver.get("https://q-host.togee.io/")
        yield
        print("Okay!")
        driver.close()

    def test_tabs(self, test_setUp):
        for i in range(25):
            driver.switch_to.new_window('tab')
            driver.get(urlnew)
            if i == 25:
                break
        for y in range(5):
            global  driver1
            driver1= webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
            driver1.get(urlnew)
            for x in range(25):
                driver1.switch_to.new_window('tab')
                driver1.get(urlnew)
                if y == 5:
                    break
