import requests 
from bs4 import BeautifulSoup 

URL = 'https://www.amazon.com/LG-UltraFine-International-Certified-Refurbished/dp/B07D24BQBQ/ref=sr_1_3?keywords=lg+macbook+pro+display&qid=1563419236&s=gateway&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify)