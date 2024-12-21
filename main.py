from bs4 import BeautifulSoup
import requests 
import json

url = 'https://quotes.toscrape.com/'
page = requests.get(url)
file = 'data.json'
index = 'index.html'

allquote = []
allauthor = []
saved_file = []

soup = BeautifulSoup(page.text, 'html.parser')
quote = soup.findAll('span', class_='text')
author = soup.findAll('small', class_='author')

for i in quote:
    allquote.append(i.text)
for i in author:
    allauthor.append(i.text)

for i in range(len(allquote)):
    print(f'{i + 1}. quote: {allquote[i]}; author: {allauthor[i]};')

with open(file, 'w+', encoding='utf-8') as f:
    for i in range(len(allquote)):
        saved = {'quote': allquote[i], 'author': allauthor[i]}
        saved_file.append(saved)
    json.dump(saved_file, f, indent=4, ensure_ascii=False)

html_content = """
<html>
<head>
    <title>quotes</title>
</head>
<body bgcolor="#063645">
    <h1><p align="center"><a href="https://quotes.toscrape.com/">ссылка</a></p></h1>
    <table cellspacing="3" bordercolor="blue" bgcolor="#c9700a" border="1" align="center">
        <tr>
            <td>Цитата</td>
            <td>Автор</td>
            <td>Номер</td>
        </tr>
"""

with open(file, 'r', encoding='utf-8') as file_open:
    file_saved = json.load(file_open)
    for i in range(len(file_saved)):
        html_content += f"""
        <tr>
            <th>{file_saved[i]['quote']}</th>
            <th>{file_saved[i]['author']}</th>
            <th>{i + 1}</th>
        </tr>
        """

html_content += """
    </table>
</body>
</html>
"""

with open(index, "w+", encoding='utf-8') as f:
    f.write(html_content)
