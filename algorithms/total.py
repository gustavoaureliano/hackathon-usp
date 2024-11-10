import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import io

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

# Função para calcular a diferença de tempo em horas
def calcular_tempo(comeco, fim):
    formato = "%H:%M"
    comeco = datetime.strptime(comeco, formato)
    fim = datetime.strptime(fim, formato)
    delta = fim - comeco
    return delta.total_seconds() / 3600  # Converte para horas

# Definir a faixa de tempo do gráfico (por exemplo, de 00:00 às 23:59)
horarios = [datetime.strptime(f"{h:02}:00", "%H:%M") for h in range(24)]  # Hora a hora
consumo_por_hora = [0] * 24  # Inicializa o consumo por hora

# Para cada equipamento, calcular o consumo em cada intervalo de tempo
for dado in dados_consumo_lista:
    comeco = datetime.strptime(dado['comeco'], "%H:%M")
    fim = datetime.strptime(dado['fim'], "%H:%M")
    potencia = dado['potencia']
    
    # Dividir o período em horas
    while comeco < fim:
        hora_atual = comeco.hour
        proxima_hora = comeco.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
        
        if fim <= proxima_hora:
            # Consumo parcial na última hora
            tempo_parcial = calcular_tempo(comeco.strftime("%H:%M"), fim.strftime("%H:%M"))
            consumo_por_hora[hora_atual] += potencia * tempo_parcial
            break
        else:
            # Consumo completo de uma hora
            tempo_completo = 1  # Uma hora completa
            consumo_por_hora[hora_atual] += potencia * tempo_completo
            comeco = proxima_hora

# Gerar o gráfico de consumo por hora
horarios_str = [h.strftime("%H:%M") for h in horarios]  # Para exibir o horário no eixo x
plt.figure(figsize=(10, 6))
plt.plot(horarios_str, consumo_por_hora, marker='o', color='skyblue')
plt.xlabel('Horário do Dia')
plt.ylabel('Consumo Total (kWh)')
plt.title('Consumo de Energia ao Longo do Dia')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('grafico_consumo.png')
plt.show()

