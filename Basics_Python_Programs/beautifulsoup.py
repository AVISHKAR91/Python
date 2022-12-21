# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 21:23:16 2022

@author: dhpcap
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 18:48:39 2021

@author: anilk
"""

#import libraries
#request module helps to send request to web site and retirve html page
import requests  
from bs4 import BeautifulSoup
import re

url = 'http://www.imdb.com/search/title?release_date=2020&sort=num_votes,desc&page=1'
response = requests.get(url)
print(response.content)
#print(response.text[:500])


html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
print(html_soup)

#data=html_soup.find_all("a")
#print(len(data))

#find_all  ------ all matching element
#find  ---- first matching element

movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
print(type(movie_containers))
print(len(movie_containers))


#to get name and movie number of first movie


first_movie=movie_containers[0]
print(first_movie)
# to retrieve movie name
#print(first_movie.find_all('a'))
print(first_movie.h3)
print(first_movie.h3.a)
print(first_movie.h3.a.text)


#to print the rating
print(first_movie.strong.text)

#to find year test
print(first_movie.h3)
#print(first_movie.h3.find_all('span'))

#to find first year

first_year = first_movie.find('span', class_ = 'lister-item-year text-muted unbold')

print(first_year.text)
#To retrieve rating
print(first_movie.strong)
first_imdb = float(first_movie.strong.text)


all_years = html_soup.find_all('span', class_ = 'lister-item-year text-muted unbold')
print(len(all_years))
first_year = all_years[1]
print(first_year.text)




names = []
years = []
ratings = []
movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
for movie in movie_containers:
    #to retrieve movie name
    names.append(movie.h3.a.text)
    yr=movie.find('span', class_ = 'lister-item-year text-muted unbold').text 
    years.append(yr)
    ratings.append(movie.strong.text)
d={"name":names,"year":years,"ranting":ratings}
import pandas as pd
df=pd.DataFrame(d)
