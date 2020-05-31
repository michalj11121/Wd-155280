from lxml import html
import requests

# url = "https://boardgamegeek.com/"
# data = requests.get(url)
# page = html.fromstring(data.text)
link = "https://boardgamegeek.com/"
temp = requests.get(link)
pom = html.fromstring(temp.text)

xpath = '//div[@id="results_1"]//h2//a'
wynik = pom.xpath(xpath)
for i in wynik:
    for name, value in i.items():
        if name == "href" or name == "ng-href":
            print(f"{value}")

xpath = '//div[@id="results_1"]//p//a'
wynik = pom.xpath(xpath)
for i in wynik:
    for name, value in i.items():
        if name == "href" or name == "ng-href":
            print(f"{value}")