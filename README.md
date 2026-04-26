# Portfólio Profissional

Este é o meu projeto de portfólio profissional desenvolvido utilizando o framework web **Django**. O projeto permite exibir informações pessoais, projetos desenvolvidos e inclui um formulário de contato funcional que envia mensagens diretamente para o e-mail configurado.

## 🚀 Funcionalidades

- **Início:** Exibe os dados pessoais principais do perfil (foto, nome social, curso, período).
- **Projetos:** Lista todos os projetos acadêmicos e profissionais cadastrados.
- **Contato:** Uma página contendo os canais de contato (LinkedIn, GitHub, Telefone) e um formulário integrado que realiza o envio real de e-mails utilizando SMTP.
- **Painel Administrativo:** Gerenciamento dos dados dinâmicos do site através do painel admin padrão do Django (Modelos: `DadosPessoais`, `Projeto`, `Certificado` e `Tecnologia`).

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Django 6.0.4**
- **HTML5 e CSS3** (Estilização própria com design responsivo, variáveis de cor, etc.)
- **Banco de Dados:** PostgreSQL
- **Bibliotecas auxiliares:**
    - `**python-decouple - 3.8**` | Serve para separar as configurações do código fonte (como senhas, chaves de API e strings de banco de   dados), lendo esses dados do arquivo `.env`.
    - `**cloudinary - 1.44.2**` | SDK oficial do Cloudinary para Python. Serve para integrar e interagir com a API do Cloudinary.
    - `**django-cloudinary-storage - 0.3.0**` | Serve como uma ponte para o Django usar o Cloudinary como o sistema de armazenamento padrão (guardando as fotos dos alunos).
    - `**whitenoise - 6.12.0**` | Serve para hospedar e entregar os arquivos estáticos (CSS, JS, imagens do layout) de forma eficiente direto da sua aplicação, essencial para quando a aplicação está em produção (deploy no Render).
    - `**dj-database-url - 3.1.2**` | Serve para permitir a configuração do banco de dados no Django através de uma única variável de ambiente URL (como `DATABASE_URL=sqlite:///db.sqlite3` ou URLs de bancos Postgres).
    - `**psycopg2-binary - 2.9.12**` | Driver do banco de dados PostgreSQL. Serve para permitir que o Django se conecte e converse com bancos de dados Postgres, frequentemente usados em ambientes de produção como o Render.
    - `**gunicorn - 25.3.0**` | Servidor WSGI para Python. Serve como o servidor de produção para rodar a aplicação web Django quando está em deploy, pois o servidor embutido do Django não é feito para lidar com tráfego real.
    - `**pillow - 12.2.0**` | Biblioteca de processamento de imagens do Python. Serve para que o Django consiga lidar e processar os campos de imagem (`ImageField`) nos seus modelos.
  

---

## 📂 Estrutura do Projeto

- `/Server/core/`: Aplicativo principal com os modelos (`DadosPessoais`, `Projeto`) e templates base (`base.html`).
- `/Server/portifolio/`: Aplicativo responsável pelas visualizações (views) principais (`home`, `projetos`, `contato`) e formulários.
- `/Server/projeto/`: Configurações centrais do Django (`settings.py`, `urls.py`).
- `/Server/media/`: Diretório onde as imagens (como a foto de perfil e imagens dos projetos) são salvas.
