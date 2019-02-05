import requests
from bs4 import BeautifulSoup

URL = "https://www.wired.co.uk/article/best-shows-netflix"
r = requests.get(URL)

soup = BeautifulSoup(r.content,features = "html.parser")
table = soup.find('div',attrs={'class':'a-body__content has-bbcode'})
show = table.findAll('h2',attrs={'class':'bb-h2'})
for sh in show:
	for names in sh:
		name = sh.contents[0]
		print(name)

	



	