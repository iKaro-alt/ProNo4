#!/usr/bin/env python3
class scraperCVM():
cvm_dfp_url = 'http://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv'
    def getDFP():
        r = requests.get(cvm_dfp_url)
        lines = [i.strip().split(';') for i in r.text.split('\n')]
        df = pd.DataFrame(lines[1:],columns=lines[0])
        return df
