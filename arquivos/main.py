import gerenciador_demandas as gd
from utils import limpar_tela, exibir_cabecalho
from integracoes_api import consultar_cep, consultar_cotacao_dolar


def pausar():
    input("\nPressione ENTER para continuar...")


def menu():
    print("1. Cadastrar demanda")
    print("2. Listar demandas")
    print("3. Buscar demanda")
    print("4. Atualizar demanda")
    print("5. Excluir demanda")
    print("6. Consultar CEP")
    print("7. Consultar cotação do dólar")
    print("0. Sair")


def executar():
    while True:
        limpar_tela()
        exibir_cabecalho()

        menu()

        opcao = input("\nEscolha uma opção: ").strip()

        try:
            if opcao == "1":
                gd.adicionar_demanda()

            elif opcao == "2":
                gd.listar_demandas()

            elif opcao == "3":
                gd.buscar_demanda()

            elif opcao == "4":
                gd.atualizar_demanda()

            elif opcao == "5":
                gd.excluir_demanda()

            elif opcao == "6":
                cep = input("Digite o CEP: ")
                endereco = consultar_cep(cep)

                if endereco:
                    print("\nEndereço encontrado:")
                    print("Logradouro:", endereco.get("logradouro"))
                    print("Bairro:", endereco.get("bairro"))
                    print("Cidade:", endereco.get("localidade"))
                    print("UF:", endereco.get("uf"))
                else:
                    print("CEP inválido ou serviço indisponível.")

            elif opcao == "7":
                cotacao = consultar_cotacao_dolar()

                if cotacao:
                    print(f"\nCotação atual do dólar: R$ {cotacao:.2f}")
                else:
                    print("Não foi possível consultar a cotação.")

            elif opcao == "0":
                print("\nEncerrando o TechFlow Core...")
                break

            else:
                print("\nOpção inválida!")

        except Exception as erro:
            print(f"\nOcorreu um erro: {erro}")

        pausar()


if __name__ == "__main__":
    executar()