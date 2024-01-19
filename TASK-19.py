'''Visit the URL https://www.saucedemo.com/ and login with the following
credentials:

Username: standard_user
Password: standard_user

Try to fetch the following using Python Selenium:
1) Title of the webpage
2) Current URL of the webpage
3) Extract the entire contents of the webpage and save it in a Text file
whose name will be "Webpage_task_11.txt"'''

from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new Chrome browser instance
driver=webdriver.Chrome()

# Open the URL
driver.get("https://www.saucedemo.com/")

#Maximize the window
driver.maximize_window()

# Login
driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("standard_user")
driver.find_element(By.XPATH,"//input[@id='login-button']").click()

# Fetch and print the title of the webpage
print("Title of the webpage is: ",driver.title)

# Fetch and print the current URL of the webpage
print("Current URL of the webpage is: ",driver.current_url)

# Extract the entire webpage's contents
webpage_contents = driver.page_source

# Create and write the contents to a text file
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(webpage_contents)

# Close the browser
driver.quit()