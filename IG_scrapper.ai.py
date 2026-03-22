#pip install selenium requests beautifulsoup4 pandas
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# setting Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Headless mode, no browser webpage reveal
options.add_argument("--disable-gpu")  # Banned GPU
options.add_argument("--no-sandbox")  # Running in the Docker

# Create WebDriver element
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Access Instagram
driver.get("https://www.instagram.com/")

# fill in login information
username = "your_username"
password = "your_password"
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

# User URL
user_profile_url = "https://www.instagram.com/{username}/"

# User profile
driver.get(user_profile_url)
time.sleep(3)

# User photo URL and Image
photos = driver.find_elements(By.XPATH, "//div[@class='_aagv']")
for photo in photos:
    img_url = photo.find_element(By.TAG_NAME, 'img').get_attribute('src')
    caption = photo.find_element(By.XPATH, ".//following-sibling::div").text
    print(f"photo URL: {img_url}, Description: {caption}")
    
# Get posts info
posts = driver.find_elements(By.XPATH, "//div[@class='_aagv']")
for post in posts:
    post.click()
    time.sleep(3)

    # Get likes
    likes = driver.find_element(By.XPATH, "//div[@class='_aamw']").text
    print(f"点赞数: {likes}")

    # Get comments
    comments = driver.find_elements(By.XPATH, "//div[@class='_a9zc']")
    for comment in comments:
        user = comment.find_element(By.XPATH, ".//span[@class='_a9zs']").text
        text = comment.find_element(By.XPATH, ".//span").text
        print(f"评论者: {user}, 评论内容: {text}")

    # Back to last page
    driver.back()
    time.sleep(2)
    #Demostrate human behavior
    for i in range(10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

import random
# Proxy server
proxies = [
    "http://user:pass@proxy1.com",
    "http://user:pass@proxy2.com",
    "http://user:pass@proxy3.com"
]

#Randomization
proxy = {"http": random.choice(proxies)}

#Set headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# User proxy to send requests
driver.get(user_profile_url, proxies=proxy)

#Save data to CSV
import pandas as pd

data = {
    "Photo URL": [],
    "Description": [],
    "Likes": [],
    "Commenter": [],
    "Comment": []
}

data["Photo URL"].append(img_url)
data["Description"].append(caption)
data["Likes"].append(likes)
data["Commenter"].append(user)
data["Comment"].append(text)

df = pd.DataFrame(data)
df.to_csv('instagram_data.csv', index=False)