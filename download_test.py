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


if __name__ == "__main__":
    print(download_by_id())
    print(download_by_id("pnP5kFcKLT8"))

