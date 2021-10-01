import urllib.request, json
from datetime import date

hilfe = "https://tyrrrz.me/blog/parsing-steam-market"

#currency=3  für Euro
#beim Namen ist es egal, ob %7C oder | 

#Funktionen
def getName(url):
    name = url.split("/")
    name = name[-1]
    return name

def changeLink(url):
    name = getName(url)
    url = "https://steamcommunity.com/market/priceoverview/?appid=730&market_hash_name=" + name+"&currency=3"
    return url

def cleanName(name):
    name = name.replace("%20", "_")
    name = name.replace("%7C","|")
    return name

def getDate():
    today = date.today()
    today = today.strftime("%b-%d-%Y")
    return today

#überprüft, das Item schon mit Link abgespeichert ist, wenn nicht wird ein Eintrag angelegt
#Fehler war: json.load() macht Probleme, wenn die Datei leer oder fehlerhaft ist
def saveLink(url, name, data = {}):
    with open('links.json','r+') as f:
        data = json.load(f)
        if name not in data:
            y = {name:url}
            data.update(y)
            f.close()
        return
    
#führt Json request auf der Steam Seite aus
def getPreis(url):
    with urllib.request.urlopen(url) as link:
        data = json.loads(link.read().decode())
        return data


#legt Preis Datei an
#gibt es das Item schon
#sind schon Einträge für heute bereits angelegt?
#gibt es schon 7 Datensätze für das Item? 

def aktualisieren(name, currentItem):
    price = currentItem['lowest_price']
    dic1 = {name:{today:price}}
    with open("data.json",'r+', encoding='utf-8') as f:
        data = json.load(f)
        try:
            

        

url ="https://steamcommunity.com/market/listings/730/Glove%20Case" 
#url = input("Url eingeben: \n")


if __name__ == '__main__':
    name = getName(url)
    url = changeLink(url)
    steamItem = getPreis(url)
    name = cleanName(name)
    today = getDate()
    saveLink(url,name)
    preis = getPreis(url)
    print(preis)
    print(aktualisieren(name,steamItem))

#with open('data.json', 'w', encoding='utf-8') as f:
#    json.dump(dic1, f, ensure_ascii=False)
#    f.close()

#auslesen und speichern funktioniert für links,
#jetzt json datei für preise anlegen