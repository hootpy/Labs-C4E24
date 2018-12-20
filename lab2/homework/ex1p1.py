from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel as p
from collections import OrderedDict
import json

url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)
raw_data= conn.read()
page_content = raw_data.decode("utf-8")
soup = BeautifulSoup(page_content, "html.parser")
section = soup.find("section","section chart-grid")
ul = section.div.ul
li_list = ul.find_all("li")
itunes_chart = []
for li in li_list:
    rank = li.strong.string.replace(".","")
    a=li.a
    link= a["href"]
    h3=li.h3.a
    song = h3.string
    h4=li.h4.a
    artist = h4.string
    itunes_song=OrderedDict({
        "Rank": rank,
        "Song": song,
        "Artist": artist,
        "Link": link
    })
    itunes_chart.append(itunes_song)
    
    
p.save_as(records=itunes_chart,dest_file_name="itunes.xlsx")
with open("itunes.json","w") as text:
    text.write(json.dumps(itunes_chart))