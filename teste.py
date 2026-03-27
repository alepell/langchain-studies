from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Carrega as variaveis de .env
load_dotenv()

# Chama a API do modelo da openAI
model = ChatOpenAI(model="gpt-4o")

# Executa a chamada ao modelo
result = model.invoke(
    "Este é um teste. Se voce recebeu a requisicao responda  'teste ok'"
)

print(result)
