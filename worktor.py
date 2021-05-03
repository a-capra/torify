#!/usr/bin/env python

import requests

#proxies = { 'http': 'socks5://127.0.0.1:9050',
#            'https': 'socks5://127.0.0.1:9050' }
proxies = { 'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050' }
# Note the extra h stands for hostname resolution

def anon_request(url):
    print(requests.get(url, proxies=proxies).text)


from stem import Signal
from stem.control import Controller

def new_identity():
    with Controller.from_port(port = 9051) as c:
        c.authenticate(password="tor4me.p")
        c.signal(Signal.NEWNYM)
    #print(anon_request(url))



if __name__=='__main__':

    URLs=['https://ident.me','https://api.ipify.org','http://httpbin.org/ip','https://ifconfig.me']

    for i,url in enumerate(URLs):
        print(url)
        print(requests.get(url).text)
        anon_request(url)
        print('')

    print('=== nc ===')
    new_identity()
    print('==========')

    for i,url in enumerate(URLs):
        print(url)
        print(requests.get(url).text)
        anon_request(url)
        print('')
   

