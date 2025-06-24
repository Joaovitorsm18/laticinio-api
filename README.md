
# 🧀 API de Vendas para Laticínio

Esta é uma API RESTful desenvolvida com Django e Django REST Framework, voltada para o controle de vendas de um laticínio, incluindo cadastro de clientes, produtos, vendas e geração de relatórios filtráveis.

Repositório oficial: [github.com/Joaovitorsm18/laticinio-api](https://github.com/Joaovitorsm18/laticinio-api)

---

## 🚀 Funcionalidades

- 📋 CRUD de clientes (feiras e comércios)
- 📦 CRUD de produtos (por unidade, litro ou quilo)
- 💰 Registro de vendas com status e foto de recibo
- 🧾 Controle detalhado dos itens vendidos por venda
- 📊 Relatório de vendas com filtros por data, cliente, produto e status
- 📷 Suporte a upload de imagens (recibo)
- ✅ Calcula automaticamente total da venda e dos itens

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11+
- Django 5.2
- Django REST Framework
- Django Filters
- Pillow (para upload de imagens)
- SQLite (banco de dados local)
- CORS Headers (liberação de acesso entre origens)

---

## 📦 Como rodar o projeto localmente

```bash
# Clone o repositório
git clone https://github.com/Joaovitorsm18/laticinio-api.git
cd laticinio-api

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Inicie o servidor local
python manage.py runserver
```

Acesse: [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/)

---

## 🌐 Endpoints Principais

### Clientes
- `GET /api/v1/customers/`
- `POST /api/v1/customers/`
- `GET /api/v1/customers/<id>/`
- `PUT /api/v1/customers/<id>/`
- `DELETE /api/v1/customers/<id>/`

### Produtos
- `GET /api/v1/products/`
- `POST /api/v1/products/`
- `GET /api/v1/products/<id>/`
- `PUT /api/v1/products/<id>/`
- `DELETE /api/v1/products/<id>/`

### Vendas
- `GET /api/v1/sales/`
- `POST /api/v1/sales/`
- `GET /api/v1/sales/<id>/`
- `PUT /api/v1/sales/<id>/`
- `DELETE /api/v1/sales/<id>/`

### Itens da Venda
- `GET /api/v1/sale-items/`
- `POST /api/v1/sale-items/`
- `GET /api/v1/sale-items/<id>/`
- `PUT /api/v1/sale-items/<id>/`
- `DELETE /api/v1/sale-items/<id>/`

### Relatório de Vendas
- `GET /api/v1/sales/report?date_after=...&customer=...&status=...`

---

## 📁 Estrutura do Projeto

```
laticinio-api/
├── app/
├── customers/
├── products/
├── sales/
├── media/
├── manage.py
├── requirements.txt
└── README.md
```


## ✨ Autor

Desenvolvido por João Vítor — [LinkedIn](https://www.linkedin.com/in/joao-vitor-sm/)
