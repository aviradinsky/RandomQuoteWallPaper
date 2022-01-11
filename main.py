from PIL import Image, ImageDraw, ImageFont
from random import randint
from time import sleep
from pathlib import Path

import ctypes
import os

def change_wallpaper_windows(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(path) , 0)

def get_quote(n = 0):
    import feedparser
    feed_url = "https://www.brainyquote.com/link/quotebr.rss"
    blog_feed = feedparser.parse(feed_url)
    author = blog_feed['entries'][n]['title']
    quote = blog_feed['entries'][n]['summary']
    return author, quote

def get_system_screen_size():
    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

print("getting quote...")
author, quote= get_quote(randint(0, 3))
msg = f'{quote}\n{author}'

print("creating image...")
W, H = get_system_screen_size()
im = Image.new("RGB",(W,H),"black")
draw = ImageDraw.Draw(im)
draw.textsize(msg)
w, h = draw.textsize(msg)
draw.text(((W-w)/2,(H-h)/2), msg, fill="white")
im.save(Path.home()/'image.png',"PNG")

print("setting new wallpaper...")
change_wallpaper_windows(Path.home()/'image.png')

print('removing stored file...')
# for some reason if I dont sleep the wallpaper wont change
sleep(1)
os.remove(Path.home()/'image.png')

print("done")