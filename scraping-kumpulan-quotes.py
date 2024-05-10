import requests
from bs4 import BeautifulSoup
from datetime import date, datetime
import csv

title = 'Quotes to Scrape'
url = 'https://quotes.toscrape.com/page/'.format(title)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'}

df = []
# isi disini mau sampe halaman ke berapa yang diambil
for page in range(1, 10):
    # koneksi ke web
    req = requests.get(url+str(page), headers=headers)

    # ubah ke format Beautiful Soup
    soup = BeautifulSoup(req.text, 'html.parser')
    quote = soup.findAll('div', 'quote')

    for i in quote:
      isi = i.find('span', 'text').text
      penulis = i.find('small', 'author').text
      tags = i.find('div', 'tags').text
      df.append([isi, penulis, tags])

# bikin header kolom file csv
column = ['quotes', 'Author', 'tags']

# tambahkan tanggal hari ini sebagai nama file
today = date.today()
file = csv.writer(open('hasil scraping.csv', 'w', newline='', encoding='utf-8'))

# overwrite file csv
file.writerow(column)
for x in df:
  file.writerow(x)