import json
from youtube_dl import YoutubeDL
f = open("itunes.json")
itunes_chart = json.loads(f.read())

for i in itunes_chart:
    options = {
        'default_search': 'ytsearch',
        'max_downloads': 1,
        'format':'bestaudio/audio'
    }
    dl = YoutubeDL(options)
    dl.download([f"{i['Song']} {i['Artist']}"])

