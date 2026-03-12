import math as m
import random as r
import datetime as d
import statistics as s
import locale as l

l.setlocale(l.LC_ALL, 'pt_BR.UTF-8')

#Entradas
Capital_inicial = float(input('Insira o capital Inicial (R$): '))
Aporte_mensal = float(input('Insira o aporte mensal (R$): '))
Prazo_investimento = float(input('Insira o prazo do investimento (meses): '))
CDI_Anual = float(input('Insira o CDI anual (%) : ')) /100
PCT_CDI_CDB = float(input('Percentual do CDI aplicado ao CDB (%): ')) /100
PCT_CDI_LCI_CLA = float(input('Percentual do CDI aplicado à LCI/LCA (%): ')) /100
Rentabilidade_esperada_mensal = float(input('Rentabilidade mensal esperada do FII (%): ')) /100
Meta = float(input('Meta financeira desejada (R$): '))


#processamento

CDI_mensal = m.pow((1 + CDI_Anual), 1/12) -1 #conversao CDI

total_investido = Capital_inicial + (Aporte_mensal * Prazo_investimento) # total investido

# CDB 
taxa_cdb = CDI_mensal * PCT_CDI_CDB
montante_cdb = (Capital_inicial * m.pow ((1+taxa_cdb), Prazo_investimento))+(Aporte_mensal * Prazo_investimento)
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.05)

#LCI
taxa_lci = CDI_mensal * PCT_CDI_LCI_CLA
montante_lci = (Capital_inicial * m.pow ((1+taxa_lci), Prazo_investimento))+(Aporte_mensal * Prazo_investimento)
lucro_lci = montante_lci - total_investido
montante_lci_liquido = total_investido + (lucro_lci * 0.05)

#poupança
taxa_poupanca = 0.05
montante_poupanca = (Capital_inicial * m.pow((1+taxa_poupanca), Prazo_investimento))+(Aporte_mensal * Prazo_investimento)









#saida