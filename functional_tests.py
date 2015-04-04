from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')
page_source = browser.page_source

assert 'mini' in page_source

browser.quit()
