from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
#1. Download trang
url = "https://dantri.com.vn"
#1.1 Open connection to sever
conn = urlopen(url)
#1.2 Read data
raw_data = conn.read()
#1.3 Decode data
page_content = raw_data.decode("utf-8")

# f = open("dantri.html","wb")
# f.write(raw_data)
# f.close

#2. Extract ROI
soup = BeautifulSoup(page_content, "html.parser")
ul = soup.find("ul", "ul1 ulnew")

#3. Extract data
li_list = ul.find_all("li")
news_list=[]
for li in li_list:
    a = li.a
    title = a.string
    link = url + a["href"]
    news = OrderedDict({
        "Title": title,
        "Link": link
    })
    news_list.append(news)
#4. Save data to excel
pyexcel.save_as(records=news_list,dest_file_name="news.xlsx" )

