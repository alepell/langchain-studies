from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "Gere para mim uma poema sobre: {tema}. Escreva em {idioma}"
)
retorno = prompt_template.invoke({"tema": "amor", "idioma": "português"})

print(retorno.text)
