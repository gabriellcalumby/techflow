TECHFLOW CORE
Documento de Engenharia de Requisitos

Projeto: TechFlow Core  
Empresa: TechFlow Solutions  
Linguagem: Python 3.13
Interface CLI (Linha de Comando)  
Versão 1.0

---

1. Objetivo 

O TechFlow Core é um sistema de gerenciamento de demandas internas desenvolvido em Python, com interface de linha de comando (CLI). Seu objetivo é facilitar o cadastro, a consulta, a atualização e a exclusão de chamados técnicos, garantindo organização, integridade e facilidade de utilização.

2. Requisitos Funcionais (RF)

Os requisitos funcionais descrevem as funcionalidades que o sistema deverá executar.

| Código | Requisito | Descrição |
|---|---|---|
| RF01 | Cadastrar demandas | Permitir cadastrar novas demandas com ID, título, solicitante, prioridade, CEP e cidade. |
| RF02 | Listar demandas | Exibir todas as demandas cadastradas no sistema. |
| RF03 | Buscar demandas | Permitir localizar uma demanda específica por meio do seu ID. |
| RF04 | Atualizar status | Permitir alterar o status de uma demanda cadastrada. |
| RF05 | Excluir demandas | Permitir excluir uma demanda utilizando seu ID. |
| RF06 | Consultar CEP | Consultar automaticamente o endereço e a cidade por meio da API ViaCEP. |
| RF07 | Consultar cotação | Consultar a cotação atual do dólar em relação ao real por meio da AwesomeAPI. |
| RF08 | Filtrar por prioridade | Permitir visualizar demandas de acordo com sua prioridade. |
| RF09 | Converter valores | Permitir converter valores estimados em reais para dólares utilizando a cotação consultada. |

3. Requisitos Não Funcionais (RNF)

Os requisitos não funcionais estabelecem os padrões de qualidade e funcionamento do sistema.

| Código | Categoria | Descrição |
|---|---|---|
| RNF01 | Segurança | O sistema deverá validar as entradas dos usuários para evitar dados inválidos e operações indevidas. |
| RNF02 | Integridade | O sistema deverá impedir cadastros com campos obrigatórios vazios e IDs duplicados. |
| RNF03 | Usabilidade | A interface CLI deverá apresentar menus organizados e mensagens claras para facilitar a utilização. |
| RNF04 | Desempenho | As operações de cadastro, busca, listagem, atualização e exclusão deverão ocorrer sem demora desnecessária. |
| RNF05 | Confiabilidade | O sistema deverá tratar erros de conexão e entradas inválidas sem encerrar abruptamente a aplicação. |
| RNF06 | Compatibilidade | O programa deverá funcionar em ambientes com Python 3.x, sem exigir instalação de bibliotecas externas. |

## 4. Tecnologias Utilizadas

- Python 3.13;
- Biblioteca urllib.request para requisições HTTP;
- Biblioteca json para interpretação de dados das APIs;
- Biblioteca sqlite3 para persistência de dados;
- Interface CLI para interação com o usuário.

## 5. Restrições do Projeto

- O sistema será desenvolvido em Python.
- A interface será exclusivamente via terminal.
- As integrações externas utilizarão APIs REST com retorno JSON.
- Serão priorizadas bibliotecas nativas do Python.
- O desenvolvimento deverá funcionar sem permissões de administrador.

6. Considerações Finais

O documento estabelece os requisitos necessários para o desenvolvimento do TechFlow Core. 
As funcionalidades e características descritas servirão como referência para as próximas etapas de implementação, testes e validação do sistema.
