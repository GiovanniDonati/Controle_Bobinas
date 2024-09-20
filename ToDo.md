# ToDo List - Controle de Bobinas

## Fase 1: Planejamento e Definições Iniciais
- [x] **Definir os requisitos do projeto**
  - [x] Listar as funcionalidades principais (ex.: cadastro de bobinas, movimentações de produção...).
  -  [x] Escolher a arquitetura do projeto (ex.: REST API para comunicação entre backend e frontend).
- [x] **Escolher tecnologias e ferramentas**
  - [x] Banco de dados MySQL.
  - [x] Backend com Python e FastAPI / Frontend com React.
  - [x] Versionamento Git/GitHub.

## Fase 2: Configuração do Ambiente
- [x] **Configurar o repositório do projeto**
  - [x] Criar repositório Git.
  - [x] Definir e criar branch principal (`main`).
- [ ] **Configurar o ambiente de desenvolvimento**
  - [x] Configurar ambientes virtuais (virtualenv) para gerenciar dependências do Python.
  - [ ] Instalar dependências do frontend (React, Node.js, etc.).
  - [x] Instalar dependências do backend (Python, FastAPI, etc.).

## Fase 3: Backend - API e Banco de Dados
- [x] **Definir e modelar o banco de dados**
  - [x] Modelar as entidades principais (ex.: Vagas, Veículos, Usuários).
  - [x] Criar o esquema de banco de dados.
- [x] **Configurar o servidor backend**
  - [x] Configurar o servidor, Uvicorn
  - [x] Criar rotas para as principais operações CRUD (ex.: adicionar vaga, atualizar status, listar vagas).
- [ ] **Implementar autenticação e autorização**
  - [ ] Implementar login, logout e proteção de rotas (JWT, OAuth, etc.).
- [ ] **Testar rotas da API com Postman ou Insomnia**
  - [ ] Testar manualmente as rotas e a comunicação com o banco de dados.

## Fase 4: Frontend - React
- [ ] **Configurar o ambiente do React**
  - [ ] Criar o projeto React com `create-react-app`.
  - [ ] Configurar estrutura de pastas e arquivos.
- [ ] **Criar componentes principais**
  - [ ] Componente para listar vagas de estacionamento.
  - [ ] Componente para detalhes da vaga.
  - [ ] Componente de formulário para reserva/cadastro.
- [ ] **Conectar o frontend ao backend**
  - [ ] Utilizar Axios ou Fetch para fazer requisições à API.
  - [ ] Testar a comunicação entre o React e o backend Python.
- [ ] **Implementar autenticação no frontend**
  - [ ] Criar formulário de login.
  - [ ] Armazenar tokens de autenticação (ex.: JWT) no frontend (localStorage ou sessionStorage).

## Fase 5: Funcionalidades Avançadas
- [ ] **Implementar funcionalidades de atualização em tempo real (opcional)**
  - [ ] Usar WebSockets ou outra tecnologia para monitorar mudanças no status das vagas.
- [ ] **Configurar upload de imagens (opcional)**
  - [ ] Permitir upload de imagens dos veículos ou das vagas.
- [ ] **Implementar notificações e alertas (opcional)**
  - [ ] Notificar usuários sobre vagas disponíveis ou reservas.

## Fase 6: Testes e Deploy
- [ ] **Testar o sistema**
  - [ ] Implementar testes unitários (frontend e backend).
  - [ ] Fazer testes de integração para verificar a interação entre o frontend e o backend.
- [ ] **Configurar CI/CD (opcional)**
  - [ ] Configurar integração contínua e entrega contínua (ex.: GitHub Actions, Travis CI).
- [ ] **Fazer deploy do backend e frontend**
  - [ ] Deploy do backend em um serviço como Heroku, AWS ou DigitalOcean.
  - [ ] Deploy do frontend em um serviço como Vercel ou Netlify.
- [ ] **Configurar domínio e HTTPS (opcional)**
  - [ ] Registrar um domínio e configurar certificados SSL.

## Fase 7: Monitoramento e Manutenção
- [ ] **Configurar monitoramento e logs**
  - [ ] Implementar ferramentas de monitoramento de erros e logs (ex.: Sentry, LogRocket).
  - [ ] Monitorar o desempenho e o uso do sistema.
