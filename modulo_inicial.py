# ==============================================================================
# ALUNO: GABRIEL HENRIQUE CALUMBY MOURA
# PROJETO TECHFLOW CORE - MÓDULO DE AUTENTICAÇÃO E REQUISIÇÕES
# ==============================================================================

def executar_sistema():
    """Realiza a autenticação e inicia o sistema após o acesso autorizado."""
    print("--- SISTEMA TECHFLOW CORE - PAINEL INICIAL ---")

    tentativas_maximas = 3
    tentativas_atuais = 0
    usuario_autenticado = False
    usuario_correto = "admin_techflow"
    senha_correta = "senha123"

    # Autenticação: permite até três tentativas de usuário/senha.
    while tentativas_atuais < tentativas_maximas and not usuario_autenticado:
        print(f"\\n[Tentativa {tentativas_atuais + 1} de {tentativas_maximas}]")
        usuario_input = input("Informe o nome de usuário: ").strip()
        senha_input = input("Informe a senha de acesso: ").strip()

        if not usuario_input or not senha_input:
            print("Aviso: Nenhum campo pode ficar em branco!")
        elif usuario_input == usuario_correto and senha_input == senha_correta:
            usuario_autenticado = True
            print("\\nSucesso: Acesso concedido! Bem-vindo ao TechFlow Core.")
        else:
            print("Erro: Usuário ou senha incorretos.")
            tentativas_atuais += 1

    if usuario_autenticado:
        executar_menu_principal(senha_correta)
    else:
        print("\\nBloqueio: Excedeu o número máximo de tentativas de acesso.")


def executar_menu_principal(senha_correta):
    """Exibe o menu principal e executa a opção escolhida pelo usuário."""
    executando = True

    while executando:
        print("\\n=== MENU DE OPÇÕES TECHFLOW ===")
        print("1 - Registrar Novo Chamado")
        print("2 - Listar Chamados Ativos")
        print("3 - Sair do Sistema")
        print("4 - Alterar Senha")

        opcao = input("Selecione uma opção (1-4): ").strip()

        if opcao == "1":
            titulo_chamado = input("Digite o título do chamado: ").strip()

            if len(titulo_chamado) >= 5:
                print(f"Sucesso: Chamado '{titulo_chamado}' registrado!")
            else:
                print("Aviso: O título do chamado deve ter pelo menos 5 caracteres.")

        elif opcao == "2":
            print("\\nCarregando lista de chamados...")

            # Laço for simulando a varredura de registros.
            for i in range(1, 4):
                print(f" -> Chamado #00{i}: [Em Andamento]")

        elif opcao == "3":
            print("Encerrando sessão no TechFlow Core. Até breve!")
            executando = False

        elif opcao == "4":
            senha_atual = input("Informe a senha atual: ").strip()

            if senha_atual != senha_correta:
                print("Erro: A senha atual está incorreta.")
            else:
                nova_senha = input("Digite a nova senha: ").strip()
                confirmacao_senha = input("Confirme a nova senha: ").strip()

                if not nova_senha:
                    print("Aviso: A nova senha não pode ficar em branco.")
                elif nova_senha != confirmacao_senha:
                    print("Erro: As senhas informadas não coincidem.")
                else:
                    senha_correta = nova_senha
                    print("Sucesso: Senha alterada com sucesso!")

        else:
            print("Aviso: Opção inválida! Escolha um número entre 1 e 4.")


# Execução do programa.
if __name__ == "__main__":
    executar_sistema()
