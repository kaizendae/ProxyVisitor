from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import Proxies

options = webdriver.ChromeOptions()

proxies = Proxies.get_Proxies()
print(proxies)

PROXY = "36.89.181.161:50204"
options.binary_location= r"C:/Users/Heidiki/AppData/Local/Chromium/Application/chrome.exe"

options.add_argument('--proxy-server=%s' % PROXY)

driver = webdriver.Chrome("./chromedriver.exe",options = options)  # Optional argument, if not specified will search path.



driver.get("https://www.whatsmyip.org/")
