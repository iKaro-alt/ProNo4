#!/usr/bin/env python3
import os
import pandas as pd
import requests
class scraperCVM:

    # getDFP(ano:datetime)
    def getDFP(self):
        df = pd.DataFrame(lines[1:],columns=lines[0])
        return df

    def downloadDFP(self):
        cvm_dfp_url = 'http://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/'
        for ano in range(2010,2023):
            r = requests.get(cvm_dfp_url+f'dfp_cie_aberta_{ano}.zip')
            open(f"./scrapping/dfps/dfp_cia_aberta_{ano}.zip","wb").write(r.content)
        return 0

    def prepareDFP(self):
        dfps=[]
        rootDir = os.getcwd()
        os.chdir(rootDir+"/scrapping/dfps")
        for file in os.listdir(os.getcwd()):
            uncompressed_data = zipfile.ZipFile(file)
            for spread in uncompressed_data.namelist():
                df = pd.read_csv(
                    file.open(spread)),
                    sep = ";",
                    encoding="ISO-8859-1",
                    dtype={"ORDEM_EXERC":"category"})
                    dfps.append(df)
        os.chdir(rootDir)
        return dfps
