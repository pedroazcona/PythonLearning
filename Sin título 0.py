# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 14:34:07 2018

@author: poaa
"""

import urllib
from lxml import html

url = "http://www.evaascarza.com"
dominio = "margarita"
servicio = ""

urls = []

page = html.fromstring(urllib.urlopen(url).read())

for link in page.xpath("//a"):
  if ".com" in link.get("href") or ".es" in link.get("href"):
    if "@" not in link.get("href"):
      if dominio not in link.get("href"):
          #print "Name", link.text, "URL", link.get("href")
          urls.insert(0,link.get("href"))

for url in urls:
  try:
    print (url + "\n")
    pagina = html.fromstring(urllib.urlopen(url).read())
    for enlace in pagina.xpath("//a"):
      if servicio in enlace.get("href"):
        print ("La url "+url+" tiene el servicio X")
  except Exception as e:
    print ("La url "+url+" no se pudo estudiar")

print ("termino")

