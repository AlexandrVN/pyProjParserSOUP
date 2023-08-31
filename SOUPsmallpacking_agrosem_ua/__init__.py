import requests
from bs4 import BeautifulSoup


# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
#     Chrome/115.0.0.0 Safari/537.36"
# }
#
# page = 1
# url = f'https://smallpacking.agrosem.ua/products/?page={page}'
#
# s = requests.Session()
# response = s.get(url=url, headers=headers)
#
# # print(response)
# # with open('index.html', 'w', encoding="utf-8") as file:
# #     file.write(response.text)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# items = soup.find(class_='products').text
#
# lst_items = []
# str = ''
#
# for i in items:
#     if i.isdigit():
#         str += i
#     else:
#         if str != '':
#             lst_items.append(int(str))
#             str = ''
#
# lst_items.append((lst_items[1]//lst_items[0])+1)
# lst_items.append(lst_items[1]%lst_items[0])
# # print(lst_items)
#
# page_end = lst_items[2]
# print(page_end)
#
# response = s.get(url=url, headers=headers)
# # print(response)
# with open('index.html', 'w', encoding="utf-8") as file:
#     file.write(response.text)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# links = soup.find(attrs={"class":"info"}).select("div a")
# for link in links:
#     a = link['href']
#     print(a)

def get_url(page=1):
    url = f'https://smallpacking.agrosem.ua/products/?page={page}'

    return url
def get_page(url):
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/115.0.0.0 Safari/537.36"
    }
    s = requests.Session()
    response = s.get(url=url, headers=headers)
    s.close()

    # soup = BeautifulSoup(response.text, 'html.parser')

    return response

soup = BeautifulSoup(get_page(get_url(page=1)).text, 'html.parser')

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

lst_items.append((lst_items[1] // lst_items[0]) + 1)
lst_items.append(lst_items[1] % lst_items[0])
# print(lst_items)

page_end = lst_items[2]
# print(page_end)

for i in range(2, 0, -1):
    # link = get_url(i + 1)
    # print(link)
    # links = get_page(link)
    # print(links)
    # p = links.find(class_='item').find(attrs={"class": "info"}).select("div a")
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/115.0.0.0 Safari/537.36"
    }
    url = f'https://smallpacking.agrosem.ua/products/?page={int(i)}'

    session = requests.Session()
    responseA = session.get(url=url, headers=headers)
    session.close()


    print(responseA)
    with open(f'index{i}.html', 'w', encoding="utf-8") as file:
        file.write(responseA.text)

    soupA = BeautifulSoup(responseA.text, 'html.parser')
    p = soupA.find(class_='item').find(attrs={"class": "info"}).select("div a")
#     a = ''
#     for link in links:
#         a = link['href']
#         print(a)
    print(p)
