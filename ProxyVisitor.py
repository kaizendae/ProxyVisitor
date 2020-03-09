import random
import Proxies
import requests
import time
from bs4 import BeautifulSoup


while True:
    proxies_list = Proxies.get_Proxies()
    print(len(proxies_list))

    #PROXY = proxies[random.randrange(0,len(proxies))]
    for PROXY in proxies_list:
        i = 0
        if Proxies.is_working(PROXY): 
            print("#####################")
            requests.get('https://www.ebay.com/itm//392707893919', proxies={'http': 'http://'+ PROXY},timeout=1)
            wait = random.randrange(30,300)
            print(" visit N:" + str(i) + " Waiting : " + str(wait))
            time.sleep(random.randrange(30,300))
            i = i+1
        if i == 5:
            time.sleep(3600)
            i = 0


