from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
time.sleep(5)
browser.save_screenshot("dom.png")

browser.get("https://ru.wikipedia.org/wiki/Selenium")
time.sleep(3)
browser.save_screenshot("selenium.png")
browser.refresh()