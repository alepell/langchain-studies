from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain.schema import HumanMessage

prompt_template = ChatPromptTemplate(
    [
        (
            "system",
            "Você é um assistente útil e criativo com habilidades de escritor e poeta.",
        ),
        ("user", "Gere para mim uma poema sobre: {tema}. Escreva em {idioma}"),
    ]
)
retorno = prompt_template.invoke({"tema": "navegação", "idioma": "português"})

# alternativa usando MessagesPlaceholder

prompt_template2 = ChatPromptTemplate(
    [
        (
            "system",
            "Você é um assistente útil e criativo com habilidades de escritor e poeta.",
        ),
        MessagesPlaceholder(variable_name="msg_user"),
    ]
)
retorno2 = prompt_template2.invoke(
    {
        "msg_user": HumanMessage(
            content="Gere para mim uma poema sobre: amor. Escreva em ingles"
        )
    }
)


print(retorno)
print(retorno2)
