# -*- coding: utf-8 -*-
from selenium import webdriver
import time

dr = webdriver.Chrome()
time.sleep(2)

dr.quit()
