from bs4 import BeautifulSoup
import requests 
import json

url = 'https://quotes.toscrape.com/'
page = requests.get(url)
file = 'data.json'
index = 'index.html'

allQuote = []
allAuthor = []
saved_file = []

soup = BeautifulSoup(page.text, 'html.parser')
Quote = soup.findAll('span', class_='text')
Author = soup.findAll('small', class_='author')

for i in Quote:
    allQuote.append(i.text)
for i in Author:
    allAuthor.append(i.text)

for i in range(len(allQuote)):
    print(f'{i + 1}. Quote: {allQuote[i]}; Author: {allAuthor[i]};')

with open(file, 'w+', encoding='utf-8') as f:
    for i in range(len(allQuote)):
        saved = {'Quote': allQuote[i], 'Author': allAuthor[i]
                     }
        saved_file.append(saved)
    json.dump(saved_file, f, indent = 4, ensure_ascii = False)

with open(index, "w+" , encoding='utf-8') as f: 
    f.write("<html><head><title>Quotes</title></head><body>\n")  
    f.write('<h1><p align="center" > <a href="https://quotes.toscrape.com/">ссылка</h1></a></p>\n') 
    f.write('<body bgcolor="#063645">\n') 
    f.write('<table cellspacing="3"  bordercolor="blue"  BGCOLOR= #c9700a border="1" align="center"') 
    f.write("<table>\n") 
    f.write("<tr>\n")
    f.write(" <td>Цитата</td>\n<td>Автор</td>\n<td>Номер</td>\n</tr>\n")
    
    with open(file, 'r', encoding='utf-8') as file_open:
        file_saved = json.load(file_open)
        for i in range(len(file_saved)):
            f.write(f"<tr>\n<th>{file_saved[i]['Quote']}</th>\n<th>{file_saved[i]['Author']}</th>\n<th>{i+1}</th>\n")
    f.write("</table>\n") 
    f.write("</body></html>")