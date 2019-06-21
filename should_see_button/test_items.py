'''
1. Тест в репозитории можно запустить командой pytest --language="es", тест успешно проходит.
2.Проверка работоспособности кода для разных языков. Добавьте в файл с тестом команду time.sleep(30) сразу после открытия ссылки. Запустите тест с параметром language="fr" и визуально проверьте, что фраза на кнопке добавления в корзину выглядит так: "Ajouter au panier".
3.Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
4.В тесте проверяется наличие кнопки добавления в корзину. Селектор кнопки является уникальным для проверяемой страницы.
5.Название тестового метода внутри файла test_items.py соответствует задаче. Название test_something не удовлетворяет требованиям.
'''
import time

link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_add_to_basket(browser):
	browser.get(link)
	browser.find_element_by_css_selector('[class = "btn btn-lg btn-primary btn-add-to-basket"]') #поиск кнопки
	#time.sleep(30)