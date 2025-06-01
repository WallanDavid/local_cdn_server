# 📦 local_cdn_server

Servidor local simples de CDN em Python para testes de cache, headers HTTP e entrega de arquivos estáticos.

![Python CI](https://github.com/WallanDavid/local_cdn_server/actions/workflows/python-app.yml/badge.svg)
![Cobertura de Testes](https://img.shields.io/badge/cobertura-100%25-brightgreen)

---

## 🚀 Funcionalidades

- Entrega de arquivos estáticos via HTTP
- Headers customizados (como `Cache-Control`, `X-CDN`)
- Ideal para testar comportamento de cache em navegadores, proxies ou CDNs

---

## 🛠️ Como executar localmente

```bash
git clone https://github.com/WallanDavid/local_cdn_server.git
cd local_cdn_server

# Cria ambiente virtual (opcional)
python -m venv venv
venv\Scripts\activate  # No Windows

# Instala dependências
pip install -r requirements.txt

# Executa o servidor
python server.py
```

Acesse: [http://localhost:8000/index.html](http://localhost:8000/index.html)

---

## 🧪 Como executar os testes

```bash
# Ative o venv antes, se ainda não estiver ativo
venv\Scripts\activate

# Executa testes com cobertura
coverage run -m pytest
coverage report

# Gera relatório HTML
coverage html
start htmlcov/index.html  # Abre no navegador (Windows)
```

---

## 📁 Estrutura do Projeto

```
local_cdn_server/
├── .github/workflows/       # CI com GitHub Actions
│   └── python-app.yml
├── static/                  # Arquivos estáticos servidos
│   └── index.html
├── tests/                   # Testes automatizados
│   └── test_server.py
├── server.py                # Código principal do servidor HTTP
├── requirements.txt         # Dependências do projeto
├── .gitignore
└── README.md
```

---

## 📄 Licença

Projeto de uso livre para fins educacionais e testes locais.
