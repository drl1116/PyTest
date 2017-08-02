# --coding:utf-8--
from selenium import webdriver
import time

driver = webdriver.Chrome()
url1 = "http://www.baidu.com/"

print("---Test Begin---")

print("get url1")
driver.get(url1)
time.sleep(1)

driver.find_element_by_id("kw").send_keys("selenium2")

time.sleep(1)

driver.find_element_by_id("su").click()

print("Print Title")
aaa = driver.title
print(aaa)

print("Browser Maxsize")
driver.maximize_window()

time.sleep(2)

print("Set Size 1366*768")
driver.set_window_size(1366, 768)

time.sleep(2)

url2 = "http://news.baidu.com/"
print("Get url2")
driver.get(url2)

print("Back to %s" % (url1))
driver.back()

time.sleep(2)

print("forward to %s" % (url2))
driver.forward()

time.sleep(5)

print("---Test Over---")

driver.quit()
