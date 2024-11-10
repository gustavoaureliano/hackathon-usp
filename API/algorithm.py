import tarifabranca as tarifabranca
from datetime import datetime

def total_tarifabranca(dados_consumo_lista):
    #Dados = read_data(Casa)
    valor_tarifabranca = 0
    for dict in dados_consumo_lista:
        valor_tarifabranca += tarifabranca.calcula_tarifa_branca(dict['comeco'], dict['fim'], dict['potencia'])
    return valor_tarifabranca

def total_tarifaconvencional(dados_consumo_lista):
    #Dados = read_data(Casa)
    tarifa_convencional = 0.73
    valor_tarifaconvencional = 0
    total = 0
    for dict in dados_consumo_lista:
        comeco =datetime.strptime(dict['comeco'], "%H:%M")
        fim = datetime.strptime(dict['fim'], "%H:%M")
        valor_tarifaconvencional = (fim-comeco).total_seconds()/3600
        valor_tarifaconvencional *= float(dict['potencia'])
        valor_tarifaconvencional *= tarifa_convencional 
        total += valor_tarifaconvencional
    return round(total,2)

def total_equipamentotarifabranca(Dados, Equipamento):
    DictEquipamento = []
    for dict in Dados:
        if dict['equipamento'] == Equipamento:
            DictEquipamento.append(dict)
    return round(total_tarifabranca(DictEquipamento),2)

def total_equipamentotarifaconvencional(Dados, Equipamento):
    DictEquipamento = []
    for dict in Dados:
        if dict['equipamento'] == Equipamento:
            DictEquipamento.append(dict)
    return round(total_tarifaconvencional(DictEquipamento),2)