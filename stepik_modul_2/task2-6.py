from selenium import webdriver
from os import path

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

# Ваш код
for selector, keys in {'[name = "firstname"]':"Ivan", '[name = "lastname"]':"Petrov", '[name = "email"]':"test@test.ty", '[id = "file"]':path.join(path.dirname(__file__), 'file.txt')}.items():browser.find_element_by_css_selector(selector).send_keys(keys)

# получаем путь к директории текущего исполняемого файла 
#current_dir = os.path.abspath(os.path.dirname(__file__))  
# добавляем к этому пути имя файла
#file_path = os.path.join(current_dir, 'file.txt')  
#находим кнопку выбора файла
#element = browser.find_element_by_css_selector("[id='file']:required") 
#передаем файл на отправку
#element.send_keys(file_path)

# Отправляем заполненную форму
browser.find_element_by_css_selector(".btn").click()

