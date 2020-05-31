from bs4 import BeautifulSoup
import urllib3
import pandas as pd

dane = []
dane.append(["Title", "Platform", "Date", "Score"])
for i in range(10):
    print(f"Wczytywanie danych ({i + 1}/10)")
    link = "https://www.metacritic.com/browse/games/genre/metascore/strategy/all?view=detailed&page=" + str(i)
    temp = urllib3.PoolManager()
    pom = temp.request("GET", link)
    soup = BeautifulSoup(pom.data, 'lxml')
    for table in soup.find_all("table"):
        for tr in table.find_all("tr", class_=None):
            title = tr.find_all("td")[1].h3.text
            platform = tr.find_all("td")[1].find("div", class_="clamp-details").find_all("span")[1].text.strip()
            date = tr.find_all("td")[1].find("div", class_="clamp-details").find_all("span")[2].text
            score = tr.find_all("td")[1].find("div", class_="clamp-score-wrap").div.text
            dane.append([title, platform, date, score])

foo = pd.DataFrame(dane[1:], columns=dane[0])


top10 = foo[foo["Platform"] == "PC"].sort_values(["Score"], ascending=False).head(10)
print(top10)