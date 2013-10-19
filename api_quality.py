import pyechonest
import json
import urllib2
import time
import pandas as pd



  # var get_url = "http://developer.echonest.com/api/v4/song/search?api_key=" + echonestApiKey 
  # + "&format=json&min_tempo=" + bpm + "&max_tempo=" + bpm + 
  # "&bucket=id:spotify-WW&bucket=audio_summary&bucket=tracks&sort=song_hotttnesss-desc"


num_songs = []
top_songs = []

for bpm in xrange(20, 300):
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

    # add number of songs for BPM query
    num_songs.append(len(song_list))
    
    top_songs_curr = []
    for i, song in enumerate(song_list):
        if i>9:
            break
        top_songs_curr.append(song['artist_name']+'- '+ song['title'])
        

    top_songs.append(top_songs_curr)
    print bpm
    time.sleep(4)

    song_stats = pd.DataFrame({ '#songs query' : num_songs, 'songs' : top_songs })
    song_stats.to_csv('song_queries.csv')







