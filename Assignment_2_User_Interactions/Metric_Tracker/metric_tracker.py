import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize browser
driver = webdriver.Chrome()

# Navigate to your website 
driver.get("http://localhost:3000/")

metrics = []
# Track presence time 
start_time = time.time()
presence_time = start_time
# while True:#presence_time < 50: # seconds
current_time = time.time()
presence_time = current_time - start_time
print(f"Presence time: {presence_time} seconds")

print()

# Track scrolling
scroll_height = driver.execute_script("return document.body.scrollHeight")  
current_scroll = driver.execute_script("return window.pageYOffset")
print(f"Scrolled {current_scroll}/{scroll_height} pixels")

print()

text_content = driver.find_element(by=By.TAG_NAME, value ="h1").text
para_content = driver.find_elements(by=By.TAG_NAME, value="p")

print("Webpage title: ", text_content)

print()

for item in para_content:
    print("Paragraph content: ", item.text)



time.sleep(2) 
    
driver.quit()