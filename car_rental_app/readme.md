

# TedCar

O **TedCar** é uma aplicação web desenvolvida em Python utilizando o framework Flask. Este projeto foi concebido com fins acadêmicos para simular um sistema completo de gestão e aluguel de veículos, focando em boas práticas de desenvolvimento backend, segurança de dados e interface moderna.

O sistema permite o cadastro de usuários, autenticação segura, gerenciamento de sessão e controle total (CRUD) sobre a frota de veículos, apresentando uma interface visual estilizada com identidade Cyberpunk/Neon.

## Funcionalidades

O sistema conta com as seguintes funcionalidades principais:

  * **Autenticação de Usuários:** Sistema robusto de registro e login com criptografia de senhas (hash).
  * **Gestão de Sessão:** Controle de acesso seguro utilizando Flask-Login, restringindo rotas protegidas apenas a usuários autenticados.
  * **Dashboard Personalizado:** Painel exclusivo onde o usuário visualiza e gerencia apenas os veículos cadastrados por ele.
  * **Gestão de Veículos:**
      * Cadastro de novos veículos (Marca, Modelo, Preço/Dia).
      * Listagem pública de frota disponível.
      * Exclusão de veículos (com verificação de propriedade).
  * **Interface Visual:** Design responsivo e estilizado com tema escuro (Neon/Cyberpunk) e CSS modular.
  * **Feedback ao Usuário:** Sistema de mensagens instantâneas (Flash Messages) para confirmações de ações e alertas de erro.

## Tecnologias Utilizadas

### Backend

  * **Python 3:** Linguagem principal.
  * **Flask:** Framework web para estruturação da aplicação.
  * **Flask-Login:** Gerenciamento de sessões de usuário.
  * **Flask-SQLAlchemy:** ORM para integração e manipulação do banco de dados.
  * **Werkzeug Security:** Biblioteca para hash e verificação segura de senhas.

### Frontend

  * **HTML5 / Jinja2:** Motor de templates para renderização dinâmica.
  * **CSS3:** Estilização personalizada com arquitetura modular (arquivos dedicados por página) e uso de variáveis CSS.

### Banco de Dados

  * **SQLite:** Banco de dados relacional utilizado no ambiente de desenvolvimento (facilmente escalável para PostgreSQL).

## Estrutura do Projeto

A organização de diretórios segue o padrão MVC (Model-View-Controller) adaptado para Flask:

```text
/car_rental_app
│
├── app.py                # Ponto de entrada da aplicação e definição de rotas
├── db.py                 # Configuração e instância do banco de dados
├── modelos.py            # Modelos de dados (User e Car)
│
├── static/               # Arquivos estáticos (Estilos CSS)
│   ├── style.css         # Estilos globais
│   ├── login.css         # Estilo específico da tela de login
│   ├── register.css      # Estilo específico da tela de registro
│   ├── dashboard.css     # Estilo do painel do usuário
│   └── cars.css          # Estilo da listagem e cards de carros
│
├── templates/            # Templates HTML (Views)
│   ├── base.html         # Layout base (Navbar, Footer e Blocos)
│   ├── login.html        # Página de login
│   ├── register.html     # Página de registro
│   ├── dashboard.html    # Painel administrativo do usuário
│   └── cars.html         # Listagem geral de veículos
│
└── instance/
    └── database.db       # Arquivo do banco de dados SQLite
```

## Como Executar o Projeto

Para rodar o projeto localmente, siga as instruções abaixo:

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/KaykEstecio/TedCar.git
    cd TedCar
    ```

2.  **Crie um ambiente virtual (opcional, mas recomendado):**

    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install flask flask-login flask-sqlalchemy
    ```

4.  **Execute a aplicação:**

    ```bash
    python app.py
    ```

5.  **Acesse no navegador:**
    O sistema estará disponível em `http://127.0.0.1:5000`.

## Objetivos de Aprendizado

Este projeto visa demonstrar proficiência nos seguintes conceitos:

  * Implementação de arquitetura Client-Server com Flask.
  * Manipulação de banco de dados relacional via ORM.
  * Segurança em aplicações web (CSRF, Session Hijacking, Password Hashing).
  * Desenvolvimento de interfaces modulares e reutilizáveis com Jinja2.

## Melhorias Futuras

O roteiro de desenvolvimento prevê as seguintes atualizações:

  * Implementação de upload de imagens para os veículos.
  * Sistema de busca e filtragem avançada (por preço ou modelo).
  * Criação de uma API RESTful para consumo externo.
  * Deploy automatizado em serviços de nuvem (Render/Railway).

-----

Desenvolvido para fins acadêmicos.