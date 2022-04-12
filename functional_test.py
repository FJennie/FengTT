from selenium import webdriver

browser = webdriver.Chrome(executable_path=r'D:\Google Driver\chromedriver.exe') # 浏览器驱动
browser.get('http://localhost:8000')

assert 'Django' in browser.title