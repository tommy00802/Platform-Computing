import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize browser
driver = webdriver.Chrome()

# Navigate to your website 
driver.get("https://www.selenium.dev/selenium/web/web-form.html")


title = driver.title # requests browser information

driver.implicitly_wait(0.5) # this makes our program wait


text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text

# driver.quit()

while True:
   print()
