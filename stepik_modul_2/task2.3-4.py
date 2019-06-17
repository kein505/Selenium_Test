from selenium import webdriver
import pyperclip
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

# Находим и Нажимаем кнопку
browser.find_element_by_css_selector("[class='trollface']").click()
#запоминание название нового окна
new_window = browser.window_handles[1]
#переключение на новое окно
browser.switch_to.window(new_window)

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