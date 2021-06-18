from django.shortcuts import render

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.action_chains import ActionChains

# Create your views here.

def list_view(request):
    return render(request, "scraper1/index.html", {})


url = "https://www.nseindia.com/option-chain"
driver = webdriver.Chrome()
driver.get(url)
import time
time.sleep(5)

action = ActionChains(driver)

download = driver.find_element_by_xpath('//*[@id="downloadOCTable"]').click()
