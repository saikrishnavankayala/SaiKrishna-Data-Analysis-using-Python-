# -*- coding: utf-8 -*-
"""DA_DAY5ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bj4GFdsoDpZZvewYSCeE4CyBXBRLds4d

Random Fox API
"""

import requests

page=requests.get('https://randomfox.ca/floof')

print(page.status_code)

print(page.text)

print(page.json())

"""my api=b192eae6-3069-4264-ad42-589411a037a6
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

---


"""

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY':'b192eae6-3069-4264-ad42-589411a037a6',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

import pandas as pd

norm=pd.json_normalize(data['data'])
norm

"""machine learning=like humans learn from their past expereiences,machines learn from past data!
training a machine on various things is called machine learning

machine learning language is put the songs like loved songs later suggest songs and then unlike songs

types of machine learning:
Supervised Learning
Unsupervised Learning
Reinforcement
"""