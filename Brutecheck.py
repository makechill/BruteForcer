from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

url = sys.argv[1]

with open('wordlist.txt', 'r') as file:
        soup_string = file.read()

soup = BeautifulSoup(soup_string, 'html.parser')

hostname = url

rg = requests.get(hostname)

