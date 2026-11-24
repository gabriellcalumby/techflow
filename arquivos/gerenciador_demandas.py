"""Gerenciador de demandas do TechFlow Core — Etapa 06.

Nesta etapa, os registros ficam em memória em uma lista de dicionários.
Os dados são perdidos quando o programa é encerrado. A persistência com
SQLite será tratada no desafio extra ou em uma etapa posterior.
"""

PRIORIDADES_VALIDAS = ("baixa", "media", "alta")
STATUS_VALIDOS = ("aberta", "em andamento", "concluida")


def cadastrar_demanda(demandas, dados):
    """Cadastra uma demanda, impedindo campos vazios e IDs duplicados."""
    campos_obrigatorios = (
        "id", "titulo", "solicitante", "prioridade", "cep", "cidade"
    )

    for campo in campos_obrigatorios:
        if not str(dados.get(campo, "")).strip():
            return False, f"O campo {campo} é obrigatório."

    identificador = str(dados["id"]).strip()

    if any(demanda["id"] == identificador for demanda in demandas):
        return False, "Já existe uma demanda com esse ID."

    prioridade = str(dados["prioridade"]).strip().lower()
    if prioridade not in PRIORIDADES_VALIDAS:
        return False, "Prioridade inválida. Use baixa, media ou alta."

    demanda = {
        "id": identificador,
        "titulo": str(dados["titulo"]).strip(),
        "solicitante": str(dados["solicitante"]).strip(),
        "prioridade": prioridade,
        "cep": str(dados["cep"]).strip(),
        "cidade": str(dados["cidade"]).strip(),
        "status": "aberta",
    }
    demandas.append(demanda)
    return True, "Demanda cadastrada com sucesso."


def listar_demandas(demandas):
    """Retorna a lista de demandas cadastradas."""
    return demandas


def buscar_demanda(demandas, identificador):
    """Localiza uma demanda pelo ID."""
    identificador = str(identificador).strip()
    for demanda in demandas:
        if demanda["id"] == identificador:
            return demanda
    return None


def atualizar_status(demandas, identificador, novo_status):
    """Atualiza o status de uma demanda existente."""
    demanda = buscar_demanda(demandas, identificador)
    if demanda is None:
        return False, "Demanda não encontrada."

    novo_status = str(novo_status).strip().lower()
    if novo_status not in STATUS_VALIDOS:
        return False, "Status inválido."

    demanda["status"] = novo_status
    return True, "Status atualizado com sucesso."


def excluir_demanda(demandas, identificador):
    """Exclui uma demanda pelo ID."""
    demanda = buscar_demanda(demandas, identificador)
    if demanda is None:
        return False, "Demanda não encontrada."

    demandas.remove(demanda)
    return True, "Demanda excluída com sucesso."


def solicitar_texto(mensagem):
    """Solicita um texto não vazio."""
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Este campo não pode ficar vazio.")


def exibir_demandas(demandas):
    """Mostra as demandas em formato organizado."""
    if not demandas:
        print("\nNenhuma demanda cadastrada.")
        return

    print("\n" + "=" * 72)
    print("DEMANDAS CADASTRADAS")
    print("=" * 72)
    for demanda in demandas:
        print(
            f"ID: {demanda['id']} | Título: {demanda['titulo']}\n"
            f"Solicitante: {demanda['solicitante']} | "
            f"Prioridade: {demanda['prioridade']}\n"
            f"CEP: {demanda['cep']} | Cidade: {demanda['cidade']}\n"
            f"Status: {demanda['status']}"
        )
        print("-" * 72)


def menu():
    """Executa o menu de gerenciamento pelo terminal."""
    demandas = []

    while True:
        print("\n===== TECHFLOW CORE =====")
        print("1 - Cadastrar demanda")
        print("2 - Listar demandas")
        print("3 - Buscar demanda")
        print("4 - Atualizar status")
        print("5 - Excluir demanda")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            dados = {
                "id": solicitar_texto("ID: "),
                "titulo": solicitar_texto("Título: "),
                "solicitante": solicitar_texto("Solicitante: "),
                "prioridade": solicitar_texto(
                    "Prioridade (baixa/media/alta): "
                ),
                "cep": solicitar_texto("CEP: "),
                "cidade": solicitar_texto("Cidade: "),
            }
            sucesso, mensagem = cadastrar_demanda(demandas, dados)
            print(mensagem)

        elif opcao == "2":
            exibir_demandas(listar_demandas(demandas))

        elif opcao == "3":
            identificador = solicitar_texto("Informe o ID: ")
            demanda = buscar_demanda(demandas, identificador)
            if demanda:
                exibir_demandas([demanda])
            else:
                print("Demanda não encontrada.")

        elif opcao == "4":
            identificador = solicitar_texto("Informe o ID: ")
            status = solicitar_texto(
                "Novo status (aberta/em andamento/concluida): "
            )
            sucesso, mensagem = atualizar_status(
                demandas, identificador, status
            )
            print(mensagem)

        elif opcao == "5":
            identificador = solicitar_texto("Informe o ID: ")
            sucesso, mensagem = excluir_demanda(demandas, identificador)
            print(mensagem)

        elif opcao == "0":
            print("Encerrando o TechFlow Core. Até mais!")
            break

        else:
            print("Opção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    menu()
