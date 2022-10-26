#!/usr/bin/env python3
class DBDataframes():
    def SaveDataFrame(dics):
        db.collection.insert_many(dics)
        return 0
