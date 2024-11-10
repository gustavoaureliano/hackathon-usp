
import openai

def message(dados):
  client = openai.OpenAI(
      api_key="66d0cf0694d1e514ee227bca_8c165bb5ba850006",
      base_url="https://chat.maritaca.ai/api",
  )
  str1 = str(dados)
  str2 = str1+'Gere insights resumidos sem os cálculos pela prioridade de economia de cada equipamento. Para cada equipamento, em ordem de prioridade, explique de forma sucinta a importância de reduzir, explique o porquê é importante considerá-lo. Também indique formas alternativas de energia para cada equipamento. Seu trabalho aqui é auxiliar e conscientizar um usuário que quer reduzir o consumo de energia elétrica doméstica.'
  response = client.chat.completions.create(
    model="sabia-3",
    messages=[
      {"role": "user", "content": str2},
    ],
    max_tokens=8000
  )
  answer = response.choices[0].message.content 
  return answer