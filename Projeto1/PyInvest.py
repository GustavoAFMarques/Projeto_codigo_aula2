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
taxa_poupanca = 0.005
montante_poupanca = (Capital_inicial * m.pow((1+taxa_poupanca), Prazo_investimento))+(Aporte_mensal * Prazo_investimento)

# FII 

taxa_fii_mensal = Rentabilidade_esperada_mensal
n = int(Prazo_investimento)

taxa_segura = taxa_fii_mensal + 1e-9

fator = m.pow(1 + taxa_fii_mensal, n)

montante_base = (Capital_inicial * fator) + (
    Aporte_mensal * ((fator - 1) / taxa_segura)
)

# variação única
variacao_final = r.uniform(-0.03, 0.03)
montante_fii_oficial = montante_base * (1 + variacao_final)

# estatísticas
media_fii   = montante_fii_oficial
mediana_fii = montante_fii_oficial
desvio_fii  = 0.0


# formatação monetária (sem função)
l.setlocale(l.LC_ALL, 'pt_BR.UTF-8')

montante_cdb_fmt = l.currency(montante_cdb_liquido, grouping=True)
montante_lci_fmt = l.currency(montante_lci_liquido, grouping=True)
montante_poupanca_fmt = l.currency(montante_poupanca, grouping=True)
montante_fii_fmt = l.currency(montante_fii_oficial, grouping=True)


# Data de simulação e resgate
data_simulacao = d.datetime.now()
data_resgate = data_simulacao + d.timedelta(days=Prazo_investimento * 30)


# Meta 
atingiu_meta = (
    (montante_cdb_liquido >= Meta) or
    (montante_lci_liquido >= Meta) or
    (montante_poupanca >= Meta) or
    (montante_fii_oficial >= Meta)
)


# ASCII (sem função)
max_valor = max(montante_cdb_liquido, montante_lci_liquido, montante_poupanca, montante_fii_oficial)
grafico_cdb = '█' * int((montante_cdb_liquido / max_valor) * 50)
grafico_lci = '█' * int((montante_lci_liquido / max_valor) * 50)
grafico_poupanca = '█' * int((montante_poupanca / max_valor) * 50)
grafico_fii = '█' * int((montante_fii_oficial / max_valor) * 50)



#saida



print("\n" + "-"*60)
print("PyInvest - Simulador de Investimentos")
print("-"*60 + "\n")

print("Data da simulação:", data_simulacao.strftime("%d/%m/%Y"))
print("Data estimada de resgate:", data_resgate.strftime("%d/%m/%Y"))
print("="*60 + "\n")

print("Total investido:", total_investido)
print("\n" + "-"*60)
print("      RESULTADOS FINANCEIROS")
print("-"*60 + "\n")

# CDB
print("CDB:", montante_cdb_fmt)
print(grafico_cdb + "\n")

# LCI/LCA
print("LCI/LCA:", montante_lci_fmt)
print(grafico_lci + "\n")

# Poupança
print("Poupança:", montante_poupanca_fmt)
print(grafico_poupanca + "\n")

# FII (média oficial)
print("FII (média):", montante_fii_fmt)
print(grafico_fii + "\n")

print("--- ESTATÍSTICAS FII ---")
print("Média:", montante_fii_fmt)
print("Mediana:", montante_fii_fmt)
print("Desvio padrão:", l.currency(desvio_fii, grouping=True))

print("\nMeta atingida:", atingiu_meta)
print("_"*60 + "\n")



