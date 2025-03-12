from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 
driver = webdriver.Chrome()
driver.get("https://www.youtube.com")

# Wait for page to load
time.sleep(3)

# Search for ""
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Mehbooba mehbooba")
search_box.send_keys(Keys.RETURN)
driver.maximize_window()
# Wait for results to load
time.sleep(3)

# # Click on the first video
video = driver.find_element(By.CSS_SELECTOR, "ytd-video-renderer a#thumbnail")
video.click()

# # Close the browser after some time
time.sleep(15)
# driver.quit()