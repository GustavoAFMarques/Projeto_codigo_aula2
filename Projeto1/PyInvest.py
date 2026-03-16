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

#FII
simulacoes_fii = []
taxa_fii_mensal = Rentabilidade_esperada_mensal
n = int(Prazo_investimento)

for _ in range(5):
    if taxa_fii_mensal != 0:
        fator = m.pow(1 + taxa_fii_mensal, n)
        montante_base = (Capital_inicial * fator) + (Aporte_mensal * ((fator - 1) / taxa_fii_mensal))
    else:
        
        montante_base = Capital_inicial + (Aporte_mensal * n)

  
    variacao_final = r.uniform(-0.03, 0.03)
    montante_ajustado = montante_base * (1 + variacao_final)

    simulacoes_fii.append(montante_ajustado)

# Estatísticas
media_fii   = s.mean(simulacoes_fii)
mediana_fii = s.median(simulacoes_fii)
desvio_fii  = s.stdev(simulacoes_fii) if len(simulacoes_fii) > 1 else 0.0
montante_fii_oficial = media_fii
#formatação monetária
l.setlocale(l.LC_ALL, 'pt_BR.UTF-8')

def moeda(valor):
    return l.currency(valor, grouping=True)

#Data de simulação e resgate

data_simulacao = d.datetime.now()
data_resgate = data_simulacao + d.timedelta(days=Prazo_investimento * 30)



atingiu_meta = False

if montante_cdb_liquido >= Meta:
    atingiu_meta = True
elif montante_lci_liquido >= Meta:
    atingiu_meta = True
elif montante_poupanca >= Meta:
    atingiu_meta = True
elif montante_fii_oficial >= Meta:
    atingiu_meta = True

#ASCII


def grafico_ascii(valor):
    return '█' * int(valor // 1000)



#saida



print("\n" + "-"*60)
print("PyInvest - Simulador de Investimentos")
print("-"*60 + "\n")

print("Data da simulação:", data_simulacao.strftime("%d/%m/%Y"))
print("Data estimada de resgate:", data_resgate.strftime("%d/%m/%Y"))
print("="*60 + "\n")

print("Total investido:", moeda(total_investido))
print("\n" + "-"*60)
print("      RESULTADOS FINANCEIROS")
print("-"*60 + "\n")

# CDB
print("CDB:", moeda(montante_cdb_liquido))
print(grafico_ascii(montante_cdb_liquido) + "\n")

# LCI/LCA
print("LCI/LCA:", moeda(montante_lci_liquido))
print(grafico_ascii(montante_lci_liquido) + "\n")

# Poupança
print("Poupança:", moeda(montante_poupanca))
print(grafico_ascii(montante_poupanca) + "\n")

# FII (média oficial)
print("FII (média):", moeda(montante_fii_oficial))
print(grafico_ascii(montante_fii_oficial) + "\n")

print("--- ESTATÍSTICAS FII ---")
print("Média:", moeda(montante_fii_oficial))
print("Mediana:", moeda(mediana_fii))
print("Desvio padrão:", moeda(desvio_fii))

print("\nMeta atingida:", atingiu_meta)
print("_"*60 + "\n")








