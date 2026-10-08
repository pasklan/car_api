# car_api

API REST para cadastro e gestão de usuários, veículos e marcas, desenvolvida com FastAPI, SQLAlchemy e SQLite.

## Visão geral

Este projeto é uma API backend focada em operações de catalogação e gestão de veículos em um ambiente simples e extensível. A estrutura atual já contempla:

- autenticação e hash de senhas com `pwdlib`
- persistência com SQLAlchemy Async
- banco SQLite local com suporte a migrações via Alembic
- endpoints para usuários com CRUD básico
- estrutura inicial para modelos de carros e marcas

## Stack tecnológica

- Python 3.13+
- FastAPI
- Pydantic v2
- SQLAlchemy Async
- SQLite + aiosqlite
- Alembic
- pwdlib

## Estrutura do projeto

```text
car_api/
├── app.py                 # aplicação FastAPI
├── core/
│   ├── database.py        # engine e sessão do banco
│   ├── security.py        # hash/verificação de senhas
│   └── settings.py        # leitura de configurações via .env
├── models/
│   ├── base.py            # declarative base do SQLAlchemy
│   ├── users.py           # modelo de usuário
│   └── cars.py            # modelos de marca e carro
├── routers/
│   ├── user.py            # endpoints de usuários
│   ├── cars.py            # estrutura inicial para carros
│   └── brands.py          # estrutura inicial para marcas
├── schemas/
│   ├── users.py           # schemas de entrada/saída de usuários
│   └── brands.py          # estrutura inicial de schemas de marcas
├── __init__.py
migrations/
├── versions/
├── env.py
├── script.py.mako
alembic.ini
car.db
.pyproject.toml
README.md
.env
```

## Pré-requisitos

- Python 3.13 ou superior
- Poetry
- Git

## Instalação

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
cd car_api
```

2. Instale as dependências:

```bash
poetry install
```

3. Ative o ambiente virtual:

```bash
poetry shell
```

## Configuração

O projeto usa um arquivo `.env` para configurar a URL do banco de dados. O valor atual é:

```env
DATABASE_URL='sqlite+aiosqlite:///car.db'
```

## Executando a aplicação

Para iniciar a API em modo de desenvolvimento:

```bash
poetry run uvicorn car_api.app:app --reload
```

A aplicação ficará disponível em:

- http://127.0.0.1:8000
- documentação Swagger em http://127.0.0.1:8000/docs
- documentação ReDoc em http://127.0.0.1:8000/redoc

## Endpoints atuais

### Saúde da API

```http
GET /health_check
```

Resposta esperada:

```json
{
  "status": "Ok"
}
```

### Usuários

```http
POST /api/v1/users/
GET /api/v1/users/
GET /api/v1/users/{user_id}
PUT /api/v1/users/{user_id}
DELETE /api/v1/users/{user_id}
```

O endpoint de criação de usuário valida:

- username único
- e-mail único
- mínimo de 3 caracteres para username
- senha com mínimo de 6 caracteres

## Modelo de dados

### Usuário

- `id`
- `username`
- `email`
- `password`
- `created_at`
- `updated_at`

### Carro

- `id`
- `factory_year`
- `model_year`
- `model`
- `color`
- `plate`
- `fuel_type`
- `transmission`
- `price`
- `description`
- `is_available`
- `brand_id`
- `owner_id`
- `created_at`
- `updated_at`

### Marca

- `id`
- `name`
- `is_active`
- `description`
- `created_at`
- `updated_at`

## Migrações do banco

O projeto já inclui migrações do Alembic para criação das tabelas principais. Para aplicar as migrações:

```bash
poetry run alembic upgrade head
```

Para gerar uma nova migração:

```bash
poetry run alembic revision --autogenerate -m "descricao_da_migracao"
```

## Observações

- A API está estruturada como um backend modular e pronta para expansão.
- Os módulos de `cars` e `brands` já aparecem na estrutura do projeto, mas podem requerer implementação complementar conforme a funcionalidade desejada.
- O banco padrão utilizado no projeto é SQLite para facilitar desenvolvimento local e testes.

## Licença

Este projeto está em desenvolvimento e não possui licença definida no momento.
