import feedparser
import telegram
import ssl
import json
from datetime import datetime, date, time, timedelta
import os

#bot = telegram.Bot(token='[your token]')
bot1 = telegram.Bot(token='[your token]')
ssl._create_default_https_context = ssl._create_unverified_context
rss1 = feedparser.parse("https://knvd.krcert.or.kr/rss/securityNotice.do") #보안공지
rss4 = feedparser.parse("https://knvd.krcert.or.kr/rss/patchInfo.do") #취약점패치
load = rss1.entries
load2 = rss4.entries

# 보안공지 
pj = json.dumps(load,indent=2, ensure_ascii=False)
jp = json.loads(pj)
title = jp[0]["title"]
link = jp[0]["link"]
date1 = jp[0]["published"]
date2 = datetime.strptime(date1, "%a, %d %b %Y %H:%M:%S GMT").strftime('%Y/%m/%d %H:%M:%S')
format = '%Y/%m/%d %H:%M:%S'
dt_datetime = datetime.strptime(date2,format)
kst_hour = dt_datetime + timedelta(hours=9)
print(kst_hour)
save_link=str(link)+"\n"
save_link_str=str(link)
send="제목 : "+title+"\n"+"시각 : "+str(kst_hour)+"\n"+"링크 : "+link

#취약점패치
pj2 = json.dumps(load2,indent=2, ensure_ascii=False)
jp2 = json.loads(pj2)
title2 = jp2[0]["title"]
link2 = jp2[0]["link"]
date1_2 = jp2[0]["published"]
date2_2 = datetime.strptime(date1_2, "%a, %d %b %Y %H:%M:%S GMT").strftime('%Y/%m/%d %H:%M:%S')
format2 = '%Y/%m/%d %H:%M:%S'
dt_datetime_2 = datetime.strptime(date2_2,format2)
kst_hour_2 = dt_datetime_2 + timedelta(hours=9)
print(kst_hour_2)
save_link2=str(link2)+"\n"
send2="제목 : "+title2+"\n"+"시각 : "+str(kst_hour_2)+"\n"+"링크 : "+link2
save_link2_str=str(link2)

#보안공지
with open("./test2.txt") as f2:
  if save_link_str in f2.read():
    print(save_link_str in f2.read())
  else:
    save_files2 = open("./test2.txt", "a")
    save_files2.write(save_link)
    save_files2.close
    print(send)
    #print(pj)
    #bot.sendMessage([your MessageId], send)
    bot1.sendMessage([your MessageId], send)
  
#취약점패치
with open("./test.txt") as f:
  if save_link2_str in f.read():
    print(save_link2_str in f.read())
  else:
    save_files = open("./test.txt", "a")
    save_files.write(save_link2)
    save_files.close
    print(send2)
    #print(pj2)
    #bot.sendMessage([your MessageId], send2)
    bot1.sendMessage([your MessageId], send2)
