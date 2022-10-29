#!/usr/bin/env python3
import datetime
import requests
import pandas as pd
import pandas_datareader as pdr
import yfinance as yf
import numpy as np
import database.connect as con

# Nome/quantidade/tipo
collection = con.db["Ativos"]
data = list(collection.find())
for i in data:
    print(i)

tickers=[]

def status_carteira():  #Esta função retorna o status da carteira,
    for i in range(len(ativos_carteira)):
        tickers.append(yf.Ticker(ativos_carteira[i][0]))
        print(id(tickers[i]))
    return 0

def aporte():
    #Aqui implementarei a logica do aporte mensal
    return 0

def main():
    r = requests.get('http://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv')
    lines = [i.strip().split(';') for i in r.text.split('\n')]
    df = pd.DataFrame(lines[1:],columns=lines[0])
    print(df.info())
    return 0

if __name__ == '__main__':
    main()
