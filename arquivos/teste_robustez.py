from utils import validar_valor


def testar_validacao_valores():
    casos = [
        ("100", 100.0),
        ("50,50", 50.5),
        ("10.25", 10.25),
        ("0", None),
        ("-10", None),
        ("abc", None),
        ("", None),
        ("10abc", None)
    ]

    for entrada, esperado in casos:
        resultado = validar_valor(entrada)

        if resultado == esperado:
            print(f"[OK] Entrada: {entrada!r}")
        else:
            print(f"[ERRO] Entrada: {entrada!r}")
            print(f"Esperado: {esperado}")
            print(f"Recebido: {resultado}")


if __name__ == "__main__":
    testar_validacao_valores()