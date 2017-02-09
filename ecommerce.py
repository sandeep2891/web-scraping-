try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

from time import sleep
from bs4 import BeautifulSoup  
import re 
import pandas as pd

df = pd.read_csv('C:/holiday/sqlaexport.txt')
keyword =  df['QUERY_TXT'].tolist()

columns = ['rank','term','product', 'price-in $','cents']
pc = pd.DataFrame(columns=columns)

length = len(keyword)- 1
i = 0
for j in range(length):
    try:
        k = 1
        term = keyword[j]
        term = term.replace(" ", "%20")
        quote_page = (url + term)
        term = term.replace("%20"," ")
    
        page = urllib2.urlopen(quote_page)
    except:
         print("Something bad happened")
         print(j)
         print(term)   
         sleep(60)
    else:
        soup = BeautifulSoup(page, 'html.parser') 
        for tv in soup.find_all("div",class_="search-result-listview-item clearfix"):
            for product in ndtv.find_all("h2", class_="prod-ProductTitle no-margin truncated font-normal heading-b"):
                x = product.text
                break
            for sport in ndtv.find_all("span",class_='Price-characteristic'):
                y = sport.text
                break
            for commerce in ndtv.find_all("span",class_="Price-mantissa"):
                z = commerce.text
                
                
                break
            pc.set_value(i, 'product', x)
            pc.set_value(i,'price-in $',y)
            pc.set_value(i,'cents',z)
            pc.set_value(i,'term',term)
            pc.set_value(i,'rank',k)
            k= k + 1
            i = i + 1
            
pc['price'] = pc['price-in $']+'.'+pc['cents']
data.to_csv("C:/holiday/commerce.csv")
