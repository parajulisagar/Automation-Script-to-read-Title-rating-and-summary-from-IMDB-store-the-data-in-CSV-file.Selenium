
# from selenium import webdriver
from bs4 import BeautifulSoup
import requests
# import time
import pandas as pd
import csv

# from webdriver_manager.chrome import ChromeDriverManager

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# path="C:\\Users\\intern13\\Desktop\\driver\\chromedriver.exe"
# driver = webdriver.Chrome(path)

# driver.get("https://www.imdb.com/chart/top?ref_=nv_mv_250")
# driver.maximize_window()




url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
Titles=[]
Ratings=[]
Summaries=[]
movies = soup.find_all('tr')

# file=open('scrapes.csv', 'wb')
# writer=csv.writer(file)



for movie in movies:
    if movie.find('td',class_='titleColumn')!= None:
        Title=movie.find('td',class_='titleColumn').a.text
        print(Title)
        Curr_url=movie.find('td',class_='titleColumn').a['href']
        Curr_url=f"https://www.imdb.com{Curr_url}"
        Titles.append(Title)
    else:
        pass

    if movie.find('strong')!= None:
        Rating=movie.find('strong').text
        Ratings.append(Rating)
        print(Rating)
    else:
        pass
    if movie.find('td',class_='titleColumn')!= None:
        Title=movie.find('td',class_='titleColumn').a.text
        if Title != "":
            inresp=requests.get(Curr_url)
            Summary_soup=BeautifulSoup(inresp.text, 'lxml')
            Summary=Summary_soup.find(class_='sc-16ede01-0 fMPjMP').text
            Summaries.append(Summary)
            print(Summary)   
        else:
            pass
    else:
        pass
    # writer.writerow([Title.encode('utf-8'), Rating.encode('utf-8') , Summary.encode('utf-8')])
    
# file.close()

dictonary = {'Title':Titles,'Rating':Ratings, 'Summary':Summaries}
df = pd.DataFrame(dictonary)
csv=df.to_csv('C:\\Users\\intern13\\Desktop\\driver\\scraping.csv')