from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

def check_keyword(url, keyword):
    driver = webdriver.Chrome()
    

    try:
        driver.get(url)
        time.sleep(30)

        extended_time = 0

        keyword_elements = driver.find_elements(By.TAG_NAME, "p")
        keyword_elements += driver.find_elements(By.TAG_NAME, "li") 
        keyword_elements += driver.find_elements(By.TAG_NAME, "h1")
        keyword_elements += driver.find_elements(By.TAG_NAME, "h2")
        keyword_elements += driver.find_elements(By.TAG_NAME, "h3")
        keyword_elements += driver.find_elements(By.TAG_NAME, "h4")
        keyword_elements += driver.find_elements(By.TAG_NAME, "h5")
        keyword_elements += driver.find_elements(By.TAG_NAME, "h6")


        for k in keyword_elements:
            if k.text != "":
                for word in k.text.split(" "):
                    if word.lower() == keyword.lower(): # multiple keywords in sentence
                        print("\n\nFound keyword! Extending time...")
                        print("Element:", k.text)
                        extended_time += 10
                    
        print(f"presence time: {extended_time} seconds.")
        
    finally:
        driver.quit()

url = input("Enter the URL: ")
keyword = input("Enter the keyword: ")
check_keyword(url, keyword)


