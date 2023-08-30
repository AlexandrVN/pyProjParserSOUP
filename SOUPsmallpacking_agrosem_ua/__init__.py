import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/115.0.0.0 Safari/537.36"
}

url = f"https://smallpacking.agrosem.ua/products"

s = requests.Session()
response = s.get(url=url, headers=headers)

# print(response)
# with open('index.html', 'w', encoding="utf-8") as file:
#     file.write(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
items = soup.find(class_='products').text

lst_items = []
str = ''

for i in items:
    if i.isdigit():
        str += i
    else:
        if str != '':
            lst_items.append(int(str))
            str = ''

lst_items.append((lst_items[1]//lst_items[0])+1)
lst_items.append(lst_items[1]%lst_items[0])
# print(lst_items)

page = lst_items[2]
# print(page)

url = f"https://smallpacking.agrosem.ua/products/?page={page}"
response = s.get(url=url, headers=headers)
# print(response)
with open('index.html', 'w', encoding="utf-8") as file:
    file.write(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find(class_='item').select("div a", class_='key ddd-truncated')
for link in links:
    print(link['href'])


