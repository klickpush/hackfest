import pyechonest
import json
import urllib2
import pandas as pd

num_songs = []
top_songs = []


  # var get_url = "http://developer.echonest.com/api/v4/song/search?api_key=" + echonestApiKey 
  # + "&format=json&min_tempo=" + bpm + "&max_tempo=" + bpm + 
  # "&bucket=id:spotify-WW&bucket=audio_summary&bucket=tracks&sort=song_hotttnesss-desc"


bpm = 135
req_str = ("http://developer.echonest.com/api/v4/song/search?api_key=PGFOUPJMLMTIHEQEX"
    "&format=json&min_tempo="+ str(bpm) +"&max_tempo="+ str(bpm) + 
    "&bucket=id:spotify-WW&bucket=audio_summary&bucket=tracks&sort=song_hotttnesss-desc")
# &results=100
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











