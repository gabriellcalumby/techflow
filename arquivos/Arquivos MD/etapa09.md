# Etapa 9 — Robustez e Segurança

## Objetivo
Implementar mecanismos de validação e tratamento de erros para garantir que o TechFlow Core funcione de maneira segura e estável.

## Implementações
- Tratamento de exceções com try/except.
- Validação de valores monetários.
- Rejeição de valores negativos ou iguais a zero.
- Tratamento de entradas inválidas.
- Tratamento de falhas de conexão com APIs.
- Proteção contra encerramento inesperado.

## Testes realizados
- Valores numéricos válidos.
- Valores com vírgula decimal.
- Valores negativos.
- Valores iguais a zero.
- Entradas contendo letras.
- Campos vazios.
- CEP inválido.
- Falha de conexão com API.

## Resultado
O sistema passou a tratar entradas inválidas e falhas externas, evitando encerramentos inesperados durante as operações testadas.

**Status: Em desenvolvimento / Concluída após os testes.**
