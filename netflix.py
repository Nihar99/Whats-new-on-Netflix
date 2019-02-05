import requests
from bs4 import BeautifulSoup

URL = "https://www.radiotimes.com/news/on-demand/2019-02-05/best-tv-shows-netflix/"
r = requests.get(URL)

result = []
soup = BeautifulSoup(r.content,features = "html.parser")
table = soup.find('div',attrs={'class':'template-article__main-content'})
show = table.findAll('h2')
for sh in show:
	for names in sh:
		name = sh.contents[0]
		print(name)




		




