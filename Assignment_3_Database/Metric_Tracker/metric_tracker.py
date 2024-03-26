import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pymongo
from datetime import datetime

# Initialize browser
driver = webdriver.Chrome()

# Navigate to your website 
driver.get("http://localhost:3000/")

# Try to connect to MongoDB

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["PlatformComputing"]
collection = db["UserInteractionMetrics"]
print("Connected to MongoDB")


# Track presence time 
start_time = time.time()


while True:
        current_time = time.time()
        presence_time = current_time - start_time
        print(f"Presence time: {presence_time} seconds")

        scroll_height = driver.execute_script("return document.body.scrollHeight") # track scrolling
        current_scroll = driver.execute_script("return window.pageYOffset")
        print(f"Scrolled {current_scroll}/{scroll_height} pixels")

        metrics = {
            "TIMESTAMP (HH/MM/SS)": datetime.now().strftime('%H:%M:%S'),
            "PRESENCE_TIME (SEC.)": presence_time,
            "SCROLLING (PIXELS)": current_scroll
        }

        collection.insert_one(metrics)


        if presence_time > 10:
            break

        

time.sleep(2)  # Sleep to prevent tight loop (adjust as needed)


driver.quit()
mongo_client.close()
    