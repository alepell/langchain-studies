from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4o", temperature=0.1)

# o ChatModel é um componente langchain entao ele possui o protocolo invoke()

resposta = model.invoke("Olá como voce está e o que voce é capaz de fazer?")

print("--------RESPOSTA AIMessage:---------")
print(resposta)
print("-------------------------------------")

print("--------RESPOSTA Somente Texto:------")
print(resposta.content)
print("-------------------------------------")
