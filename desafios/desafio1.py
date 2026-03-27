# Desafio 1 - Manipulação de Dicionário e Paralelização:
# - Receber a entrada do tipo {"input": "Parabéns Você "} e passar para frente (testar uso do RunnablePassthrough)
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

# PARTE 1 - Receber a entrada do tipo {"input": "Parabéns Você "} e passar para frente (testar uso do RunnablePassthrough)
mensagem: dict = {"input": "Parabéns Você"}
parte_1_runnable = RunnablePassthrough()


# PARTE 2 - Quando eu receber a entrada de (1) eu gostaria de criar um dicionário mantendo a entrada de (1) intacta, mas criando uma
# chave nova {"num_caract"} tal que seja a entrada de (1) contando o total de caracteres.
def count_characters(mensagem: dict) -> int:
    return len(mensagem["input"])


count_characters_runnable = RunnableLambda(count_characters)
parte_2_runnable = RunnablePassthrough.assign(num_caract=count_characters_runnable)


# Parte 3 - Usando a saída de (2) quero paralelizar a entrada em dois processos, o primeiro, pegando a entrada textual e adicionando a palavra " Conseguiu!" numa
# chave chamada "transformar_entrada". O segundo não fará nada, apenas passarei para frente a entrada sem qualquer alteração numa chave passa_para_frente.
def transform(entrada: dict) -> str:
    return f"{entrada['input']} Conseguiu!"


parte_3_transforma_entrada = RunnableLambda(transform)
parte_3_passa_pra_frente = RunnablePassthrough()
parte_3_runnable = RunnableParallel(
    {
        "transformar_entrada": parte_3_transforma_entrada,
        "passa_pra_frente": parte_3_passa_pra_frente,
    }
)

# Parte 4 passar pra frente

parte_4_runnable = RunnablePassthrough()

chain = parte_1_runnable | parte_2_runnable | parte_3_runnable | parte_4_runnable

result = chain.invoke(mensagem)

print(result)
