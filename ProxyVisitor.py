from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import random
import Proxies
import requests
import time
options = webdriver.ChromeOptions()
options.binary_location= r"./chrome-win/chrome.exe"


proxies_list = Proxies.get_Proxies()

#PROXY = proxies[random.randrange(0,len(proxies))]
for PROXY in proxies_list:
    try:
        print("Testing : " + PROXY + " ...")
        requests.get('http://google.com', proxies={'http': 'http://'+ PROXY})


        options.add_argument('--proxy-server=%s' % PROXY)
        driver = webdriver.Chrome("./chromedriver.exe",options = options)  # Optional argument, if not specified will search path.

        driver.get("https://www.iplocation.net/find-ip-address")
        time.sleep(random.randrange(50,300))

        driver.close()
    except IOError:
        print("T.T / T.T / T.T ==> Proxy Not Working!")
    else:
        print("Visiting ...")

        


