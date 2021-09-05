import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# 0. Declare the browser
browser = webdriver.Chrome(executable_path="./chromedriver")

# 1. Open faceboook
browser.get("http://facebook.com")

# 2. Truy to login

txtUser = browser.find_element_by_id("email")
txtUser.send_keys("fake_user")

txtPassword = browser.find_element_by_id("pass")
txtPassword.send_keys("fake_password")

txtPassword.send_keys(Keys.ENTER)

sleep(10)

pickle.dump(browser.get_cookies(), open("my_cookie.pkl","wb"))

browser.close()
