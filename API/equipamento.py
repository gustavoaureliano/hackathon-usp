import matplotlib.pyplot as plt
from datetime import datetime
'''
# Lista de dados de consumo
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
    {'equipamento': 'Televisão', 'potencia': 0.150, 'comeco': '09:00', 'fim': '09:27'}
]
'''
# Função para calcular a diferença de tempo em horas
def calcular_tempo(comeco, fim):
    formato = "%H:%M"
    comeco = datetime.strptime(comeco, formato)
    fim = datetime.strptime(fim, formato)
    delta = fim - comeco
    return delta.total_seconds() / 3600  # Converte para horas

def grafico_equipamento(dados):
    consumos = []
    for dado in dados:
        tempo_uso = calcular_tempo(dado['comeco'], dado['fim'])
        consumo = dado['potencia'] * tempo_uso
        consumos.append({'equipamento': dado['equipamento'], 'consumo': consumo})

    # Agora, para gerar o gráfico, podemos somar o consumo por equipamento ou plotar o consumo por evento.
    equipamentos = [dado['equipamento'] for dado in dados]
    consumos_totais = [consumo['consumo'] for consumo in consumos]

    # Gerar o gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(equipamentos, consumos_totais, color='skyblue')
    plt.xlabel('Equipamento')
    plt.ylabel('Consumo Total (kWh)')
    plt.title('Consumo Total de Energia por Equipamento')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('grafico_equipamento.png')
