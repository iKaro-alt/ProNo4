#!/usr/bin/env python3
# Objetivo deste programa é criar uma forma de
# de avaliar o mercado financeiro com queries
# poderosas.
import b3api as b3
import pandas as pd
import yfinance as yf
import matplotlib as mlp
import matplotlib.pyplot as plt
import numpy as np
import inspect

# Nome/quantidade/tipo
ativos_carteira = [
          ['BMGD4',100,'stock'],
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
    ticker2 = yf.Ticker(ativos_carteira[1][0])
    print(ticker2.history("8d"))
    status_carteira()
    return 0


# quant = y/p

if __name__ == '__main__':
    main()
