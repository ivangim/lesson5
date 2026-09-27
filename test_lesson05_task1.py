from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")

    click_forms = driver.find_element(By.LINK_TEXT, "HTML Form")
    click_forms.click()
    driver.back()
    current_url = driver.current_url
    
    driver.quit()
