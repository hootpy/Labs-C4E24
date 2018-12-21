from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel as p
from collections import OrderedDict

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
page_content = raw_data.decode("utf-8")

soup = BeautifulSoup(page_content,"html.parser")

table1 = soup.find("div", "cf_ResearchDataHistoryInfo")
title_soup = table1.find_all("td","h_t")
header = ["Nội dung"]
for i in title_soup:
    title = i.string.replace("\n","").replace("\r","")
    header.append(title)

table_content = table1.find("table", id="tableContent")
tr_list= table_content.find_all("tr")
row_list=[]
for a in tr_list:
    td_list = a.find_all("td","b_r_c",limit=5)
    td_value_list=[]
    for j in td_list:
        if str(j.string).replace("\n","").replace("\r","").replace("\xa0\xa0","") == "None":
            td_value = ""
        else:
            td_value = str(j.string).replace("\n","").replace("\r","").replace(" ","").replace("\xa0\xa0","")
        td_value_list.append(td_value)
    row_value = OrderedDict(dict(zip(header,td_value_list)))
    row_list.append(row_value)

p.save_as(records=row_list,dest_file_name="ex2.xlsx" )

