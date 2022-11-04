import discord
import os
import scrapy



url="http://cafe-battelle.eldora.ch/menus-du-jour/cafe-battelle/"

import requests
from bs4 import BeautifulSoup


vgm_url = 'http://cafe-battelle.eldora.ch/menus-du-jour/cafe-battelle/'
html_text = requests.get(vgm_url).text




print(soup)