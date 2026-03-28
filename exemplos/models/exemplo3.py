from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()

## Chatmodel
model = ChatOpenAI(model="gpt-4o", temperature=0.1)

conversa = [
    (
        "system",
        "Você é um assistente útil que responde ao usuário com detalhes e exemplos.",
    )
]

while True:
    entrada = input("Entrada Usuário (digite 'q' para parar.): ")
    if entrada.lower() == "q":
        break

    conversa.append(("user", f"{entrada}"))

    resultado = model.invoke(conversa)
    resposta = resultado.content
    conversa.append(("assistant", f"{resposta}"))

    print(f"Resposta IA: {resposta}")

print("---- Histórico Completo ----")
print(conversa)
