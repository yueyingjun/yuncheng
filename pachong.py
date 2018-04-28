from urllib import request
from urllib.parse import *
from bs4 import BeautifulSoup as bf

import  sys

# 创建文件
f=open("/Users/gaoxin/Documents/job/pages/index/data.js","w",encoding="utf8")
f.write("var data=\nmodule.exports=data");
f.close();

# 读取文件
f1=open("/Users/gaoxin/Documents/job/pages/index/data.js","r",encoding="utf8");
con=f1.read()
index=(con.find("\n"))
start=con[0:index]
end=con[index:]

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

total=[]
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

    for (key,job) in enumerate(jobsinfo):
        json={
            "title":namesinfo[key],
            "job":jobsinfo[key],
            "money":moneyinfo[key],
            "address":addressinfo[key],
        }
        total.append(json)
    f2=open("/Users/gaoxin/Documents/job/pages/index/data.js","w",encoding="utf8")
    f2.write(start+str(total)+end);
    f2.close()






pages=getPages("太原","java",1)

getInfo(pages)


