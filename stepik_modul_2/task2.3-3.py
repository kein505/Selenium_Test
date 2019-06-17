from selenium import webdriver
import pyperclip
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

# Нажимаем кнопку
browser.find_element_by_css_selector(".btn").click()

browser.switch_to.alert.accept()

# Ваш код, который берет переменнную х и заполняет обязательные поля
x_element = browser.find_element_by_css_selector("[id='input_value']")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_css_selector("[id='answer']")
input1.send_keys(y)

browser.find_element_by_css_selector(".btn").click()

#переключаемся на выходящее сообщение (алерт) и копируем код ответа
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)
#alert.accept()

#browser.get("https://stepik.org/lesson/228249/step/8?unit=200781")
#browser.find_element_by_css_selector("again-btn white").click()
