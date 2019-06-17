import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

# Ваш код, считываем значение для х
one_element = browser.find_element_by_css_selector("[id='input_value']")
x = one_element.text
y = calc(x)

#прокрутка страницы вниз на 200 пикселей
browser.execute_script("window.scrollBy(0, 200);")

# вставка посчитанного ответа уровнения в строку
input1 = browser.find_element_by_css_selector("[id='answer']:required")
input1.send_keys(y)

# изменение чекбокса в состояние "отмечено" 
option1 = browser.find_element_by_css_selector("[id='robotCheckbox']:required")
option1.click()

# изменение состояния radiobutton в состояние "активно"
option2 = browser.find_element_by_css_selector("[value='robots']")
option2.click()

#проскролить вниз и нажать кнопку
#button = browser.find_element_by_tag_name("button")
button = browser.find_element_by_css_selector("button.btn")
button.click()
