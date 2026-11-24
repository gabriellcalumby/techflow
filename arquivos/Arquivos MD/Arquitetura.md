TECHFLOW CORE — PARECER TÉCNICO DE ARQUITETURA
Etapa: 04 — Arquitetura de Sistemas e Defesa Técnica do Python
Data: 24/11/2026

Comparação entre Console/CLI, Web e Desktop
Uma aplicação Console/CLI funciona por meio de comandos e menus exibidos no terminal. Ela consome poucos recursos, é simples de executar e permite desenvolver funcionalidades sem depender de interface gráfica. Como o TechFlow Core será utilizado em um laboratório com restrição de instalação e deverá funcionar com Python 3.x já disponível, a CLI atende ao cenário e facilita os testes das operações de cadastro, consulta, atualização e exclusão.

Uma aplicação Web é acessada pelo navegador e normalmente utiliza uma aplicação servidora, rotas HTTP e páginas ou componentes visuais. Ela seria interessante caso o TechFlow Core precisasse ser acessado simultaneamente por vários setores ou computadores. Porém, essa arquitetura exigiria mais componentes e configuração, aumentando a complexidade para o escopo atual e para o ambiente restrito do laboratório.

Uma aplicação Desktop é instalada e executada como um programa com interface gráfica no computador. Ela pode oferecer uma experiência visual mais amigável, mas pode exigir bibliotecas, empacotamento e permissões de instalação. Por esses motivos, não é a opção mais simples para a situação proposta. A escolha técnica é Python em modo CLI, pois permite entregar as funcionalidades solicitadas com menor complexidade, usando bibliotecas nativas e sem exigir privilégios de administrador.

Defesa técnica da escolha
A arquitetura CLI em Python atende ao TechFlow Core porque:

permite criar um menu simples para as operações do sistema;
utiliza estruturas nativas como listas e dicionários;
permite consumir APIs REST com urllib.request e interpretar JSON com json;
permite persistência futura com sqlite3;
funciona sem instalação global de pacotes externos.
Simulação de Comitê de Arquitetura
Pergunta 1 — Por que escolher uma interface CLI em vez de uma interface Web?

Resposta: Porque o escopo atual é um sistema interno de pequeno porte, executado no laboratório. A CLI reduz a complexidade, consome poucos recursos e permite implementar e testar o CRUD sem precisar configurar servidor ou instalar dependências externas. Se futuramente houver necessidade de acesso simultâneo por vários setores, a arquitetura poderá ser reavaliada.

Pergunta 2 — Como o sistema continuará funcionando se a API estiver indisponível?

Resposta: As chamadas HTTP serão protegidas por tratamento de exceções, incluindo erros de conexão e tempo limite. O sistema exibirá uma mensagem clara e permitirá que o usuário continue utilizando as funções locais, como cadastrar, listar, buscar, atualizar e excluir demandas. A consulta externa ficará indisponível temporariamente, mas não deverá encerrar o programa.

Conclusão
A escolha de Python com interface CLI é adequada ao cenário, aos recursos disponíveis e ao prazo do projeto. A solução é simples de executar, modularizável e compatível com as bibliotecas nativas do Python.
