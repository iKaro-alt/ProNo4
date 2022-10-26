#!/usr/bin/env python3
import connect

class DBCarteira():
    def getAtivos():
        col = db["Ativos"]
        return col.find_one()
