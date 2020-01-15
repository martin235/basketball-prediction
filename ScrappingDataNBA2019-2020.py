from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pickle
Liste1=[]
Liste2=[]
Liste3=[]
Liste5=[]
Liste6=[]
Liste7=[]
def make_soup(url):
    thepage=uReq(url)
    soupdata=soup(thepage,"html.parser")
    return soupdata

space=" "

sou=make_soup('https://www.basketball-reference.com/leagues/NBA_2020_standings.html')

container=sou.find("table",{"id":"confs_standings_E"})
for record in container.findAll('tr'):
    for data in record.findAll('a'):
        Liste2.append(data.get_text())
    for datas in record.findAll('td'):
        Liste3.append(datas.get_text())
        
containers=sou.find("table",{"id":"confs_standings_W"})
for record in containers.findAll('tr'):
    for data in record.findAll('a'):
        Liste2.append(data.get_text())
    for datas in record.findAll('td'):
        Liste3.append(datas.get_text())
        
for i in range(30,0,-1):
    del Liste3[(i*7)-1]
    del Liste3[(i*7)-4]
    
for i in range(30):
    Liste7.append(Liste2[i])
    for e in range(5):
        Liste6.append(float(Liste3[(5*i)+e]))
    Liste7.append(Liste6)
    Liste5.append(Liste7)
    Liste6=[]
    Liste7=[]

for i in range(30):
    print(Liste5[i])
    print("")
pickle_out=open("Stat2019-2020.pickle","wb")
pickle.dump(Liste5, pickle_out)
