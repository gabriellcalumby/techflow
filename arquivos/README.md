# TechFlow Core
## Sistema de Gestão de Demandas Internas

**Empresa fictícia:** TechFlow Solutions  
**Linguagem:** Python 3.13 
**Interface:** CLI (linha de comando)  
**Unidade Curricular:** Desenvolvimento de Sistemas I — SENAI  
**Prazo da banca final:** 08/12/2026

---

## 1. Apresentação do projeto

O TechFlow Core é um sistema de gestão de demandas internas desenvolvido em Python. Seu objetivo é permitir o cadastro, a consulta, a listagem, a atualização e a exclusão de chamados técnicos por meio de uma interface de linha de comando.

O sistema também prevê integração com serviços externos para consulta de CEP e cotação de moedas. O desenvolvimento é dividido em 14 etapas, desde a preparação do ambiente até a apresentação final.

## 2. Objetivos

- Organizar demandas e chamados técnicos.
- Evitar registros com campos obrigatórios vazios ou IDs duplicados.
- Permitir consulta, atualização e exclusão de demandas.
- Consultar CEP por meio da API ViaCEP.
- Consultar a cotação USD/BRL por meio da AwesomeAPI.
- Tratar entradas inválidas e falhas de conexão sem encerrar o programa inesperadamente.
- Desenvolver uma aplicação modular, documentada e testada.

## 3. Ambiente e tecnologias

O projeto foi planejado para funcionar em laboratório com **zero permissões de administrador**.

| Recurso | Utilização |
|---|---|
| Python 3.x | Linguagem e execução do sistema |
| VS Code | Edição dos arquivos |
| `urllib.request` | Requisições HTTP às APIs |
| `json` | Leitura das respostas JSON |
| `sqlite3` | Persistência local no desafio extra |
| `datetime` | Manipulação de datas, quando necessário |
| Terminal | Execução da interface CLI |

**Restrição de ambiente:** não instalar bibliotecas globalmente nem utilizar comandos que exijam senha de administrador. As integrações previstas utilizam bibliotecas nativas do Python.

## 4. Estrutura prevista do projeto

```text
techflow_core/
├── main.py
├── gerenciador_demandas.py
├── utils.py
├── integracoes_api.py
├── database.py
├── teste_ambiente.py
├── pratica_clean_code.py
├── codigo_legado.py
├── REQUISITOS.md
├── KANBAN.md
├── PARECER_ARQUITETURA.md
├── CONTRATO.md
├── TESTES.md
└── README.md
```

Os arquivos serão adicionados conforme as etapas forem desenvolvidas. `database.py` é destinado ao desafio extra de persistência com SQLite. `codigo_legado.py` é um arquivo de exercício de refatoração, não um módulo necessário para a execução final.

---

# 5. Desenvolvimento por etapas

## Etapa 01 — Onboarding, ambiente local e compromisso

**Objetivo:** verificar se o Python e o VS Code funcionam no laboratório e estabelecer regras pessoais de organização.

**Atividades:**
1. Criar a pasta `techflow_core`.
2. Abrir a pasta no VS Code.
3. Verificar a versão do Python.
4. Criar e executar `teste_ambiente.py`.
5. Redigir o contrato individual de compromisso com cinco regras.

**Comando de verificação:**

```bash
python --version
```

**Execução do teste:**

```bash
python teste_ambiente.py
```

**Entregáveis:** `teste_ambiente.py` e `CONTRATO.md`.

## Etapa 02 — Engenharia de requisitos

**Objetivo:** registrar o que o sistema deve fazer e os padrões de qualidade que deverá cumprir.

**Requisitos funcionais previstos:**
- RF01 — Cadastrar demandas.
- RF02 — Listar demandas.
- RF03 — Buscar demandas.
- RF04 — Atualizar o status.
- RF05 — Excluir demandas.
- RF06 — Consultar CEP.
- RF07 — Consultar cotação de moedas.
- RF08 — Filtrar demandas por prioridade.
- RF09 — Converter valores estimados em reais para dólares.

**Requisitos não funcionais previstos:**
- Segurança: validar entradas e evitar operações inválidas.
- Integridade: impedir campos obrigatórios vazios e IDs duplicados.
- Usabilidade: apresentar menus e mensagens claras.
- Desempenho: executar operações locais sem demora desnecessária.
- Confiabilidade: tratar erros sem encerramento abrupto.
- Compatibilidade: funcionar em Python 3.x sem dependências externas.

**Entregável:** `REQUISITOS.md`.

## Etapa 03 — Organização ágil e quadro Kanban

**Objetivo:** acompanhar o andamento individual das entregas.

O quadro deverá conter as colunas:
- Backlog;
- A Fazer;
- Em Andamento;
- Em Validação IA;
- Concluído.

As 14 etapas devem ser distribuídas no quadro conforme os prazos do projeto. A situação de cada etapa deve refletir o trabalho realmente executado e validado.

**Entregável:** `KANBAN.md` ou quadro online no Trello/GitHub Projects.

## Etapa 04 — Arquitetura e defesa técnica do Python

**Objetivo:** comparar aplicações Console/CLI, Web e Desktop e justificar a arquitetura escolhida.

**Decisão arquitetural:** utilizar Python em modo CLI. Essa opção é adequada ao escopo atual porque simplifica a execução no laboratório, consome poucos recursos e permite utilizar bibliotecas nativas do Python. A comparação e a justificativa devem ser apresentadas em três parágrafos.

**Preparação para a arguição:**
- Explicar por que a CLI atende ao projeto.
- Explicar como o sistema reagirá quando uma API ou a conexão com a internet estiver indisponível.

**Entregável:** `PARECER_ARQUITETURA.md`.

## Etapa 05 — Sintaxe fundamental, Clean Code e PEP 8

**Objetivo:** refatorar um trecho de código legado que calcula a prioridade de chamados considerando a prioridade informada e o prazo.

**Práticas aplicadas:**
- Utilizar nomes de variáveis e funções claros em `snake_case`.
- Declarar constantes em letras maiúsculas.
- Separar responsabilidades em funções.
- Manter indentação consistente.
- Validar entradas e tratar valores inválidos.

**Arquivos de prática:** `codigo_legado.py` e `pratica_clean_code.py`.

**Execução:**

```bash
python pratica_clean_code.py
```

## Etapa 06 — Estruturas de dados em memória e CRUD

**Objetivo:** implementar as operações de cadastro, listagem, busca, atualização de status e exclusão.

Cada demanda deverá utilizar um dicionário com os campos:
- `id`;
- `titulo`;
- `solicitante`;
- `prioridade`;
- `cep`;
- `cidade`;
- `status`.

Os registros serão armazenados em uma lista de dicionários. O programa deverá bloquear campos obrigatórios vazios, IDs duplicados, prioridades inválidas e status inválidos.

**Execução:**

```bash
python gerenciador_demandas.py
```

**Importante:** nesta etapa os dados ficam somente em memória e são perdidos quando o programa é encerrado. A persistência em banco de dados é tratada no desafio extra.

## Etapa 07 — Modularização e biblioteca utilitária

**Objetivo:** extrair funções reutilizáveis para `utils.py` e reduzir a duplicação de código.

O módulo deverá conter rotinas como:
- Limpar a tela;
- Exibir cabeçalhos;
- Validar textos não vazios;
- Validar prioridades;
- Formatar CEP.

Cada função deverá possuir docstring. O módulo principal deverá importar e utilizar essas funções.

**Entregáveis:** `utils.py` e atualização dos módulos que utilizarem suas funções.

## Etapa 08 — Integração com APIs externas via HTTP e JSON

**Objetivo:** consultar dados externos utilizando somente bibliotecas nativas.

**ViaCEP:** consultar endereço a partir de um CEP no formato:

```text
https://viacep.com.br/ws/{cep}/json/
```

**AwesomeAPI:** consultar a cotação do dólar em relação ao real:

```text
https://economia.awesomeapi.com.br/json/last/USD-BRL
```

O módulo `integracoes_api.py` deverá realizar as requisições com `urllib.request` e interpretar as respostas com `json`.

**Entregável:** `integracoes_api.py`.

## Etapa 09 — Segurança, tratamento de erros e teste de estresse

**Objetivo:** proteger o programa contra entradas inválidas e falhas externas.

**Verificações necessárias:**
- Letras digitadas em campos numéricos;
- Campos vazios;
- CEP inexistente ou inválido;
- Falta de internet;
- Tempo limite excedido;
- Respostas inesperadas das APIs;
- Opções inexistentes no menu.

Utilizar `try`, `except` e `finally` quando apropriado. Tratar erros de conexão, incluindo `urllib.error.URLError`, e apresentar mensagens compreensíveis ao usuário.

**Entregável:** código protegido e registro dos cenários de teste de estresse.

## Etapa 10 — Gestão de conflito e repriorização de escopo

**Objetivo:** simular uma solicitação urgente da área comercial e negociar o impacto no prazo.

**Novos requisitos solicitados:**
- Adicionar o campo `valor_estimado_brl`;
- Converter o valor estimado de reais para dólares usando a cotação consultada;
- Adicionar filtro de listagem por prioridade.

A negociação deverá considerar o impacto das mudanças no cronograma e manter a data final da entrega.

**Entregável:** ata de repriorização com aproximadamente 10 linhas, registrando solicitação, impacto, acordo e prioridades.

## Etapa 11 — Sprint 1: integração total e versão Alpha

**Objetivo:** integrar os módulos e demonstrar o fluxo completo pelo menu principal.

A integração deverá reunir:
- `main.py`;
- `gerenciador_demandas.py`;
- `utils.py`;
- `integracoes_api.py`.

A versão Alpha deverá incluir o campo `valor_estimado_brl`, a conversão para dólar e o filtro por prioridade, conforme a Etapa 10.

**Entregável:** versão Alpha executável a partir de `main.py`.

**Execução prevista:**

```bash
python main.py
```

## Etapa 12 — Sprint 2: testes funcionais, correções e versão Beta

**Objetivo:** verificar o funcionamento do sistema por meio de casos de teste documentados.

Criar `TESTES.md` com pelo menos oito casos, registrando:
- Identificação do teste;
- Funcionalidade testada;
- Entrada utilizada;
- Resultado esperado;
- Resultado obtido;
- Situação (aprovado ou reprovado).

Testar também entradas inválidas, IDs duplicados e falhas de conexão. Corrigir os problemas encontrados antes de declarar o congelamento do código (*Code Freeze*).

**Entregável:** `TESTES.md` preenchido com os testes realmente executados e versão Beta corrigida.

## Etapa 13 — Documentação técnica e ensaio do Pitch

**Objetivo:** finalizar a documentação e preparar a apresentação.

O README deverá apresentar:
- Descrição e objetivo do projeto;
- Tecnologias utilizadas;
- Estrutura de arquivos;
- Requisitos atendidos;
- Instruções de execução;
- Limitações conhecidas.

Preparar um Pitch de cinco minutos com:
1. Problema;
2. Solução;
3. Arquitetura e segurança;
4. Demonstração ao vivo.

**Entregáveis:** `README.md` e roteiro de apresentação.

## Etapa 14 — Banca final

**Data prevista:** 08/12/2026.

**Objetivo:** apresentar e demonstrar o sistema ao docente e à turma.

A apresentação deverá incluir:
- Pitch de cinco minutos;
- Execução do sistema no terminal;
- Demonstração das funcionalidades;
- Respostas às perguntas técnicas;
- Autoavaliação MSEP.

**Entregável:** apresentação final e registro da avaliação docente.

---

# 6. Desafio extra — Persistência com SQLite

Para alunos adiantados, o manual propõe persistir as demandas em banco de dados relacional utilizando o módulo nativo `sqlite3` ou MySQL já instalado no laboratório.

A opção SQLite permite criar um banco local sem instalar pacotes externos. O módulo previsto é `database.py`.

A persistência deverá permitir que as demandas continuem disponíveis mesmo depois de fechar e abrir novamente o programa.

---

# 7. Cronograma geral

| Prazo do manual | Entregas |
|---|---|
| 19/11 | Etapas 01, 02 e 03 |
| 24/11 | Etapas 04, 05 e 06 |
| 26/11 | Etapas 07 e 08 |
| 01/12 | Etapas 09, 10 e 11 |
| 03/12 | Etapas 12 e 13 |
| 08/12 | Etapa 14 — Banca final |

As datas são os checkpoints indicados no manual da atividade. Caso alguma etapa atrase, o quadro Kanban deverá ser atualizado com a situação real.

# 8. Como executar o projeto

Abra a pasta `techflow_core` no VS Code e utilize o terminal integrado.

Para verificar a instalação:

```bash
python --version
```

Para executar os módulos de prática:

```bash
python pratica_clean_code.py
python gerenciador_demandas.py
```

Quando a integração estiver concluída, o ponto de entrada da aplicação será:

```bash
python main.py
```

Se o comando `python` não estiver disponível, verifique se o ambiente possui o iniciador `py`:

```bash
py --version
```

## 9. Boas práticas e limitações

- Não instalar bibliotecas globalmente no laboratório.
- Utilizar bibliotecas nativas sempre que possível.
- Validar entradas antes de executar operações.
- Não armazenar senhas ou informações sensíveis nos arquivos do projeto.
- Não considerar uma etapa concluída sem executar e validar sua entrega.
- As consultas às APIs dependem de conexão com a internet.
- O CRUD em memória não mantém registros após o encerramento; isso muda somente quando a persistência for implementada.

## 10. Referências técnicas

- Python — documentação oficial: https://docs.python.org/3/
- ViaCEP — serviço de consulta de CEP: https://viacep.com.br/
- AwesomeAPI — documentação e serviços: https://docs.awesomeapi.com.br/
- SQLite — documentação: https://docs.python.org/3/library/sqlite3.html

---

**TechFlow Core — TechFlow Solutions**  
Projeto Integrado — Desenvolvimento de Sistemas I
