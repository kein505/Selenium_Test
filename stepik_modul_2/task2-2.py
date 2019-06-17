import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
from selenium import webdriver

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
x_element = browser.find_element_by_css_selector("[id='treasure']")
value_x = x_element.get_attribute("valuex")
y = calc(value_x)

input1 = browser.find_element_by_css_selector("[id='answer']:required")
input1.send_keys(y)

option1 = browser.find_element_by_css_selector("[id='robotCheckbox']:required")
option1.click()

option2 = browser.find_element_by_css_selector("[value='robots']")
option2.click()


# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()