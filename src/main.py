#!/usr/bin/env python3
import zipfile
import datetime
import pandas_datareader as pdr
import yfinance as yf
import numpy as np
import database.connect as con
import scrapping.scraperCVM as scraper
import os

# Nome/quantidade/tipo
# collection = con.db["Ativos"]
# data = list(collection.find())
# for i in data:
#     print(i)

# tickers=[]

def status_carteira():  #Esta função retorna o status da carteira,
    for i in range(len(ativos_carteira)):
        tickers.append(yf.Ticker(ativos_carteira[i][0]))
        print(id(tickers[i]))
    return 0

def aporte():
    #Aqui implementarei a logica do aporte mensal
    return 0

def main():
    cvm = scraper.scraperCVM()
    dfps = cvm.prepareDFP()
    print(dfps)
    # uncompressed_data = zipfile.ZipFile('./scrapping/dfps/dfp_cia_aberta_2010.zip','r')
    return 0

if __name__ == '__main__':
    main()
