#!/usr/bin/python
# -*- coding: utf-8

import urllib.parse
import urllib.request
import requests


proxy_file = "./proxy/proxies.txt"
with open(proxy_file, "r") as file:
    proxies = file.readlines()

# Gets html of page even if https
def get_html_with_proxy(url, proxy):

    # create the object, assign it to a variable
    proxy = urllib.request.ProxyHandler({'http': proxy})
    # construct a new opener using your proxy settings
    opener = urllib.request.build_opener(proxy)
    # install the openen on the module-level
    urllib.request.install_opener(opener)

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request(url, None, headers)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
    print("1.0.0.176:80: " + str(the_page).replace("\n", "").replace("b'", "").replace("'", ""))
