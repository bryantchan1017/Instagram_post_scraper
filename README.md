# This tool is for educational and personal use only. 
# Do not use it for commercial purposes, bulk data collection, or any activity that violates Instagram’s Terms of Service.
# The author is not responsible for any account or legal issues caused by misuse.

## Install requirement
pip install selenium requests beautifulsoup4 pandas webdriver-manager

## Edit login info
username = "your_instagram_username"
password = "your_instagram_password"

## Select target user
user_profile_url = "https://www.instagram.com/target_username/"

After execution, a file named instagram_data.csv will be generated in the same directory, containing:
- Photo URL
- Description (caption)
- Likes
- Commenter
- Comment content

## Important Notes
Account Risk:
Instagram prohibits automated crawling.
Using this script may result in account suspension, ban, or rate limiting.
Use a test account at your own risk.
Delay Settings:
The time.sleep() intervals simulate human behavior.
Do not shorten them excessively to avoid detection.
Element Selectors:
Instagram’s front-end class names change frequently.
If the script fails to locate elements, update the XPath or class names accordingly.
Data Logic:
The current version saves only the last post’s data by default.
You may extend the loop to store all posts.
