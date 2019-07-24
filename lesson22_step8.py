import os

from selenium import webdriver


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)

browser.find_element_by_css_selector('input[name="firstname"]').send_keys('Ivan')
browser.find_element_by_css_selector('input[name="lastname"]').send_keys('Ivanov')
browser.find_element_by_css_selector('input[name="email"]').send_keys('Ivan@ivan.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
element_upload = browser.find_element_by_css_selector('input[type="file"]')
element_upload.send_keys(file_path)

browser.find_element_by_css_selector('button.btn').click()
