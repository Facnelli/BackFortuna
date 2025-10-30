# 🏦 BackFortuna — Backend do Site de Investimentos

Este é o backend do projeto **Fortuna**, um site de investimentos desenvolvido com foco em **Clean Architecture**, **modularidade** e **testabilidade**.  
O backend é escrito em **Python (Flask)** e integra-se a um frontend em **TypeScript**.

---

## 🚀 Tecnologias

- **Python 3.12+**
- **Flask**
- **Cerberus** (validações)
- **MySQL** (banco de dados)
- **Docker / Docker Compose**
- **pytest** (testes unitários)

---

## 🧱 Estrutura do Projeto

```bash
BackFortuna/
│
├── .dockerignore
├── .env
├── .gitignore
├── .pre-commit-config.yaml
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── README.md
├── requirements.txt
└── run.py                # Ponto de entrada da aplicação
│
├── init/
│   └── schema.sql        # Script de criação do banco de dados
│
└── src/
    ├── data/             # Camada de casos de uso e interfaces com repositórios
    │   ├── interfaces/
    │   │   └── users_repository.py
    │   ├── tests/
    │   │   ├── user_finder_spy.py
    │   │   ├── user_register_spy.py
    │   └── use_cases/
    │       ├── user_finder.py
    │       ├── user_finder_test.py
    │       ├── user_register.py
    │       └── user_register_test.py
    │
    ├── domain/           # Regras de negócio e entidades puras
    │   ├── models/
    │   │   └── users.py
    │   └── use_cases/
    │       ├── user_finder.py
    │       └── user_register.py
    │
    ├── errors/           # Manipulação e definição de erros HTTP
    │   ├── error_handler.py
    │   └── types/
    │       ├── http_bad_request.py
    │       ├── http_not_found.py
    │       └── http_unprocessable_entity.py
    │
    ├── infra/            # Implementações concretas (DB, conexões, repositórios)
    │   ├── db/
    │   │   ├── entities/
    │   │   │   └── users.py
    │   │   ├── repositories/
    │   │   │   ├── users_repository.py
    │   │   │   └── users_repository_test.py
    │   │   ├── settings/
    │   │   │   ├── base.py
    │   │   │   ├── connection.py
    │   │   │   └── connection_test.py
    │   │   └── tests/
    │   │       └── users_repository_spy.py
    │
    ├── main/             # Entrada da aplicação (Flask) e configuração de rotas
    │   ├── adapters/
    │   │   └── request_adapter.py
    │   ├── composers/
    │   │   ├── user_finder_composer.py
    │   │   └── user_register_composer.py
    │   ├── routes/
    │   │   └── routes.py
    │   └── server/
    │       └── server.py
    │
    ├── presentation/     # Controladores e modelos de request/response
    │   ├── controllers/
    │   │   ├── user_finder_controller.py
    │   │   ├── user_register_controller.py
    │   ├── http_types/
    │   │   ├── http_request.py
    │   │   └── http_response.py
    │   └── interfaces/
    │       └── controller_interface.py
    │
    └── validators/       # Validações de entrada com Cerberus
        ├── user_finder_validator.py
        └── user_register_validator.py
