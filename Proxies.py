import requests

def save_to_text():

    url = "https://free-proxy-list.net/"
    page = requests.get(url)
    from bs4 import BeautifulSoup
    table_doc = BeautifulSoup(page.text, 'html.parser')

    with open('proxy_list.txt', 'w') as f:
        for tr in table_doc.table.find_all('tr'):
            res = tr.find_all('td')
            if len(res) > 0:
                proxy = res[0].get_text() + ":" + res[1].get_text()
                #print(proxy)
                f.write(proxy+"\n")
            """ for r in res:
                print(r.get_text()) """

def get_Proxies():
    url = "https://free-proxy-list.net/"
    page = requests.get(url)
    proxies = []
    from bs4 import BeautifulSoup
    table_doc = BeautifulSoup(page.text, 'html.parser')

    
    for tr in table_doc.table.find_all('tr'):
        res = tr.find_all('td')
        if len(res) > 0:
            proxy = res[0].get_text() + ":" + res[1].get_text()
            if is_working(proxy):
                print(proxy)
                proxies.append(proxy)
            
    return proxies

def is_working(proxy):
    try:
        print("Testing : " + proxy + ' ...')
        requests.get('http://google.com', proxies={'http': 'http://'+ proxy},timeout=2)
    except:
        print("Not Working :/")
        return False
    else:
        print("Working :)")
        return True


def Get_Proxy_File(path):
    proxy_list = list()
    with open(path) as f:
        for line in f:
            proxy_list.append(line)
        return proxy_list

