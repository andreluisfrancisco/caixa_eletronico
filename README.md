# Caixa Eletrônico

Este projeto simula o funcionamento de um caixa eletrônico, permitindo a interação das operações básicas bancárias de depósito, saque e consulta de saldo.

## Estrutura do Projeto

### Arquivos e Diretórios

- **`main.py`**: Este é o ponto de entrada do aplicativo. Aqui, a aplicação é inicializada, e a interação do usuário com o caixa eletrônico é gerenciada.

- **`common/`**: Contém utilitários comuns que podem ser usados em todo o projeto.
- **`cpf_utils.py`**: Contém funções relacionadas à validação de CPF, ajudando a garantir que os dados do cliente sejam válidos.

- **`controllers/`**: Contém a lógica do controlador, que gerencia a interação entre a interface do usuário e os modelos de dados.
- **`atm_controllers.py`**: Define a classe `CaixaEletronico`, que gerencia a sessão do cliente e as operações do caixa eletrônico, como menu e execução de ações.

- **`models/`**: Contém as definições de modelos que representam as entidades do sistema.
- **`atm_models.py`**: Define as classes `Cliente` e `Conta`, que representam um cliente e sua conta bancária, respectivamente. Contém métodos para validar CPF e gerenciar saldo.

- **`services/`**: Contém a lógica de negócios, isolando as operações relacionadas ao serviço.
- **`atm_services.py`**: Define a classe `AtmServices`, que contém métodos para operações de depósito, saque e geração de extratos, mantendo a lógica de negócios separada dos controladores.

- **`views/`**: Contém a lógica relacionada à apresentação, que pode incluir interações de usuário.
- **`atm_views.py`**: Este arquivo contém funções para exibir mensagens ao usuário, como boas-vindas, opções do menu e feedback sobre as operações realizadas.

