# Portfólio Profissional

Este é o meu projeto de portfólio profissional desenvolvido utilizando o framework web **Django**. O projeto permite exibir informações pessoais, projetos desenvolvidos e inclui um formulário de contato funcional que envia mensagens diretamente para o e-mail configurado.

## 🚀 Funcionalidades

- **Início:** Exibe os dados pessoais principais do perfil (foto, nome social, curso, período).
- **Projetos:** Lista todos os projetos acadêmicos e profissionais cadastrados.
- **Contato:** Uma página contendo os canais de contato (LinkedIn, GitHub, Telefone) e um formulário integrado que realiza o envio real de e-mails utilizando SMTP.
- **Painel Administrativo:** Gerenciamento dos dados dinâmicos do site através do painel admin padrão do Django (Modelos: `DadosPessoais` e `Projeto`).

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Django 6.0.4**
- **HTML5 e CSS3** (Estilização própria com design responsivo, variáveis de cor, etc.)
- **Banco de Dados:** SQLite3 (padrão para desenvolvimento)
- **Bibliotecas auxiliares:** `python-decouple` para o gerenciamento de variáveis de ambiente.

---

## 📂 Estrutura do Projeto

- `/Server/core/`: Aplicativo principal com os modelos (`DadosPessoais`, `Projeto`) e templates base (`base.html`).
- `/Server/portifolio/`: Aplicativo responsável pelas visualizações (views) principais (`home`, `projetos`, `contato`) e formulários.
- `/Server/projeto/`: Configurações centrais do Django (`settings.py`, `urls.py`).
- `/Server/media/`: Diretório onde as imagens (como a foto de perfil e imagens dos projetos) são salvas.
