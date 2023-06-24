#FULL PROJECT BY B_VOTSON FROM B_VOTSON TEAM
isfirst = True
textname = "Сейчас играет - "
textauthor = " .Автор: "
timebefore = 3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from tkinter import *
import asyncio
import time
from telethon.sync import TelegramClient
from telethon.tl.functions.account import *

import threading
ison = True
from idlelib.tooltip import Hovertip

# Инициализация объекта Spotipy
#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='5c2fa33e816441f68e51540561e605ae', client_secret='9fd28d95c3af45e39bce47b1844eb89d', redirect_uri='http://bvotson.byethost7.com', scope='user-read-currently-playing'))
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='YOUR-SPOTIFY-CLIENT-ID', client_secret='YOUR-SPOTIFY-CLIENT-SECRET', redirect_uri='http://bvotson.byethost7.com', scope="user-read-currently-playing"))
# Получение информации о текущем треке
current_track = sp.current_user_playing_track()

root = Tk()
def updatesettings():
    global textname
    global textauthor
    global timebefore
    textname = e4.get()
    textauthor = e5.get()
    timebefore = e3.get()
    print("SAVED SETTINGS")
def isonchange():
    global ison
    ison = not ison
#Okno nahui===================
l1 = Label(text='NRF StatusBar')
l2 = Label(text="Наведитесь для полной информации")
Hovertip(l2, '''
Скрипт B_Votson Team для Telegram на Windows.
Каждые n секунд скрипт вызывает окно с названием трека Spotify или любого другого плеера и обновляет информацию о нем в био.
''', hover_delay=100)
l3 = Label(text="Задержка обновления")
e3 = Entry()
l4 = Label(text="Текст с указанием названия")
e4 = Entry()
l5 = Label(text="Текст для указания автора")
e5 = Entry()
bupdate = Button(text="Сохранить настройки", command=updatesettings)
bison = Button(text="Включить/Выключить", command=isonchange)
l1.pack()
l2.pack()
l3.pack()
e3.pack()
l4.pack()
e4.pack()
l5.pack()
e5.pack()
bupdate.pack()
bison.pack()


#=============================

# Use your own values from my.telegram.org
api_id = 123 #CHANGE FOR YOUR  TELEGRAM APPLICATION
api_hash = 'YOUR APPLICATION HASH'
print("Nerif Project Status Bar")
# The first parameter is the .session file name (absolute paths allowed)
def setabout(name, author):
    global isfirst
    global textauthor
    global textname
    with TelegramClient('BVTelegram', api_id, api_hash) as client:
        if isfirst:
            client.send_message('me', 'Было запущено приложение Nerif Project StatusBar Beta от B_Votson Team. Все права на скрипт принадлежат B_Votson Team. Сайт: http://bvotson.byethost7.com . Сайт проекта: nerifproject.22web.org. Удачного использования.')
            isfirst = False
        client(UpdateProfileRequest(
            about = textname + name + textauthor + author
        ))
def setstandart():
    with TelegramClient('BVTelegram', api_id, api_hash) as client:
        
        client(UpdateProfileRequest(
            about = ""
        ))
def loop1():
    while True:
        global ison
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        while ison == True:
            global timebefore
            
            time.sleep(int(timebefore))
            if current_track is not None:
                name = current_track['item']['name']
                author = current_track['item']['artists'][0]['name']
                setabout(name, author)    
                print("TRACKED")
                
        setstandart()
            
        




t = threading.Thread(target=loop1, args=())
t.start()
root.mainloop()