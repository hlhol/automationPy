from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# declare your username and pass in verible:
username = "username"
password = "password"

#driver of firefox
driver = webdriver.Firefox()

#open the website of moodle
driver.get("https://moodle.polytechnic.bh/moodle/login/")




