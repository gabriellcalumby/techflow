
"""Programa de teste das Etapas 07 e 08."""

from utils import (
    exibir_cabecalho,
    formatar_cep,
    solicitar_texto
)

from integracoes_api import (
    consultar_cep,
    consultar_cotacao_dolar,
    converter_brl_para_usd
)


def main():
    """Executa os testes das funções utilitárias e APIs."""

    exibir_cabecalho("TechFlow Core - Teste das Etapas 07 e 08")

    # Teste de CEP
    cep = solicitar_texto("Digite um CEP: ")

    cep_formatado = formatar_cep(cep)

    if cep_formatado is None:
        print("CEP inválido!")
    else:
        print(f"\nConsultando CEP {cep_formatado}...")

        endereco, erro = consultar_cep(cep_formatado)

        if erro:
            print(erro)
        else:
            print("\nEndereço encontrado:")
            print(f"CEP: {endereco['cep']}")
            print(f"Logradouro: {endereco['logradouro']}")
            print(f"Bairro: {endereco['bairro']}")
            print(f"Cidade: {endereco['cidade']}")
            print(f"Estado: {endereco['uf']}")

    # Teste da cotação
    print("\nConsultando cotação do dólar...")

    cotacao, erro = consultar_cotacao_dolar()

    if erro:
        print(erro)
    else:
        print(
            f"Dólar: R$ {cotacao['valor']:.4f}"
        )

        valor_brl = 100.00

        valor_usd = converter_brl_para_usd(
            valor_brl,
            cotacao["valor"]
        )

        print(f"\nConversão de R$ {valor_brl:.2f}:")
        print(f"Resultado: US$ {valor_usd:.2f}")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")

    except EOFError:
        print("\nEntrada encerrada.")
