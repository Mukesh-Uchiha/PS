import re
import urllib.request
import vlc 
import time
import pafy
import webbrowser
import requests
import shutil
import youtube_dl
import multiprocessing
import os
from os import walk
from playsound import playsound 
from pytube import YouTube
from moviepy.editor import *
from pydub import AudioSegment
from pydub.playback import play

statement = input("enter the name")
statement = statement.replace("play ","")
statement = statement.replace("song ","")
song_name = statement
statement = statement.replace(" ","+")
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + statement)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
video_ids = video_ids[0]
print(video_ids)
url="https://www.youtube.com/watch?v=" + video_ids
print(url) 
song = pafy.new(url)


best = song.getbest()
filename = best.download(filepath="/Song/Song." + best.extension)

mp4_file = r'Song/Song.mp4'
mp3_file = r'Song/Song.mp3'

videoclip = VideoFileClip(mp4_file)
audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)
audioclip.close()
videoclip.close()
APP_FOLDER = 'Song/'
totalFiles = 0
totalDir = 0
for base, dirs, files in os.walk(APP_FOLDER):
    print('Searching in : ',base)
    for directories in dirs:
        totalDir += 1
    for Files in files:
        totalFiles += 1

print('Total number of files',totalFiles)
files = totalFiles



if (files == 2):
    if __name__ == "__main__":     

        p = multiprocessing.Process(target=playsound, args=("Song/Song.mp3",))
        p.start()
        enter=input("press enter")
        if enter =="":
            print("Pressed Enter")
            p.terminate()
        else:
            p.run()    
        p.join()
        dir = 'Song/'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

'''
vlc_instance  = vlc.Instance()
player = vlc_instance.media_player_new()
Media = vlc_instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()
time.sleep(0.5)
'''
'''video=pafy.new(url)
best = video.getbestaudio()
playurl = best.url
Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()
'''
