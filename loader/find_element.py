import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_loaded():
    driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
    # driver.implicitly_wait(5)
    # site_loaded_false = driver.execute_script("return _siteLoaded")

    driver.get("http://svc-adveappsvc@wdc.com:2GpY9tx5FN7xx2@adve.wdc.com/Home/")

    site_loaded_false = driver.execute_async_script("return _siteLoaded")
    # site_loaded_false = driver.execute_script("return _siteLoaded")
    # driver.implicitly_wait(5)
    time.sleep(1)

    # variables in JS > home.js?@dvever=1.48
    # site_loaded_false = driver.execute_script("return _siteLoaded")
    auto_order = driver.execute_script("return _autoOrder")
    current_version = driver.execute_script("return _adveCurrentVersion")
    site_loaded_true = driver.execute_script("return _siteLoaded")

    # element in div/body
    site_loaded_div = driver.find_element(By.CLASS_NAME, '_siteLoadedDiv').is_displayed()

    # driver.implicitly_wait(5)

    print("Before Site Loaded [false]: ", site_loaded_false)

    print("Auto Order: ", auto_order)

    print("ADVE Current Version: ", current_version)

    print("_siteLoadedDiv: ", site_loaded_div)

    print("After Site Loaded [true]: ", site_loaded_true)

    # assert current_version == "?@dvever=1.43"
    # return test_site_loaded()


if __name__ == '__main__':
    test_loaded()

#pytest find_element.py --html=JS-variable.html