
"""Funções utilitárias do TechFlow Core."""

import os

PRIORIDADES_VALIDAS = ("baixa", "media", "alta")


def limpar_tela():
    """Limpa a tela do terminal."""
    comando = "cls" if os.name == "nt" else "clear"
    os.system(comando)


def exibir_cabecalho(titulo):
    """Exibe um cabeçalho padronizado."""
    print("=" * 50)
    print(titulo.upper())
    print("=" * 50)


def validar_texto(texto):
    """Verifica se o texto não está vazio."""
    return bool(str(texto).strip())


def solicitar_texto(mensagem):
    """Solicita um texto e impede que fique vazio."""
    while True:
        texto = input(mensagem).strip()

        if validar_texto(texto):
            return texto

        print("Erro: o campo não pode ficar vazio.")


def validar_prioridade(prioridade):
    """Verifica se a prioridade informada é válida."""
    prioridade = str(prioridade).strip().lower()
    return prioridade in PRIORIDADES_VALIDAS


def solicitar_prioridade():
    """Solicita uma prioridade válida."""
    while True:
        prioridade = input(
            "Prioridade (baixa/media/alta): "
        ).strip().lower()

        if validar_prioridade(prioridade):
            return prioridade

        print("Prioridade inválida!")


def formatar_cep(cep):
    """Valida e formata um CEP com oito dígitos.

    Retorna o CEP no formato 00000-000 ou None se inválido.
    """
    numeros = ""

    for caractere in str(cep):
        if caractere.isdigit():
            numeros += caractere

    if len(numeros) != 8:
        return None

    return numeros[:5] + "-" + numeros[5:]
