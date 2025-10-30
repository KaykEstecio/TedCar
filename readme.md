# 🚗 CarRent — Aplicativo de Aluguel de Carros (Flask)

**CarRent** é um aplicativo web desenvolvido com **Python e Flask**, criado como projeto acadêmico para simular um sistema de aluguel de carros.  
Ele permite o cadastro de usuários, login seguro e o gerenciamento de veículos disponíveis para locação.  

---

## 🧩 Funcionalidades principais

- **Cadastro de usuários:** criação de contas com senha criptografada.  
- **Login e autenticação:** sistema de login seguro com gerenciamento de sessão.  
- **Dashboard pessoal:** cada usuário visualiza apenas os carros cadastrados por ele.  
- **Cadastro de veículos:** adição de carros com marca, modelo e preço por dia.  
- **Listagem pública:** página que exibe todos os carros cadastrados.  
- **Logout:** encerramento seguro da sessão do usuário.  

---

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **Flask** (framework principal)
- **Flask-Login** (autenticação e controle de acesso)
- **Flask-SQLAlchemy** (ORM e integração com SQLite)
- **Werkzeug Security** (hash de senhas)
- **HTML + CSS (Jinja Templates)**

---

## 🗄️ Estrutura básica do projeto

```
/app.py              # Arquivo principal Flask
/db.py               # Inicialização do banco de dados
/modelos.py          # Definição das classes User e Car
/templates/          # Páginas HTML (index, login, register, dashboard, etc.)
/static/             # Arquivos estáticos (CSS, imagens)
```


---

## 🎯 Objetivo do projeto

O objetivo é **demonstrar conceitos de desenvolvimento web com Flask**, incluindo:

- Estrutura de rotas e templates;  
- Criação e manipulação de banco de dados SQLite;  
- Login seguro e autenticação;  
- Boas práticas em pequenos projetos backend.  

---

## 🚀 Próximos passos (melhorias sugeridas)

- Adicionar sistema de busca e filtros para carros;  
- Implementar upload de imagens para os veículos;  
- Criar uma API REST para integração com frontend;  
- Design responsivo com Bootstrap ou Tailwind.  

---

💡 Desenvolvido com dedicação como projeto acadêmico.
