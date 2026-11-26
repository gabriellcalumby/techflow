
"""Integrações externas do TechFlow Core."""

import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


TEMPO_LIMITE = 10

URL_VIACEP = "https://viacep.com.br/ws/{}/json/"

URL_COTACAO = (
    "https://economia.awesomeapi.com.br/json/last/USD-BRL"
)


def consultar_json(url):
    """Realiza uma requisição HTTP e retorna os dados JSON."""

    requisicao = Request(
        url,
        headers={"User-Agent": "TechFlow-Core"}
    )

    try:
        with urlopen(
            requisicao,
            timeout=TEMPO_LIMITE
        ) as resposta:

            conteudo = resposta.read().decode("utf-8")
            dados = json.loads(conteudo)

            return dados, None

    except HTTPError as erro:
        return None, f"Erro HTTP: {erro.code}"

    except URLError:
        return None, "Falha de conexão com a internet."

    except TimeoutError:
        return None, "Tempo limite da consulta excedido."

    except json.JSONDecodeError:
        return None, "Erro ao interpretar os dados recebidos."

    except OSError:
        return None, "Não foi possível acessar o serviço."


def consultar_cep(cep):
    """Consulta o endereço de um CEP na API ViaCEP."""

    numeros = ""

    for caractere in str(cep):
        if caractere.isdigit():
            numeros += caractere

    if len(numeros) != 8:
        return None, "CEP inválido. Digite oito números."

    url = URL_VIACEP.format(numeros)

    dados, erro = consultar_json(url)

    if erro:
        return None, erro

    if dados.get("erro"):
        return None, "CEP não encontrado."

    endereco = {
        "cep": dados.get("cep", ""),
        "logradouro": dados.get("logradouro", ""),
        "bairro": dados.get("bairro", ""),
        "cidade": dados.get("localidade", ""),
        "uf": dados.get("uf", "")
    }

    return endereco, None


def consultar_cotacao_dolar():
    """Consulta a cotação do dólar na AwesomeAPI."""

    dados, erro = consultar_json(URL_COTACAO)

    if erro:
        return None, erro

    try:
        cotacao = dados["USDBRL"]

        valor = float(cotacao["bid"])

        resultado = {
            "moeda": "USD/BRL",
            "valor": valor,
            "data_hora": cotacao.get("create_date", "")
        }

        return resultado, None

    except (KeyError, TypeError, ValueError):
        return None, "Não foi possível interpretar a cotação."


def converter_brl_para_usd(valor_brl, cotacao):
    """Converte reais em dólares usando a cotação informada."""

    try:
        valor = float(valor_brl)
        cambio = float(cotacao)

        if valor < 0 or cambio <= 0:
            return None

        resultado = valor / cambio

        return round(resultado, 2)

    except (TypeError, ValueError):
        return None
