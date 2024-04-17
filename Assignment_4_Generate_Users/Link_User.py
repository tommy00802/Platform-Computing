import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def check_links(url):
    driver = webdriver.Chrome()

    try:
        driver.get(url)

        links = driver.find_elements(By.TAG_NAME, "a")

        clickable_links = [link for link in links if link.get_attribute('href')]

        extended_time = 0

        if clickable_links:
            for link in clickable_links:
                extended_time+=10
            print(f"Found {len(clickable_links)} clickable links on {url}. Extended time: {extended_time}")
        else:
            print(f"No clickable links found on {url}.")

    except NoSuchElementException:
        print(f"No links at all on {url}.")
        driver.quit()


url = input("Enter the URL: ")
check_links(url)



