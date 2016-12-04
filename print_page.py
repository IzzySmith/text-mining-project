#!/usr/local/bin/python3.5
import asyncio
import aiohttp
import concurrent.futures
import time
import progressbar
from concurrent.futures import ProcessPoolExecutor
from process_text import absolute_urls
from bs4 import BeautifulSoup as bs

test_url = absolute_urls[1]

bar = progressbar.ProgressBar()

@asyncio.coroutine
def print_page(urls):
    response = yield from aiohttp.request('GET', urls)
    return (yield from response.text())

def get_soup(page):
    """
    Takes an opened url page and converts it to soup
    retrieves links 
    """
    drug_list = []
    soup = bs(page, "lxml")
    encode_soup = soup.decode('utf-8', 'ignore')
    return encode_soup
    

def get_drug_and_gender(soup):
    if (soup.find(class_='footdata')):
        end_table = soup.find(class_='footdata')
        rows = end_table.findAll('tr')
    else:
        pass
    #the gender is listed in the table data text as the 3rd element in the table
    gender_in_table = [[td.text for td in tr.findAll("td")] for tr in rows]
    gender = gender_in_table[1]
    #get the table containing the drug information
    drug_class = [td.find('a') for td in soup.findAll('td', {'class' : 'dosechart-substance'})]
    drug = [drug.text for drug in drug_class if drug]
    drug_gender = (drug, gender)
    #need to return a list of tuples
    drug_list.append(drug_gender)
    return drug_list

sem = asyncio.Semaphore(5)
loop = asyncio.get_event_loop()  
test = [loop.run_until_complete(print_page(u)) for u in bar(absolute_urls)]
loop.close

print(test.get_soup)
