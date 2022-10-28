#!/usr/bin/env python3
import connect

class DBCarteira():
    def getAtivos():
        col = db["Ativos"]
        return col.find_one()
    def adicionarAtivos(ativo,quantidade,tipo):
        col = db["Ativos"]
        col.insertOne(
            {
                "codigo":ativo,
                "quantidade":quantidade,
                "tipo":tipo
            })
