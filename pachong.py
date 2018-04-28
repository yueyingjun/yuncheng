from urllib import request
from urllib.parse import *
from bs4 import BeautifulSoup as bf

import  sys


def getPages(city,job,page):
    city=quote(city)
    job=quote(job)
    url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%s&kw=%s&p=%s"%(city,job,page)
    req=request.Request(url)
    res=request.urlopen(req);
    content=res.read()
    html=content.decode("utf8");
    bfobj=bf(html,"lxml")
    arr=bfobj.select(".pagesDown li a")
    links=[]
    for item in arr:
        links.append(item.get("href"))

    return links[2:-1];

def  getInfo(pages):
    for item in pages:
        req=request.Request(item)
        res=request.urlopen(req)
        content=res.read();
        html=content.decode("utf8");
        bfobj = bf(html, "lxml")
        #找职位的信息
        jobs=bfobj.select(".zwmc div")
        jobsarr=[]
        for job in jobs:
            jobsarr.append(job.find("a"));
        # 公司名字的信息
        names=bfobj.select(".gsmc");

        namesarr=[]
        for name in names:
            namesarr.append(name.find("a"))
        #薪资的信息
        money=bfobj.select(".zwyx");
        #工作地点
        address=bfobj.select(".gzdd");

        getResult(jobsarr[1:],namesarr[1:],money[1:],address[1:])


def getResult(jobs,names,moneys,address):
    jobsinfo=[]
    for job in jobs:
        jobsinfo.append(job.text)
    namesinfo = []
    for name in names:
        namesinfo.append(name.text)
    moneyinfo = []
    for money in moneys:
        moneyinfo.append(money.text)
    addressinfo = []
    for adds in address:
        addressinfo.append(adds.text)
    print(jobsinfo)
    print(namesinfo)
    print(moneyinfo)
    print(addressinfo)




pages=getPages("太原","java",1)

getInfo(pages)


