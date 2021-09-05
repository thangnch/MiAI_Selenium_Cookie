import pickle
from selenium import webdriver

# 0. Define browser
browser = webdriver.Chrome(executable_path="./chromedriver")

# 1. open Facebook
browser.get("http://facebook.com")

# 2.Load cookie from file

cookies = pickle.load(open("my_cookie.pkl","rb"))
for cookie in cookies:
    browser.add_cookie(cookie)

# 3. Refresh the browser
browser.get("http://facebook.com")