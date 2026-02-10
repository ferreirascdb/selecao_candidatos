# Sistema de Seleção de Candidatos

Sistema web desenvolvido em Django para controle e acompanhamento de candidatos, permitindo cadastro, edição, listagem e exclusão, com controle de acesso por tipo de usuário.

O sistema foi projetado para funcionar 100% em rede local, sem dependência de internet.

# Funcionalidades

- Autenticação de usuários (login e logout)
- Dois níveis de acesso:

    - Administrador (acesso total)

    - Cadastro (apenas inclusão de candidatos)

- Cadastro de candidatos
- Edição de candidatos
- Exclusão de candidatos (com confirmação)
- Listagem com:

    Filtro por Loja
    Busca por Nome
    
- Controle de permissões por usuário
- Interface simples e objetiva
- Estilização via CSS local
- Compatível com múltiplos usuários simultâneos

# Tecnologias Utilizadas
-Python 3
- Django 5.2
- SQLite (pode ser trocado por outro banco)
- HTML5
- CSS3
- Bootstrap
- JavaScript (básico, sem CDN)

# Controle de Acesso
 
- Administrador

Permissões:

    Visualizar candidatos

    Cadastrar candidatos

    Editar candidatos

    Excluir candidatos

- Usuário de Cadastro

Permissões:

    Cadastrar candidatos

Usuários sem permissão são automaticamente redirecionados para a tela Sem Permissão.

# Como Executar o Projeto
1 - Criar ambiente virtual

python -m venv venv

2 - Ativar ambiente

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate

3 - Instalar dependências

pip install -r requirements.txt

4️ - Executar migrações

python manage.py migrate

5️ - Rodar o servidor
python manage.py runserver

Acesse:

http://127.0.0.1:8000/