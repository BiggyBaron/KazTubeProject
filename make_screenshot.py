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
    browser.visit('https://kaztube.kz/channel/106388#video')
    cook = {'_zero_ss': '5b446d9cef619.1531211164.1531211180.2',
            'session': '426f8daf46286ce84b7e4ba79e90af2b7b6ace37%7E5b446adcd7db04-45842121',
            'authautologin': '86842e49d8dc7e689a06deb3c9e371112986dcf6%7E452a0517c4d2351780902403f1003883a057f784',
            'tmr_detect': '0%7C1531211169540', '_ym_visorc_34776220': 'w', '_ym_isad': '2',
            '_ym_d': '1531211166', '_ym_uid': '1531211166443853488', '_gid': 'GA1.2.14283550.1531211166',
            '_gat': '1', 'caltat': '0d05523f019b421ba706781964756d2c', '_ga': 'GA1.2.1801048622.1531211166',
            'PHPSESSID': 'fdtki963b0bun8f162tveeuau0', '_zero_cc': 'z5b446d9cacfc6',
            'lang': 'ca8206dbf2304957a1eb324fd0617b4d5af0d0eb%7Eru'}
    browser.cookies.add(cook)
    browser.visit('https://kaztube.kz/channel/106388#video')
    return browser


def take_screenshot(browser, ID):
    browser.visit('https://kaztube.kz/channel/106388#video')
    browser.driver.set_window_size(500, 1000)
    browser.driver.find_element_by_class_name("a").click()
    URL = str(browser.driver.current_url)
    browser.driver.save_screenshot("screens/" + ID + '.png')
    return URL

browser = browser_setup()
print(take_screenshot(browser, "123"))