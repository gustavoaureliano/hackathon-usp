import tarifabranca
from datetime import datetime
'''
Equipamentos = []
'''
ConsumoPorEquipamento = []
'''
dados_consumo_lista = [
    {'equipamento': 'Geladeira', 'potencia': 0.120, 'comeco': '06:00', 'fim': '08:24'},
    {'equipamento': 'Geladeira', 'potencia': 0.120, 'comeco': '22:00', 'fim': '22:34'},
    {'equipamento': 'Geladeira', 'potencia': 0.120, 'comeco': '17:00', 'fim': '17:43'},
    {'equipamento': 'Ar Condicionado', 'potencia': 2.000, 'comeco': '18:00', 'fim': '19:33'},
    {'equipamento': 'Ar Condicionado', 'potencia': 2.000, 'comeco': '17:00', 'fim': '19:55'},
    {'equipamento': 'Ar Condicionado', 'potencia': 2.000, 'comeco': '21:00', 'fim': '22:30'},
    {'equipamento': 'Máquina de Lavar', 'potencia': 0.500, 'comeco': '06:00', 'fim': '08:02'},
    {'equipamento': 'Máquina de Lavar', 'potencia': 0.500, 'comeco': '14:00', 'fim': '14:29'},
    {'equipamento': 'Máquina de Lavar', 'potencia': 0.500, 'comeco': '09:00', 'fim': '10:47'},
    {'equipamento': 'Televisão', 'potencia': 0.150, 'comeco': '09:00', 'fim': '09:27'}]

def read_data(Casa):
    ListaEquipamentos = []
    for i in range(len(Casa.Equipamentos)):
        for periodouso in ListaUso(Equipamentos[i]):
            Dict = {
                "equipamento": Equipamento[i]
                "potencia": Equipamento[i](Potencia)
                "comeco": DataComeco(periodouso)
                "fim": Datafim(periodouso)
            }
            ListaEquipamentos.append(Dict)
        return ListaEquipamentos
'''
Dados = read_data(Input)

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
            
total_tarifabranca = total_tarifabranca(Dados)
total_tarifaconvencional = total_tarifaconvencional(Dados)
'''
print(total_tarifabranca(dados_consumo_lista))
print(total_tarifaconvencional(dados_consumo_lista))
print(total_equipamentotarifabranca(dados_consumo_lista, 'Geladeira'))
print(total_equipamentotarifabranca(dados_consumo_lista, 'Ar Condicionado'))
print(total_equipamentotarifabranca(dados_consumo_lista, 'Televisão'))
print(total_equipamentotarifabranca(dados_consumo_lista, 'Máquina de Lavar'))
print(total_equipamentotarifaconvencional(dados_consumo_lista, 'Geladeira'))
print(total_equipamentotarifaconvencional(dados_consumo_lista, 'Ar Condicionado'))
print(total_equipamentotarifaconvencional(dados_consumo_lista, 'Televisão'))
print(total_equipamentotarifaconvencional(dados_consumo_lista, 'Máquina de Lavar'))
'''