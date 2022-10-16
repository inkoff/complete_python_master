from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://vk.com")

sign = browser.find_element_by_id("index_login")
sign.click()
user = browser.find_element_by_id("index_email")
user.send_keys("79200769071")
password = browser.find_element_by_id("index_pass")
password.send_keys("GloAss1987")
# print(sign)
password.submit()
# assert "Олег Колесов" in browser.page_source
while(True):
    pass
