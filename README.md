# ApiBancariaAssincrona
api de conta bancária
# API Bancária Assíncrona

API simples em FastAPI para gerenciamento de usuários, contas, transações (depósitos/saques) e extratos. Esta documentação descreve como configurar o ambiente, executar a aplicação e usar os endpoints implementados em `app/main.py`.

> Observação: exemplos e formatos são inferidos de `app/main.py` e `app/models.py`. Para validações adicionais (ex.: limites, regex) consulte `app/schemas.py`.

---

## Requisitos
- Python 3.9+ (recomendado 3.10+)
- Git (opcional)

## Preparar ambiente (virtualenv ou venv)
Linux / macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt   # se houver
```

Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

Exemplo mínimo de `requirements.txt` sugerido:
```
fastapi
uvicorn[standard]
sqlalchemy
aiosqlite
passlib[bcrypt]
python-jose[cryptography]
pydantic
```

## Executar o servidor
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
A documentação automática ficará disponível em:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---
# API Bancária Assíncrona

API simples em FastAPI para gerenciamento de usuários, contas, transações (depósitos/saques) e extratos. Esta documentação descreve como configurar o ambiente, executar a aplicação e usar os endpoints implementados em `app/main.py`.

> Observação: exemplos e formatos são inferidos de `app/main.py` e `app/models.py`. Para validações adicionais (ex.: limites, regex) consulte `app/schemas.py`.

---

## Requisitos
- Python 3.9+ (recomendado 3.10+)
- Git (opcional)

## Preparar ambiente (virtualenv ou venv)
Linux / macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt   # se houver
```

Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

Exemplo mínimo de `requirements.txt` sugerido:
```
fastapi
uvicorn[standard]
sqlalchemy
aiosqlite
passlib[bcrypt]
python-jose[cryptography]
pydantic
```

## Executar o servidor
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
A documentação automática ficará disponível em:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---


## Criar ambiente virtual com venv e instalar Poetry dentro do venv

Abaixo está o fluxo completo para criar um `venv`, instalar o `poetry` dentro desse `venv`, instalar dependências e executar a aplicação. Este é o fluxo que você informou já usar — ele mantém o Poetry isolado dentro do ambiente virtual.

OBS: alternativamente, você pode instalar o Poetry globalmente e deixar que ele gerencie ambientes; as instruções a seguir assumem que você quer o Poetry rodando dentro do `venv`.

Linux / macOS
```bash
# 1) Criar e ativar virtualenv
python3 -m venv .venv
source .venv/bin/activate

# 2) Atualizar pip e instalar poetry dentro do virtualenv
pip install --upgrade pip
pip install poetry

# 3) Se o projeto já possuir pyproject.toml (Poetry):
#    instalar dependências listadas no pyproject.toml/poetry.lock
poetry install

# 4) Se NÃO houver pyproject.toml e você quiser criar:
poetry init --no-interaction
# adicionar dependências principais do projeto
poetry add fastapi uvicorn[standard] sqlalchemy aiosqlite passlib[bcrypt] python-jose[cryptography] pydantic

# 5) Executar o servidor usando poetry (sem abrir shell)
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# ou entrar no shell do poetry (usa o ambiente criado)
poetry shell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Windows (PowerShell)
```powershell
# 1) Criar e ativar virtualenv
python -m venv .venv
.venv\Scripts\Activate.ps1

# 2) Atualizar pip e instalar poetry dentro do virtualenv
pip install --upgrade pip
pip install poetry

# 3) Instalar dependências (se houver pyproject.toml)
poetry install

# 4) Criar pyproject e adicionar dependências (se necessário)
poetry init --no-interaction
poetry add fastapi uvicorn[standard] sqlalchemy aiosqlite passlib[bcrypt] python-jose[cryptography] pydantic

# 5) Executar o servidor
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Observações:
- `poetry install` lê `pyproject.toml` e instala as dependências no ambiente ativo (neste fluxo, o próprio venv).
- Se preferir que o Poetry crie/gerencie seu próprio virtualenv dentro do projeto, instale Poetry globalmente e rode:
  ```bash
  poetry config virtualenvs.in-project true
  poetry install
  ```
  Nesse caso, o Poetry criará `.venv/` automaticamente e você pode usar `poetry shell` ou `poetry run ...`.
- Manter o Poetry dentro do `venv` é válido; apenas garanta que você esteja executando o `poetry` do ambiente correto (ativado).

---

## Instalar dependências (resumo)

Se existir `pyproject.toml` no repositório:
```bash
# com venv ativado e poetry instalado no venv
poetry install
```

Se não existir e quiser adicionar as dependências manualmente:
```bash
# inicializa pyproject.toml interativamente (ou --no-interaction para pular)
poetry init --no-interaction

# adicionar dependências do projeto
poetry add fastapi uvicorn[standard] sqlalchemy aiosqlite passlib[bcrypt] python-jose[cryptography] pydantic
```

Para adicionar dependências de desenvolvimento:
```bash
poetry add --dev pytest black isort
```

Para ver o que está instalado:
```bash
poetry show --tree
```

---

## Executar o servidor (modo desenvolvimento)

Com o `venv` ativo (ou usando `poetry run`):
```bash
# se estiver no venv com poetry instalado
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# ou, se entrou no poetry shell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

A documentação automática ficará disponível em:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

Em produção, remova `--reload` e use um gerenciador de processos (systemd, containerização, gunicorn+uvicorn workers, etc).



## Variáveis de ambiente e segurança
Nunca coloque segredos (SECRET_KEY, senhas, tokens, credenciais de DB) no repositório. Use variáveis de ambiente e um `.env` local (com `.env.template` no repositório).

Exemplo `.env.template`:
```
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=sqlite+aiosqlite:///./dev.db
```

Adicione ao `.gitignore` pelo menos:
```
.env
.venv/
venv/
__pycache__/
*.pyc
```

Recomendações:
- Use HTTPS em produção.
- Tokens com tempo de vida curto.
- Não logue tokens ou senhas.
- Use ferramentas como `detect-secrets`, `git-secrets` ou pre-commit hooks para prevenir commits acidentais de segredos.

---

## Models principais (resumo)
- TransactionType (enum): `"deposit"`, `"withdraw"`
- User: id, username, hashed_password, accounts
- Account: id, user_id, number, balance (Decimal), transactions
- Transaction: id, account_id, type, amount (Decimal), created_at

---

## Schemas (inferidos)
- UserCreate: { username: string, password: string }
- UserOut: { id: int, username: string }
- Token: { access_token: string }
- AccountCreate: { number: string }
- AccountOut: { id: int, number: string, balance: decimal }
- TransactionCreate: { type: "deposit" | "withdraw", amount: string|number }
- TransactionOut: { id: int, type: string, amount: decimal, created_at: datetime }
- StatementOut: { account: AccountOut, transactions: [TransactionOut] }

---

## Endpoints (detalhado)

### POST /auth/signup
- Tag: Autenticação
- Autenticação: Não
- Descrição: Cadastra um novo usuário.
- Request (JSON):
```json
{
  "username": "alice",
  "password": "senhaSegura123"
}
```
- Response (ex.):
```json
{
  "id": 1,
  "username": "alice"
}
```
- Erros:
  - 400 — "Usuário já existe"

---

### POST /auth/login
- Tag: Autenticação
- Autenticação: Não
- Descrição: Realiza login e retorna um token JWT.
- Request: form-data (application/x-www-form-urlencoded)
  - username
  - password
- Response (ex.):
```json
{
  "access_token": "eyJ..."
}
```
- Erros:
  - 401 — Credenciais inválidas

Uso: incluir `Authorization: Bearer <ACCESS_TOKEN>` em endpoints protegidos.

---

### POST /accounts
- Tag: Contas
- Autenticação: Sim (Bearer token)
- Descrição: Cria uma nova conta para o usuário autenticado.
- Request (JSON):
```json
{
  "number": "0001"
}
```
- Response (ex.):
```json
{
  "id": 1,
  "number": "0001",
  "balance": "0.00"
}
```
- Erros:
  - 400 — "Conta já existe para este usuário"

---

### POST /accounts/{number}/transactions
- Tag: Transações
- Autenticação: Sim (Bearer token)
- Descrição: Aplica transação (depósito/saque) na conta identificada por `{number}`.
- Path param:
  - number: string
- Request (JSON) — exemplos:
Deposit:
```json
{
  "type": "deposit",
  "amount": "250.00"
}
```
Withdraw:
```json
{
  "type": "withdraw",
  "amount": "100.00"
}
```
Observação: `amount` é convertido para Decimal no servidor (usar string evita problemas de ponto flutuante).

- Response (ex. TransactionOut):
```json
{
  "id": 10,
  "type": "withdraw",
  "amount": "100.00",
  "created_at": "2026-01-11T12:34:56.789Z"
}
```
- Erros:
  - 404 — "Conta não encontrada"
  - 400 — Erro de negócio (ex.: saldo insuficiente)

---

### GET /accounts/{number}/statement
- Tag: Extrato
- Autenticação: Sim (Bearer token)
- Descrição: Retorna `account` + `transactions` (extrato).
- Path param:
  - number: string
- Response (ex. StatementOut):
```json
{
  "account": {
    "id": 1,
    "number": "0001",
    "balance": "150.00"
  },
  "transactions": [
    {
      "id": 5,
      "type": "deposit",
      "amount": "200.00",
      "created_at": "2026-01-11T12:00:00Z"
    },
    {
      "id": 10,
      "type": "withdraw",
      "amount": "50.00",
      "created_at": "2026-01-11T12:30:00Z"
    }
  ]
}
```
- Erros:
  - 404 — "Conta não encontrada"

---

## Segurança nos exemplos com curl (recomendado)

Não coloque tokens reais em README. Use placeholders `<TOKEN>` no material público.

1) Exemplo seguro (ler senha interativamente, não gravar no history):
```bash
read -s -p "Password: " PASSWORD
echo
USERNAME="alice"

TOKEN=$(curl -sS -X POST "https://seu-host/auth/login" \
  -F "username=$USERNAME" -F "password=$PASSWORD" \
  | python -c "import sys,json; print(json.load(sys.stdin)['access_token'])")

curl -sS -X POST "https://seu-host/accounts/0001/transactions" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"type":"withdraw","amount":"100.00"}'

unset PASSWORD
unset TOKEN
```

2) Usar arquivo temporário com permissões restritas:
```bash
printf '%s' '{"type":"withdraw","amount":"100.00"}' > /tmp/body.json
chmod 600 /tmp/body.json

curl -sS -X POST "https://seu-host/accounts/0001/transactions" \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d @/tmp/body.json

shred -u /tmp/body.json 2>/dev/null || rm -f /tmp/body.json
```

3) Exemplo simples para documentação pública (placeholder):
```bash
curl -X POST "https://seu-host/accounts/1234/transactions" \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"type":"withdraw","amount":"100.00"}'
```

---

## Códigos de status (resumo)
- 200/201 — Sucesso
- 400 — Requisição inválida / erro de negócio (ex.: usuário já existe, saldo insuficiente)
- 401 — Não autorizado (token ausente/expirado/inválido)
- 404 — Recurso não encontrado
- 500 — Erro interno do servidor

---

## Boas práticas finais
- Não comite segredos; use `.env` local e `.env.template` no repositório.
- Configure pre-commit hooks para detectar segredos.
- Em produção, remova `--reload` do uvicorn e use um gerenciador de processos.
- Use banco persistente (Postgres, etc.) e migrações (Alembic) em produção.
- Teste as rotinas críticas (ex.: `apply_transaction`) com testes automatizados.

---

Se desejar, copie este README e ajuste os exemplos conforme `app/schemas.py` (para tipos/validações exatas) antes de publicar.


## Variáveis de ambiente e segurança
Nunca coloque segredos (SECRET_KEY, senhas, tokens, credenciais de DB) no repositório. Use variáveis de ambiente e um `.env` local (com `.env.template` no repositório).

Exemplo `.env.template`:
```
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=sqlite+aiosqlite:///./dev.db
```

Adicione ao `.gitignore` pelo menos:
```
.env
.venv/
venv/
__pycache__/
*.pyc
```

Recomendações:
- Use HTTPS em produção.
- Tokens com tempo de vida curto.
- Não logue tokens ou senhas.
- Use ferramentas como `detect-secrets`, `git-secrets` ou pre-commit hooks para prevenir commits acidentais de segredos.

---

## Models principais (resumo)
- TransactionType (enum): `"deposit"`, `"withdraw"`
- User: id, username, hashed_password, accounts
- Account: id, user_id, number, balance (Decimal), transactions
- Transaction: id, account_id, type, amount (Decimal), created_at

---

## Schemas (inferidos)
- UserCreate: { username: string, password: string }
- UserOut: { id: int, username: string }
- Token: { access_token: string }
- AccountCreate: { number: string }
- AccountOut: { id: int, number: string, balance: decimal }
- TransactionCreate: { type: "deposit" | "withdraw", amount: string|number }
- TransactionOut: { id: int, type: string, amount: decimal, created_at: datetime }
- StatementOut: { account: AccountOut, transactions: [TransactionOut] }

---

## Endpoints (detalhado)

### POST /auth/signup
- Tag: Autenticação
- Autenticação: Não
- Descrição: Cadastra um novo usuário.
- Request (JSON):
```json
{
  "username": "alice",
  "password": "senhaSegura123"
}
```
- Response (ex.):
```json
{
  "id": 1,
  "username": "alice"
}
```
- Erros:
  - 400 — "Usuário já existe"

---

### POST /auth/login
- Tag: Autenticação
- Autenticação: Não
- Descrição: Realiza login e retorna um token JWT.
- Request: form-data (application/x-www-form-urlencoded)
  - username
  - password
- Response (ex.):
```json
{
  "access_token": "eyJ..."
}
```
- Erros:
  - 401 — Credenciais inválidas

Uso: incluir `Authorization: Bearer <ACCESS_TOKEN>` em endpoints protegidos.

---

### POST /accounts
- Tag: Contas
- Autenticação: Sim (Bearer token)
- Descrição: Cria uma nova conta para o usuário autenticado.
- Request (JSON):
```json
{
  "number": "0001"
}
```
- Response (ex.):
```json
{
  "id": 1,
  "number": "0001",
  "balance": "0.00"
}
```
- Erros:
  - 400 — "Conta já existe para este usuário"

---

### POST /accounts/{number}/transactions
- Tag: Transações
- Autenticação: Sim (Bearer token)
- Descrição: Aplica transação (depósito/saque) na conta identificada por `{number}`.
- Path param:
  - number: string
- Request (JSON) — exemplos:
Deposit:
```json
{
  "type": "deposit",
  "amount": "250.00"
}
```
Withdraw:
```json
{
  "type": "withdraw",
  "amount": "100.00"
}
```
Observação: `amount` é convertido para Decimal no servidor (usar string evita problemas de ponto flutuante).

- Response (ex. TransactionOut):
```json
{
  "id": 10,
  "type": "withdraw",
  "amount": "100.00",
  "created_at": "2026-01-11T12:34:56.789Z"
}
```
- Erros:
  - 404 — "Conta não encontrada"
  - 400 — Erro de negócio (ex.: saldo insuficiente)

---

### GET /accounts/{number}/statement
- Tag: Extrato
- Autenticação: Sim (Bearer token)
- Descrição: Retorna `account` + `transactions` (extrato).
- Path param:
  - number: string
- Response (ex. StatementOut):
```json
{
  "account": {
    "id": 1,
    "number": "0001",
    "balance": "150.00"
  },
  "transactions": [
    {
      "id": 5,
      "type": "deposit",
      "amount": "200.00",
      "created_at": "2026-01-11T12:00:00Z"
    },
    {
      "id": 10,
      "type": "withdraw",
      "amount": "50.00",
      "created_at": "2026-01-11T12:30:00Z"
    }
  ]
}
```
- Erros:
  - 404 — "Conta não encontrada"

---

## Segurança nos exemplos com curl (recomendado)

Não coloque tokens reais em README. Use placeholders `<TOKEN>` no material público.

1) Exemplo seguro (ler senha interativamente, não gravar no history):
```bash
read -s -p "Password: " PASSWORD
echo
USERNAME="alice"

TOKEN=$(curl -sS -X POST "https://seu-host/auth/login" \
  -F "username=$USERNAME" -F "password=$PASSWORD" \
  | python -c "import sys,json; print(json.load(sys.stdin)['access_token'])")

curl -sS -X POST "https://seu-host/accounts/0001/transactions" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"type":"withdraw","amount":"100.00"}'

unset PASSWORD
unset TOKEN
```

2) Usar arquivo temporário com permissões restritas:
```bash
printf '%s' '{"type":"withdraw","amount":"100.00"}' > /tmp/body.json
chmod 600 /tmp/body.json

curl -sS -X POST "https://seu-host/accounts/0001/transactions" \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d @/tmp/body.json

shred -u /tmp/body.json 2>/dev/null || rm -f /tmp/body.json
```

3) Exemplo simples para documentação pública (placeholder):
```bash
curl -X POST "https://seu-host/accounts/1234/transactions" \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"type":"withdraw","amount":"100.00"}'
```

---

## Códigos de status (resumo)
- 200/201 — Sucesso
- 400 — Requisição inválida / erro de negócio (ex.: usuário já existe, saldo insuficiente)
- 401 — Não autorizado (token ausente/expirado/inválido)
- 404 — Recurso não encontrado
- 500 — Erro interno do servidor

---

## Boas práticas finais
- Não comite segredos; use `.env` local e `.env.template` no repositório.
- Configure pre-commit hooks para detectar segredos.
- Em produção, remova `--reload` do uvicorn e use um gerenciador de processos.
- Use banco persistente (Postgres, etc.) e migrações (Alembic) em produção.
- Teste as rotinas críticas (ex.: `apply_transaction`) com testes automatizados.

---

