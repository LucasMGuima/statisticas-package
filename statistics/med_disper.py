import med_tend_central as mtd
import math

def var_amostral(*,valores:list, media:float):
    qtd = len(valores)
    soma = sum([(valor - media)**2 for valor in valores])
    return soma/(qtd-1)

def amplitude(valores:list):
    valores.sort()
    menValor = valores[0]
    maxValor = valores[len(valores)-1]
    return maxValor - menValor

def desvio_padrao(valores:list):
    return math.sqrt(var_amostral(valores=valores, media=mtd.media(valores)))

def coeficinete_variacao(valores:list):
    return (desvio_padrao(valores)/mtd.media(valores))*100