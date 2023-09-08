from selenium import webdriver
import time
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import re

def get_url(page=1):
    url = f'https://smallpacking.agrosem.ua/products/?page={page}'

    return url


def get_page(url, headers, driver):

    try:
        pass
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def get_page_item(id):
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/115.0.0.0 Safari/537.36"
    }
    url = f'https://smallpacking.agrosem.ua/products/{id}'
    s = requests.Session()
    response = s.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup





useragent = UserAgent()

# створює фейковий user-agent
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")


driver = webdriver.Chrome(options=options)

try:
    driver.maximize_window()






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
    arr = {'id': [],
           'link': []}

    for i in range(2, 4, 1):
        url = f'https://smallpacking.agrosem.ua/products/?page={int(i)}'
        print(url)

        driver.get(url)
        time.sleep(1)

        # оновлюємо сторінку
        driver.refresh()
        time.sleep(1)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        all_links = soup.find_all(class_='item')
        for link in all_links:
            # print(link.get('data-id'))
            arr['id'].append(int(link.get('data-id')))

            links = link.find(attrs={"class": "info"}).select("div a")
            for link in links:
                a = 'https://smallpacking.agrosem.ua' + link['href']
                # print(a)
                arr['link'].append(a)
            # print()
            # теж саме отримаємо через - print(links[0]['href'])



        # print()
        # print()


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

arr.update({'name': [],
            'price': [],
            'weight': []})

for i in arr['id']:
    # links = get_page_item(i).find(class_='item_title').text
    # print(links)
    items = get_page_item(i)

    price = items.find(class_='price').text
    price = float(price.replace(" ", "").replace("₴", ""))

    weight = items.find(class_='body_item active').find('table').find_all('tr')
    for row in weight:
        if row.find('th').text == 'Вага':
            weight = (row.find('td').text).strip()




    arr['name'].append(items.find(class_='item_title').text)
    arr['price'].append(price)
    arr['weight'].append(weight)

print(arr)







# ---------------------------------------------------------------------------------
# def get_data(url):
#     s = get_session()
#     response = s.get(url, timeout=(1.0, 3.0))
#     response.html.render(sleep=16)
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     # cookies = my_cookie_jar
#
#
#
#     # session = HTMLSession()
#     # req = session.get(url)
#     # response = req.html.render(sleep=5)
#     # par = req.html.html
#     # soup = BeautifulSoup(par, "lxml")
#
#
#
#
#     arr = []
#     # result = re.match(r'key', soup.find_all('a'))
#     # all_links = soup.find_all('a', class_ = f'key ddd-truncated')          timeout
#     all_links = soup.find_all('a', class_ = 'key')
#
#     for link in all_links:
#         arr.append(link.get("href"))
#         # arr.append(link.find("span", class_ = "market_listing_item_name").text)
#         # arr.append(link.find("span", class_ = "market_listing_game_name").text)
#         # arr.append(link.find("span", class_ = "market_table_value normal_price").find('span', class_= "normal_price").text)
#         # arr.append("  ")
#
#     # #UPD: для добавления вместо перезаписи можно использовать флаг "а"
#     # with open("links.csv", "a") as file:
#     #     csv_writer = csv.writer(file)
#     #     for links in arr:
#     #         csv_writer.writerow([links])
#     return arr
#
#
# for i in range(2, 4, 1):
#     url = f'https://smallpacking.agrosem.ua/products/?page={int(i)}'
#     print(url)
#     a = get_data(url)
#     print(a)
#     print()
#     print()

# for page in range(1, 4):
#     url = f"https://steamcommunity.com/market/search?q=&category_570_Hero%5B%5D=any&category_570_Slot%5B%5D=any&category_570_Type%5B%5D=any&appid=570#p{page}_popular_desc"
#     get_data(url)


# ---------------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------------
# def get_url(page=1):
#     url = f'https://smallpacking.agrosem.ua/products/?page={page}'
#
#     return url
# def get_page(url):
#     headers = {
#         "Accept": "*/*",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
#             Chrome/115.0.0.0 Safari/537.36"
#     }
#     s = requests.Session()
#     response = s.get(url=url, headers=headers)   # , timeout=15
#     s.close()
#
#     # soup = BeautifulSoup(response.text, 'html.parser')
#
#     return response
#
# soup = BeautifulSoup(get_page(get_url(page=1)).text, 'html.parser')
#
# items = soup.find(class_='products').text
# lst_items = []
#
# str = ''
# for i in items:
#     if i.isdigit():
#         str += i
#     else:
#         if str != '':
#             lst_items.append(int(str))
#             str = ''
#
# lst_items.append((lst_items[1] // lst_items[0]) + 1)
# lst_items.append(lst_items[1] % lst_items[0])
# # print(lst_items)
#
# page_end = lst_items[2]
# # print(page_end)
#
# for i in range(2, 0, -1):
#     # link = get_url(i + 1)
#     # print(link)
#     # links = get_page(link)
#     # print(links)
#     # p = links.find(class_='item').find(attrs={"class": "info"}).select("div a")
#     headers = {
#         "Accept": "*/*",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
#                 Chrome/115.0.0.0 Safari/537.36"
#     }
#     url = f'https://smallpacking.agrosem.ua/products/?page={int(i)}'
#
#     session = requests.Session()
#     responseA = session.get(url=url, headers=headers)
#     session.close()
#
#
#     print(responseA)
#     with open(f'index{i}.html', 'w', encoding="utf-8") as file:
#         file.write(responseA.text)
#
#     soupA = BeautifulSoup(responseA.text, 'html.parser')
#     p = soupA.find(class_='item').find(attrs={"class": "info"}).select("div a")
# #     a = ''
# #     for link in links:
# #         a = link['href']
# #         print(a)
#     print(p)

# ---------------------------------------------------------------------------------


