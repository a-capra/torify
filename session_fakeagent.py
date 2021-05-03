#!/usr/bin/env python

import requests
import time
from stem import Signal
from stem.control import Controller
from fake_useragent import UserAgent

def get_current_ip():
    session = requests.session()

    # it may be useful to change the user-agent,
    # which betrays our identity to the server.
    session.headers = { 'User-Agent': UserAgent().random }
    
    # TO Request URL with SOCKS over TOR
    session.proxies = {}
    session.proxies['http']='socks5h://localhost:9050'
    session.proxies['https']='socks5h://localhost:9050'

    try:
        r = session.get('http://httpbin.org/ip')
    except Exception as e:
        print(str(e))
    else:
        return r.text


def renew_tor_ip():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="tor4me.p")
        controller.signal(Signal.NEWNYM)


if __name__ == "__main__":
    print(get_current_ip())
    #time.sleep(1)
    #renew_tor_ip()
    #print(get_current_ip())
    
