import urllib.request
import re
import webbrowser

statement=input("enter a keyword\t")
statement=statement.replace(" ","+")
statement = statement.replace("play","")
statement = statement.replace("video","")
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + statement)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
webbrowser.open_new_tab("https://www.youtube.com/watch?v=" + video_ids[0])

