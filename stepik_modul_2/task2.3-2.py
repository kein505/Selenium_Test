from selenium import webdriver
from os import path
import pyperclip

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

# Ваш код
for selector, keys in {'[name = "firstname"]':"Ivan", '[name = "lastname"]':"Petrov", '[name = "email"]':"test@test.ty", '[id = "file"]':path.join(path.dirname(__file__), 'file.txt')}.items():browser.find_element_by_css_selector(selector).send_keys(keys)


# Отправляем заполненную форму
browser.find_element_by_css_selector(".btn").click()

alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)
alert.accept()

browser.get("https://stepik.org/lesson/228249/step/8?unit=200781")
browser.find_element_by_css_selector("again-btn white").click()
