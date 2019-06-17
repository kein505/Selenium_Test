from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pyperclip
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока сообщение не станет =10000 кнопка не станет кликабельной

button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element ((By.ID, "price"), "10000"))
browser.find_element_by_css_selector("[id='book']").click()

# Ваш код, который берет переменнную х и заполняет обязательные поля
x_element = browser.find_element_by_css_selector("[id='input_value']")
x = x_element.text
y = calc(x)

# вставляем ответ в поле посчитанного уравнения
browser.find_element_by_css_selector("[id='answer']").send_keys(y)
# ищем и нажимаем кнопку
browser.find_element_by_css_selector("[id='solve']").click()
#переключаемся на выходящее сообщение (алерт) и копируем код ответа
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)