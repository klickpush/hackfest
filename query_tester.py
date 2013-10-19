import pyechonest
import json
import urllib2
import pandas as pd

num_songs = []
top_songs = []


bpm = 80
req_str = ("http://developer.echonest.com/api/v4/song/search?api_key=PGFOUPJMLMTIHEQEX"
    "&format=json&bucket=tracks&bucket=audio_summary&bucket=id:spotify-WW"
    "&min_tempo="+ str(bpm) +"&max_tempo="+ str(bpm) + "&sort=song_hotttnesss-desc&results=100")
req = urllib2.Request(req_str)
opener = urllib2.build_opener()
f = opener.open(req)
str_json = f.read()
hash = json.loads(str_json)
song_list = hash['response']['songs']

print '# songs: ', len(song_list)
for i, song in enumerate(song_list):
    if i>9:
        break
    print i+1,') ', song['artist_name'],'- ', song['title']











