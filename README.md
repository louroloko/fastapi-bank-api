# 🏦 FastAPI Bank API

Esta é uma API RESTful assíncrona para operações bancárias (depósitos e saques) utilizando FastAPI. O projeto inclui autenticação via JWT, validações de saldo, e documentação automática via OpenAPI (Swagger).

## 🚀 Funcionalidades

- Cadastro de transações (depósitos e saques)
- Consulta de extrato da conta
- Autenticação JWT para proteger endpoints
- Validação de saldo e valores negativos
- Estrutura modular com SQLAlchemy (assíncrono)

## 📦 Requisitos

- Python 3.9+
- Virtualenv (opcional, mas recomendado)

## 🛠️ Instalação

```bash
git clone https://github.com/seunome/fastapi-bank-api.git
cd fastapi-bank-api
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
