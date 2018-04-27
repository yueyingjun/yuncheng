from urllib import request
from urllib.parse import *
from bs4 import BeautifulSoup as bf




def finds(city,job,page):
    city = quote("北京")
    url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%s&kw=%s&p=%s" % (city, job, page)
    req=request.Request(url)
    res=request.urlopen(req)
    content=res.read()
    html=content.decode("utf8")

    bfobj=bf(html,"lxml")
    arr=bfobj.select(".zwmc div a")
    jobs=[]
    for item in arr:
        print(item.text);
        jobs.append(item.text)

    f=open(job+str(page)+".py","w")
    f.write(str(jobs));
    f.close();
finds("太原","java",1)
finds("太原","java",2)
finds("太原","java",3)
finds("太原","java",4)