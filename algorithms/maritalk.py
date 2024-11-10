
import openai
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

client = openai.OpenAI(
    api_key="66d0cf0694d1e514ee227bca_8c165bb5ba850006",
    base_url="https://chat.maritaca.ai/api",
)
str1 = str(dados_consumo_lista)
str2 = str1+'Gere insights resumidos sem os cálculos pela prioridade de economia de cada equipamento. Para cada equipamento, em ordem de prioridade, explique de forma sucinta a importância de reduzir, explique o porquê é importante considerá-lo. Também indique formas alternativas de energia para cada equipamento. Seu trabalho aqui é auxiliar e conscientizar um usuário que quer reduzir o consumo de energia elétrica doméstica.'
response = client.chat.completions.create(
  model="sabia-3",
  messages=[
    {"role": "user", "content": str2},
  ],
  max_tokens=8000
)
answer = response.choices[0].message.content

print(f"Resposta: {answer}")