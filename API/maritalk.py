
import openai

def message(dados):
  client = openai.OpenAI(
      api_key="66d0cf0694d1e514ee227bca_8c165bb5ba850006",
      base_url="https://chat.maritaca.ai/api",
  )
  str1 = str(dados)
  str2 = str1+"Gere insights resumidos sem os cálculos, pela prioridade de economia de cada equipamento. Gere um prompt em ordem de prioridade de economia, explicando maneiras mais viáveis e alternativas de economia de energia. Gere somente essa saída em HTML5. Conscientize sobre a gestão de energia elétrica doméstica. Retire o '''html no inicio e o ''' no final."
  response = client.chat.completions.create(
    model="sabia-3",
    messages=[
      {"role": "user", "content": str2},
    ],
    max_tokens=8000
  )
  answer = response.choices[0].message.content 
  return answer