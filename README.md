
# 🧀 API de Vendas para Laticínio

Esta é uma API RESTful desenvolvida com Django e Django REST Framework, voltada para o controle de vendas de um laticínio, incluindo cadastro de clientes, produtos, vendas com múltiplos itens e geração de relatórios filtráveis.

🔗 Repositório oficial: [github.com/Joaovitorsm18/laticinio-api](https://github.com/Joaovitorsm18/laticinio-api)

---

## 🚀 Funcionalidades

- 🔐 Autenticação via JWT (JSON Web Tokens)
- 📋 CRUD de clientes (feiras e comércios)
- 📦 CRUD de produtos (por unidade, litro ou quilo)
- 💰 Registro e edição de vendas com múltiplos itens em um único endpoint
- 📸 Suporte a upload de foto de recibo
- 🧾 Controle de itens por venda feito exclusivamente através da própria venda
- 📊 Relatórios com filtros por data, cliente, produto e status
- ✅ Cálculo automático do total da venda

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11+
- Django 5.2
- Django REST Framework
- Django Filters
- Pillow (para imagens)
- SQLite (para desenvolvimento)
- CORS Headers

---

## 📦 Como rodar o projeto localmente

```bash
# Clone o repositório
git clone https://github.com/Joaovitorsm18/laticinio-api.git
cd laticinio-api

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```

Acesse: [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/)

---
## 🔐 Autenticação com JWT

Todos os endpoints (exceto obtenção de tokens) requerem autenticação via JWT.

### 📥Obter Token de Acesso

- `POST /api/v1/token/`

Payload:
```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```
Resposta:
```json
{
  "access": "token_de_acesso",
  "refresh": "token_de_refresh"
}
```
### 🔁Renovar Token de Acesso
`POST /api/v1/token/refresh/`

Payload:
```json
{
  "refresh": "token_de_refresh"
}
```
Resposta:
```json
{
  "access": "novo_token_de_acesso"
}
```
### Como usar
Inclua o token no cabeçalho das requisições:
```makefile
Authorization: Bearer seu_token_de_acesso
```
## 🌐 Principais Endpoints

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

### Vendas (com gerenciamento de itens incluso)
- `GET /api/v1/sales/`
- `POST /api/v1/sales/`
    - Envia os dados da venda com os itens aninhados
    - Aceita envio de `receipt_photo` via `multipart/form-data` se necessário
- `GET /api/v1/sales/<id>/`
- `PUT /api/v1/sales/<id>/`
    - Substitui os itens antigos pelos novos
- `DELETE /api/v1/sales/<id>/`

> ⚠️ **Importante:** Os itens da venda são criados, atualizados e substituídos exclusivamente através do endpoint da venda.  
> Não existem endpoints diretos para `sale-items`.


### Relatório de Vendas
- `GET /api/v1/sales/report`
    - Filtros disponíveis: `date_after`, `date_before`, `customer`, `status`, `product`

## Como criar ou atualizar uma venda
Exemplo de payload para criação/edição:
```json
{
  "customer": 1,
  "date": "2025-06-27",
  "status": "paid",
  "items": [
    {
      "product": 2,
      "unit": "kg",
      "quantity": 4.250,
      "unit_price": 18.00
    },
    {
      "product": 3,
      "unit": "un",
      "quantity": 10,
      "unit_price": 3.50
    }
  ]
}
```
- O campo `total_price` de cada item é calculado automaticamente.

- A imagem `receipt_photo` (recibo) pode ser enviada junto, usando `multipart/form-data`.

### Fornecedores
- `GET /api/v1/suppliers/`
- `POST /api/v1/suppliers/`
- `GET /api/v1/suppliers/<id>/`
- `PUT /api/v1/suppliers/<id>/`
- `DELETE /api/v1/suppliers/<id>/`


---

## 📁 Estrutura do Projeto

```
laticinio-api/
├── app/
├── authentication/
├── customers/
├── products/
├── sales/
├── suppliers/
├── media/
├── manage.py
├── requirements.txt
└── README.md
```


## ✨ Autor

Desenvolvido por João Vítor — [LinkedIn](https://www.linkedin.com/in/joao-vitor-sm/)
