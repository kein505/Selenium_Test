import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")


human_radio = browser.find_element_by_id("humanRule")
human_checked = human_radio.get_attribute("checked")
print("value of human radio: ", human_checked)
#assert human_checked is not None, "Human radio is not selected by default"
assert human_checked == "true", "Human radio is not selected by default"

robot_radio = browser.find_element_by_id("robotsRule")
robot_checked = robot_radio.get_attribute("value")
print("value of robotsRule: ", robot_checked)
