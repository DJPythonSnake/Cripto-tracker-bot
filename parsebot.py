#Simple parsing bot special for my tg-bot

import requests
from bs4 import BeautifulSoup

#parse info about bincoin
bitcoin = ['https://ru.investing.com/crypto/bitcoin/btc-usd', 'https://ru.investing.com/crypto/bitcoin/btc-rub']

#parse info about ethereum
ethereum = ['https://ru.investing.com/crypto/ethereum/eth-usd', 'https://ru.investing.com/crypto/ethereum/eth-rub']

#get dollar info
bitcoin_get_usd = requests.get(bitcoin[0])
soup = BeautifulSoup(bitcoin_get_usd.text, 'lxml')
course_usd = soup.find('span', class_='text-2xl').text

#get ruble info
bitcoin_get_usd = requests.get(bitcoin[1])
soup = BeautifulSoup(bitcoin_get_usd.text, 'lxml')
course_rub = soup.find('span', class_='text-2xl').text

#get dollar info
ethereum_get = requests.get(ethereum[0])
soup1 = BeautifulSoup(ethereum_get.text, 'lxml')
course1_usd = soup1.find('span', class_='text-2xl').text

#get ruble info
bitcoin_get_usd = requests.get(ethereum[1])
soup = BeautifulSoup(bitcoin_get_usd.text, 'lxml')
course1_rub = soup.find('span', class_='text-2xl').text

