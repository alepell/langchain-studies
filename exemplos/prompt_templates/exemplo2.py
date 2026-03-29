from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

prompt_template = ChatPromptTemplate(
    ["Gere para mim uma poema sobre: {tema}. Escreva em {idioma}"]
)
retorno = prompt_template.invoke({"tema": "navegação", "idioma": "português"})

# forma alternativa 1
prompt_template2 = ChatPromptTemplate(
    [
        HumanMessagePromptTemplate.from_template(
            "Gere para mim uma poema sobre: {tema}. Escreva em {idioma}"
        )
    ]
)
retorno2 = prompt_template2.invoke({"tema": "navegação", "idioma": "português"})

# forma alternativa 2
prompt_template3 = ChatPromptTemplate(
    [("user", "Gere para mim uma poema sobre: {tema}. Escreva em {idioma}")]
)
retorno3 = prompt_template3.invoke({"tema": "navegação", "idioma": "português"})

print(retorno)
print(retorno2)
print(retorno3)
