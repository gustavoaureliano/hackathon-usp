
from datetime import datetime, timedelta

# Definindo os valores das tarifas em reais por kWh
TARIFA_FORA_PONTA = 0.448  # Fora de ponta
TARIFA_INTERMEDIARIO = 0.653  # Intermediário
TARIFA_PONTA = 1.004  # Ponta

# Definindo o intervalo de cada período (considerando apenas dias úteis)
PONTA_INICIO = datetime.strptime("17:30", "%H:%M").time()
PONTA_FIM = datetime.strptime("20:30", "%H:%M").time()
INTERMEDIARIO_ANTES_INICIO = datetime.strptime("16:30", "%H:%M").time()
INTERMEDIARIO_ANTES_FIM = datetime.strptime("17:30", "%H:%M").time()
INTERMEDIARIO_DEPOIS_INICIO = datetime.strptime("20:30", "%H:%M").time()
INTERMEDIARIO_DEPOIS_FIM = datetime.strptime("21:30", "%H:%M").time()

def calcula_tarifa_branca(inicio: str, fim: str, consumo_kwh: float) -> float:
    inicio = datetime.strptime(inicio, "%H:%M")
    fim = datetime.strptime(fim, "%H:%M")
    custo_total = 0.0

    while inicio < fim:
        if PONTA_INICIO <= inicio.time() < PONTA_FIM:
            tarifa = TARIFA_PONTA
            periodo_fim = min(fim, inicio.replace(hour=PONTA_FIM.hour, minute=PONTA_FIM.minute))
        elif INTERMEDIARIO_ANTES_INICIO <= inicio.time() < INTERMEDIARIO_ANTES_FIM or INTERMEDIARIO_DEPOIS_INICIO <= inicio.time() < INTERMEDIARIO_DEPOIS_FIM:
            tarifa = TARIFA_INTERMEDIARIO
            if inicio.time() < INTERMEDIARIO_ANTES_FIM:
                periodo_fim = min(fim, inicio.replace(hour=INTERMEDIARIO_ANTES_FIM.hour, minute=INTERMEDIARIO_ANTES_FIM.minute))
            else:
                periodo_fim = min(fim, inicio.replace(hour=INTERMEDIARIO_DEPOIS_FIM.hour, minute=INTERMEDIARIO_DEPOIS_FIM.minute))
        else:
            tarifa = TARIFA_FORA_PONTA
            if inicio.time() < INTERMEDIARIO_ANTES_INICIO:
                periodo_fim = min(fim, inicio.replace(hour=INTERMEDIARIO_ANTES_INICIO.hour, minute=INTERMEDIARIO_ANTES_INICIO.minute))
            else:
                periodo_fim = min(fim, datetime.strptime("23:59", "%H:%M"))
        
        # Calcular a diferença em horas
        horas = (periodo_fim - inicio).total_seconds() / 3600
        custo_total += horas * tarifa * consumo_kwh

        # Atualizar o horário de início para o próximo período
        inicio = periodo_fim

    return round(custo_total, 2)