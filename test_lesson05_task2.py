from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")


    input_text = driver.find_element(By.NAME, "custname")
    input_text.send_keys("Ivan")

    current_url = driver.current_url

    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()


    assert current_url != driver.current_url


# Ваш код здесь

    driver.quit()