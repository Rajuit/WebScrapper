import requests
from bs4 import BeautifulSoup
import pymysql



def trade_spider(max_pages):
    page =15
    while page <= max_pages:
        url = 'your url with landing page name '+str(page)
        source_code = requests.get(url)
        plane_text = source_code.text
        soup = BeautifulSoup(plane_text, "lxml")
        for link in soup.find_all('div', {'class': 'food_description'}):
            href = "your base url"+str(link.a.get('href'))
            title = str(link.a.text)
            print(href)
            print(title)
            get_single_item_data(href,title)
        page += 1


def get_single_item_data(item_url,title):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    L=[[]]
    for tr in soup.find_all('tr'):
        td1 = tr.find_all('td', {'class': 'col-1'})
        td2 = tr.find_all('td', {'class': 'col-2'})



        print(str(td1[0].text)+"                 "+str(td2[0].text)+"                              "+ str(td1[1].text)+"        "+str(td2[1].text))
       # print(td1[0].text)
        L.append([td1[0].text,td2[0].text,td1[1].text,td2[1].text])

    database_connection(L,title)


def database_connection(L,title):
    print(L)
    title = title.replace("'","")
    title=title.replace("–","")
    title=title.replace("™","")
    print(title)
    db = pymysql.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         passwd="root",  # your password
                         db="fitness",
                         autocommit=True)
    cursor = db.cursor()
    #query ="INSERT INTO `test`(`name`, `image_url`, `price`, `quantity`) VALUES  ('%s', '%s', '%s', '%s')" % (title, L[1][1], L[1][3],L[9][3])
    cursor.execute(query);

    cursor.close()

trade_spider(26)








