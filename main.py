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
from pyvirtualdisplay import Display
import pyvirtualdisplay


# Send message (msg) to users in the list (ids)
def send_tlg_msg(msg):
    ids = [274271705, 257169998]
    bot = telepot.Bot('565363614:AAEVkX8AY1xbYChVpfLivdGsm_mLZnWFhPQ')
    for id in ids:
        bot.sendMessage(str(id), str(msg))


## PART OF KAZTUBE UPLOAD
def browser_setup():
    display = Display(visible=0, size=(800, 600))
    display.start()
    # if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    #     path = "./driver/chromedriverL"
    # elif sys.platform.startswith('darwin'):
    #     path = "./driver/chromedriver"
    # else:
    #     raise EnvironmentError('Unsupported platform')
    # executable_path = {'executable_path': path}
    browser = Browser('firefox', headless=True)
    browser.visit('https://add2.kaztube.kz/')
    cook = {'_zero_ss': '5b446d9cef619.1531211164.1531211180.2',
            'session': '426f8daf46286ce84b7e4ba79e90af2b7b6ace37%7E5b446adcd7db04-45842121',
            'authautologin': '86842e49d8dc7e689a06deb3c9e371112986dcf6%7E452a0517c4d2351780902403f1003883a057f784',
            'tmr_detect': '0%7C1531211169540', '_ym_visorc_34776220': 'w', '_ym_isad': '2',
            '_ym_d': '1531211166', '_ym_uid': '1531211166443853488', '_gid': 'GA1.2.14283550.1531211166',
            '_gat': '1', 'caltat': '0d05523f019b421ba706781964756d2c', '_ga': 'GA1.2.1801048622.1531211166',
            'PHPSESSID': 'fdtki963b0bun8f162tveeuau0', '_zero_cc': 'z5b446d9cacfc6',
            'lang': 'ca8206dbf2304957a1eb324fd0617b4d5af0d0eb%7Eru'}
    browser.cookies.add(cook)
    browser.visit('https://add2.kaztube.kz/')
    return browser


def kaztube_upload(browser, desc, tags, name, video):
    browser.visit('https://add2.kaztube.kz/')
    browser.driver.find_element_by_xpath("//input[@type='file']").send_keys(os.getcwd() + video)
    browser.fill("title", name)
    browser.fill("tags", tags)
    browser.select("category_id", "19")
    browser.find_by_css('.st_textarea')[0].fill(desc)
    while 1:
        try:
            time.sleep(120)
            browser.find_by_css(".inputtubmit")[0].click()
            time.sleep(10)
            break
        except:
            time.sleep(10)


def save_log(name, desc, tags, original):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    printik = "\n====================\nНазвание: " + str(name) + \
              "\nДата: " + date + "\nОписание: " + desc + "\nТэги: " + \
              tags + "\nОригинал: https://www.youtube.com/watch?v=" + original
    with open("log.txt", "a") as file:
        file.write(printik)
    try:
        with open("log" + date + ".txt", "a") as file:
            file.write(printik)
    except:
        with open("log" + date + ".txt", "w") as file:
            file.write(date)
            file.write("\n")
            file.write(printik)
##


# Gets video data fully with description and tags
def get_video_desc(ID):
    req = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id=" + ID + \
          "&key=AIzaSyCLzxcZG4DaOvgJ8AKRMqvMNbVJAx1Mce8"
    r = requests.get(req)
    description = str(r.json()["items"][0]["snippet"]["description"])
    try:
        tags = r.json()["items"][0]["snippet"]["tags"]
    except:
        tags = None
    return description, tags


# Gets html of page even if https
def get_html(url='http://www.youtube.com'):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request(url, None, headers)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
    print(the_page)


# Makes video list by ID
def get_video_list(ID='UC8M5YVWQan_3Elm-URehz9w'):
    req = "https://www.googleapis.com/youtube/v3/search?" \
          "key=AIzaSyCLzxcZG4DaOvgJ8AKRMqvMNbVJAx1Mce8" \
          "&channelId=" + ID + \
          "&part=snippet,id&order=date&maxResults=10"
    r = requests.get(req)

    videos = []
    for el in r.json()["items"]:
        try:
            name = el["snippet"]["title"]
            id = el["id"]["videoId"]
            date = str(el["snippet"]["publishedAt"]).split("T")[0]
            description, tags = get_video_desc(id)
            video = {"name": name, "id": id, "date": date, "description": description, "tags": tags}
            videos.append(video)
        except:
            pass
    return videos


# Download video by ID
def download_by_id(ID="lxMZ7VqV_KE"):
    try:
        yt = YouTube('https://www.youtube.com/watch?v=' + ID)
        stream = yt.streams.first()
        stream.download('./videos/',  filename=ID)
        if yt.streams.filter(only_audio=True).first():
            yt.streams.filter(only_audio=True).first().download('./audios/',  filename=ID)
            namA = os.listdir("./audios/")
            audiofile = str("/audios/" + namA[0])
        else:
            audiofile = None
        name = os.listdir("./videos/")
        videofile = str("/videos/" + name[0])
        return [videofile, audiofile]
    except:
        pass


# Take ScreenSHOT
def take_screenshot(browser, ID ):
    browser.visit('https://kaztube.kz/channel/106388')
    browser.driver.set_window_size(500, 1000)
    browser.driver.find_element_by_class_name("a").click()
    URL = str(browser.driver.current_url)
    browser.driver.save_screenshot("screens/" + ID + '.png')
    ids = [274271705, 257169998]
    bot = telepot.Bot('565363614:AAEVkX8AY1xbYChVpfLivdGsm_mLZnWFhPQ')
    text = "URL: " + URL + "\nID: " + ID
    for id in ids:
        bot.sendPhoto(str(id), open("./screens/" + ID + ".png", "rb"), caption=text)
    os.remove("./screens/" + ID + '.png')
    return URL


# Create list of videos from channels list txt for today
def create_list():
    with open("channels_list.txt", "r") as file:
        names = file.readlines()
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    videos = []
    for name in tqdm(names):
        video = get_video_list(name.replace("\n", ""))
        for vid in video:
            # if vid["date"] == now:
            videos.append(vid)
    return videos


def main():
    browser = browser_setup()
    print("Browser is setup")
    videos = create_list()
    print("List of " + str(len(videos)) + " is created")
    len4ik = 0
    audio4ik = 0
    for video in tqdm(videos):
        try:
            [vid, aud] = download_by_id(video["id"])
            tags = ""
            for tag in video["tags"]:
                tags = tags + str(tag) + ", "
            kaztube_upload(browser, video["description"], tags, video["name"], vid)
            save_log(video["name"], video["description"], tags, video["id"])
            take_screenshot(browser, str(video["id"]))
            os.remove("." + vid)
            len4ik = len4ik + 1
            if aud:
                kaztube_upload(browser, video["description"], tags, video["name"], aud)
                save_log(video["name"], video["description"], tags, video["id"])
                take_screenshot(browser, str(video["id"]))
                os.remove("." + aud)
                audio4ik = audio4ik + 1
        except:
            pass
    send_tlg_msg(str(len4ik) + " videos uploaded, check log file")
    send_tlg_msg(str(audio4ik) + " audios uploaded, check log file")
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    bot = telepot.Bot('565363614:AAEVkX8AY1xbYChVpfLivdGsm_mLZnWFhPQ')
    bot.sendDocument(274271705, open("log" + str(date) + ".txt", 'rb'))
    bot.sendDocument(257169998, open("log" + str(date) + ".txt", 'rb'))


if __name__ == "__main__":
    main()

