#!/usr/bin/env python3
# Objetivo deste programa é criar uma forma de
# de avaliar o mercado financeiro com queries
# poderosas.
import pandas as pd
import pandas_datareader.data as pdr
import yfinance as yf
import matplotlib as mlp
import matplotlib.pyplot as plt
import numpy as np
import graphs.history_prices as hp
import inspect

# Nome/quantidade/tipo
ativos_carteira = [
          ['BMGD4.SA',100,'stock'],
          ['CARE11.SA',2,'stock'],
          ]

#Esta função retorna o status da carteira,
#mostrando o valor da carteira.

def status_carteira():
    ticker1 = yf.Ticker(ativos_carteira[0][0])
    ticker2 = yf.Ticker(ativos_carteira[1][0])
    print(ticker1.price,ticker2.price)
    return 0

def aporte():
    #Aqui implementarei a logica do aporte mensal

    return 0

def main():
    start_date = "2020-01-1"
    end_date = "2020-12-31"
    ticker2 = pdr.DataReader(name=ativos_carteira[1][0],data_source='yahoo',start=start_date,end=end_date)
    print(ticker2['Close'])
    hp.history(ticker2['Close'])
    return 0


# quant = y/p

if __name__ == '__main__':
    main()
