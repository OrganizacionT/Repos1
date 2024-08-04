from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (you might need to adjust the path to the WebDriver executable)
driver = webdriver.Safari()

# Open the HTML file in the browser
driver.get("file:///Users/carlos_cobaleda/development/visual-studio-1.65.2-workspace/Repos1/login.html")  # Adjust the path to your HTML file

# Find the username and password fields
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

# Enter credentials
time.sleep(5)
username_field.send_keys("testuser")
time.sleep(5)
password_field.send_keys("testpassword")

time.sleep(5)
# Submit the form
password_field.send_keys(Keys.RETURN)

# Add a delay to see the result
time.sleep(5)

# Close the browser
driver.quit()
