from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def setup_driver():
    driver = webdriver.Chrome()
    return driver

def check_images(url):
    driver = setup_driver()
    driver.get(url)
    
    time.sleep(5) 
    images = driver.find_elements(By.TAG_NAME, 'img')
    num_images = len(images)
    
    extended_time = 0
    if num_images > 0:
        extended_time = 10 * num_images  
        print(f"presence time: {extended_time} seconds. {num_images} images found.")
    else:
        print("no images found")

    driver.quit()

    return extended_time

def main():
    url = input("Enter the URL: ")
    presence_time = check_images(url)

main()
