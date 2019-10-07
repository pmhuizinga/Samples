# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 15:45:57 2018
test string voor github
@author: pmhui
"""
# import libraries
import autotrader_scraping as a_s
import autotrader_config as config

# lees pagina in
soup = a_s.read_data()
# lees het totaal aantal resultaten (auto's) uit
total_nr_of_cars = a_s.read_total_results(soup)
# Bepaal het aantal pagina's tbv loop
total_nr_of_pages = a_s.loop_params(soup)

# maak loop
for x in range(1, total_nr_of_pages+1):
    print(config.urlpage0 + str(x))
    
auto_data = list(soup.find_all('h2', attrs={'class': 'css-63oe3q'}))
# =============================================================================
# auto_data = auto_data[:].replace('<h2 class="css-63oe3q">','')
# auto_data = str(auto_data).split('<span>')
# 
# auto_data = str(auto_data).split('</span>')
# auto_data = str(auto_data).split(',')
# =============================================================================



#<h2 class="css-63oe3q"><span>Mercedes-Benz B 180 CDI Business Class airco, trekhaak, face lift,</span></h2>
