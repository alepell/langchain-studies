# Desafio 1 - Manipulação de Dicionário e Paralelização:
# - Receber a entrada do tipo {"input": "Parabéns pra Você"} e passar para frente (testar uso do RunnablePassthrough)
# - Quando eu receber a entrada de (1) eu gostaria de criar um dicionário mantendo a entrada de (1) intacta, mas criando uma
# chave nova {"num_caract"} tal que seja a entrada de (1) contando o total de caracteres.
# - Usando a saída de (2) quero paralelizar a entrada em dois processos, o primeiro, pegando a entrada textual e adicionando a palavra " Conseguiu!" numa
# chave chamada "transformar_entrada" o segundo não fará nada, apenas passarei para frente a entrada sem qualquer alteração numa chave passa_para_frente.
# - Por fim, vou passar para frente a combinação do processo paralelo e imprimir o resultado.

from langchain_core.runnables import (
    RunnableLambda,
    RunnablePassthrough,
    RunnableParallel,
)


def num_caract(message: dict):
    return len(message["input"])


def transformar_entrada(message: str):
    return "Conseguiu!"


run1 = RunnablePassthrough.assign(num_caract=num_caract)
run2 = RunnableLambda(transformar_entrada)

chain = run1 | RunnableParallel(
    transformar_entrada=run2, passa_pra_frente=RunnablePassthrough()
)


result = chain.invoke({"input": "Parabéns pra Você"})

print(result)
