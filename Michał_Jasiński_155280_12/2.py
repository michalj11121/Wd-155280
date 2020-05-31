from lxml import html
import requests
import pandas as pd

link = "https://boardgamegeek.com/browse/boardgame"
temp = requests.get(link)
pom = html.fromstring(temp.text)

xpath = '//*[@id="collection"]//*[@class="table-responsive"]'
table_div = pom.get_element_by_id('collection')
table = table_div.xpath('./*[@class="table-responsive"]/table')[0]


dane = []



headerRow = []
headerRank = table.xpath(".//th")[0].xpath("./a/text()")[0]
headerTitle = table.xpath(".//th")[2].xpath("./a/text()")[0]
headerGeekRating = table.xpath(".//th")[3].xpath("./a/text()")[0]
headerAvgRating = table.xpath(".//th")[4].xpath("./a/text()")[0]
headerNumVoters = table.xpath(".//th")[5].xpath("./a/text()")[0]
headerRow.append(headerRank)
headerRow.append(headerTitle)
headerRow.append(headerGeekRating)
headerRow.append(headerAvgRating)
headerRow.append(headerNumVoters)
dane.append(headerRow)



wynik = [wynik for wynik in table.xpath("./tr[@id=\"row_\"]")]
for i in wynik:
    wynikdane = []
    rank = i.xpath("./td[@class=\"collection_rank\"]/text()")[1].strip()
    title = i.xpath(".//td")[2].xpath(".//a/text()")[0]
    geekRating = i.xpath(".//td")[3].xpath("./text()")[0].strip()
    avgRating = i.xpath(".//td")[4].xpath("./text()")[0].strip()
    numVoters = i.xpath(".//td")[5].xpath("./text()")[0].strip()
    wynikdane.append(rank)
    wynikdane.append(title)
    wynikdane.append(geekRating)
    wynikdane.append(avgRating)
    wynikdane.append(numVoters)
    dane.append(wynikdane)


foo = pd.DataFrame(dane[1:], columns=dane[0])

print(foo)
