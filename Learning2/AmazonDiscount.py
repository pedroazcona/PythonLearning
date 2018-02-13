# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:48:48 2017

@author: poaa
"""

import amazonproduct
config = {
    'access_key': '',
    'secret_key': '',
    'associate_tag': 'ofertruchas-21',
    'locale': 'es'
}
api = amazonproduct.API(cfg=config)


#Fichero
f = open('workfile.csv', 'w')
#Cabecera
f.write('Ranking;Marca;Precio;Titulo;ASIN;URL\n')

#Tipos de busqueda: 'All','Beauty','OfficeProducts','Electronics','Watches','Jewelry',
#'Luggage','MobileApps','Shoes','KindleStore','Automotive','MusicalInstruments','GiftCards',
#'Toys','SportingGoods','PCHardware','Lighting','Books','MP3Downloads','Tools','Baby',
#'VideoGames','ForeignBooks','Apparel','DVD','Kitchen','Music','LawnAndGarden','HealthPersonalCare',
#'Software'
items = api.item_search('OfficeProducts', Keywords='*', MinimumPrice='5000', MinPercentageOff='40', ResponseGroup='Large', Sort='reviewrank')

for item in items:

    #from pprint import pprint
    #pprint (vars(item))

    #Variables
    try:
        v_ranking = item.SalesRank.text
    except AttributeError:
        v_ranking = ''
    try:        
        v_marca = item.ItemAttributes.Brand.text.encode('ascii', 'ignore')
    except AttributeError:
        v_marca = ''
    try:    
        v_precio = item.OfferSummary.LowestNewPrice.FormattedPrice
    except AttributeError:
        v_precio = ''        
    v_titulo = item.ItemAttributes.Title.text.encode('ascii', 'ignore')
    v_asin = item.ASIN.text

    #log
    print ('%s' % (v_asin))

    #Fichero
    f.write(v_ranking + ';')
    f.write(v_marca + ';')
    f.write(v_precio + ';')
    f.write(v_titulo + ';')    
    f.write(v_asin + ';')
    f.write('http://www.amazon.es/gp/product/' + v_asin + '?tag=ofertruchas-21\n')
    
f.closed