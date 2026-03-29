from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# carregar as variaveis de ambiente do arquivo .env
load_dotenv()

# Criando o componente de langchain que interage com a LLM da openAI
model = ChatOpenAI(model="gpt-4o")


### Exemplo 1:
# prompt_template = ChatPromptTemplate(
#     [("user", "Escreva um poema em {idioma} sobre o tema: {tema}.")]
# )

### Criar a Chain
# chain1 = prompt_template | model

### invoke da chain passando as variavies
# resposta = chain1.invoke({"idioma": "português", "tema": "amor"})
# print(resposta.content)

### ------------------------ ###

### Exemplo 2:
# PART 1: Criando ChatPromptTemplate já com mensagem de sistema:
print("-----Exemplo Chain 2 -----")

mensagens = [
    (
        "system",
        "Você é um poeta brasileiro famoso e escreve poemas de no máximo {n_versos} versos.",
    ),
    ("human", "Escreva para mim um poema sobre {assunto}."),
]

prompt_template = ChatPromptTemplate(mensagens)

# PART 2: Criando a chain
chain2 = prompt_template | model

# PART 3: Invoke da chain passando as variáveis.
resposta = chain2.invoke({"n_versos": "10", "assunto": "navios"})

print(resposta.content)
