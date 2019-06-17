import math
  
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который считает сумму 2 чисел
one_element = browser.find_element_by_css_selector("[id='num1']")
value_one = one_element.text

two_element = browser.find_element_by_css_selector("[id='num2']")
value_two = two_element.text

y=int(value_one)+int(value_two)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(str(y)) # ищем элемент с текстом y


# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()