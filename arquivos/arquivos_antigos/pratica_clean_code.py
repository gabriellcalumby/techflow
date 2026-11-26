"""Calcula uma pontuação simples para priorizar chamados técnicos."""

PRIORIDADE_ALTA = "alta"
PRIORIDADE_MEDIA = "media"
PRIORIDADE_BAIXA = "baixa"

PONTOS_PRIORIDADE = {
    PRIORIDADE_ALTA: 3,
    PRIORIDADE_MEDIA: 2,
    PRIORIDADE_BAIXA: 1,
}


def calcular_prioridade(prioridade, prazo_dias):
    """Retorna a pontuação do chamado conforme prioridade e prazo."""
    pontuacao = PONTOS_PRIORIDADE.get(prioridade)

    if pontuacao is None:
        raise ValueError("Prioridade inválida.")

    if prazo_dias < 0:
        raise ValueError("O prazo não pode ser negativo.")

    if prazo_dias <= 1:
        pontuacao += 2
    elif prazo_dias <= 3:
        pontuacao += 1

    return pontuacao


def obter_prazo():
    """Solicita um prazo inteiro e valida a entrada."""
    while True:
        try:
            prazo = int(input("Prazo em dias: "))
            if prazo < 0:
                print("Digite zero ou um número positivo.")
                continue
            return prazo
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def main():
    """Executa o exemplo de cálculo pelo terminal."""
    print("=== CÁLCULO DE PRIORIDADE DE CHAMADO ===")
    prioridade = input("Prioridade (alta/media/baixa): ").strip().lower()

    while prioridade not in PONTOS_PRIORIDADE:
        print("Prioridade inválida.")
        prioridade = input("Digite alta, media ou baixa: ").strip().lower()

    prazo_dias = obter_prazo()
    pontuacao = calcular_prioridade(prioridade, prazo_dias)
    print(f"Pontuação do chamado: {pontuacao}")


if __name__ == "__main__":
    main()
