#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Bauyrzhan Ospan"
__copyright__ = "Copyright 2018, KazTube"
__version__ = "1.0.1"
__maintainer__ = "Bauyrzhan Ospan"
__email__ = "bospan@cleverest.tech"
__status__ = "Development"

from pytube import YouTube
import urllib.parse
import urllib.request
import requests
from splinter import Browser
import time
import os
import datetime
import telepot
from tqdm import tqdm
import sys
import pprint


## PART OF KAZTUBE UPLOAD
def browser_setup():
    if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        path = "./driver/chromedriverL"
    elif sys.platform.startswith('darwin'):
        path = "./driver/chromedriver"
    else:
        raise EnvironmentError('Unsupported platform')
    executable_path = {'executable_path': path}
    browser = Browser('chrome', **executable_path)
    browser.visit('https://kaztube.kz/channel/106400#video')
    cook = {'_zero_ss': '5b45fb6412be6.1531312997.1531313065.3',
            'videoupload': '0',
            'session': 'c42ae64a9a108f3505b4ad7db74992f7e2925326%7E5b45f8d0ba1a50-62683378',
            'tmr_detect': '0%7C1531313069707',
            'authautologin': 'a73b00d33d674f693a7a220f3eb71e89150bbe90%7Eb2b4a452a0a9e9249e846502f32c046b995def18',
            '_ym_visorc_34776220': 'w', '_ym_isad': '2', '_ym_d': '1531313010',
            '_ym_uid': '1531313010855525134', 'caltat': 'fe2024955f58487586a65dac537a7b75',
            'musicupload': '0', '_ga': 'GA1.2.1435365124.1531313009', '_gid': 'GA1.2.1262335672.1531313009',
            'PHPSESSID': '0p8s6dpqc8uqmjtf0ibkh8a4j6', '_zero_cc': 'z5b45fb65c1c9b',
            'lang': 'ca8206dbf2304957a1eb324fd0617b4d5af0d0eb%7Eru'}

    browser.cookies.add(cook)
    browser.visit('https://kaztube.kz/channel/106400#video')
    x = input("Enter: ")
    return browser


def save_cook():
    if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        path = "./driver/chromedriverL"
    elif sys.platform.startswith('darwin'):
        path = "./driver/chromedriver"
    else:
        raise EnvironmentError('Unsupported platform')
    executable_path = {'executable_path': path}
    browser = Browser('chrome', **executable_path)
    browser.visit('https://kaztube.kz/')
    x = input("Enter: ")
    print(browser.cookies.all())
    x = input("Enter again: ")


browser_setup()
