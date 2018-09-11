# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 21:28:52 2018

@author: pmhui
"""
import urllib.request
import autotrader_config as config
from bs4 import BeautifulSoup

def loop_params(soup):
    '''
    bepaal het aantal pagina's die doorlopen moeten worden  
    # zoek de div met de pagina counters  
    # zoek de laatste waarde hierin (laatste pagina)  
    # verwijder anchor tekst zodat het getal overblijft  
    !!! let op: gaat fout bij 1 pagina  
    '''
    counter_div = soup.find('div', attrs={'class': 'page-nave__desktop'})
    counter_page = int(str(counter_div.find_all('a')[-1]).split('>')[1].split('<')[0])
    return counter_page

def read_data(url=config.urlpage):
    '''
    lees data in van de website
    '''
    page = urllib.request.urlopen(url)
    # verwijder headers etc. Deze worden toch niet gebruikt. Bruikbare tekst staat in de body
    soup = BeautifulSoup(page, 'html.parser').body

    return soup

def read_total_results(soup):
    '''
    Lees het totaal aantal resultaten uit
    '''
    count = soup.find('h5', attrs={'class': 'css-1o62zrk'}).text
    count = float(count[:len(count)-11])
    return count
