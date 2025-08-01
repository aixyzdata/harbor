# Harbor - Dashboard Principal Canonika

## Descrição

O Harbor é o dashboard principal e interface de usuário do sistema Canonika, responsável pela navegação entre microserviços e gestão de funcionalidades.

## Funcionalidades

- **Dashboard Principal**: Interface centralizada para todos os microserviços
- **Navegação**: Acesso aos módulos Quarter, Guardian, Fisher, Ledger, etc.
- **Gestão de Usuários**: Interface para administração de usuários
- **Monitoramento**: Status dos serviços em tempo real
- **Hot Reload**: Desenvolvimento com atualizações automáticas

## Tecnologias

- **Frontend**: Vue.js 3 + Vite
- **Backend**: FastAPI (Python)
- **Proxy**: Nginx
- **Testes**: Vitest (unit) + Cypress (e2e)
- **Containerização**: Docker

## Estrutura do Projeto

```
harbor/
├── api/                 # Backend FastAPI
│   ├── main.py         # API principal
│   └── requirements.txt # Dependências Python
├── web/                # Frontend Vue.js
│   ├── src/
│   │   └── App.vue     # Componente principal
│   ├── tests/          # Testes unitários
│   ├── cypress/        # Testes e2e
│   └── package.json    # Dependências Node.js
├── nginx/              # Configuração do proxy
│   └── nginx.conf
├── Dockerfile          # Container principal
└── README.md           # Esta documentação
```

## Portas

- **3701**: Interface web (Nginx)
- **8001**: API FastAPI
- **5171**: Hot reload (desenvolvimento)

## Integração com Microserviços

O Harbor integra-se com:

- **Quarter**: Ponto de entrada (porta 80)
- **Guardian**: Sistema de segurança (porta 3705)
- **Fisher**: Coleta de dados (porta 3702)
- **Ledger**: Gestão financeira (porta 3703)
- **Beacon**: Notificações (porta 3704)
- **Echo**: Comunicação (porta 3706)
- **Diver**: Análise de dados (porta 3707)
- **Dock**: Armazenamento (porta 3708)
- **Mapmaker**: Visualização (porta 3709)
- **Seagull**: Relatórios (porta 3710)
- **Skipper**: Navegação (porta 3711)
- **Tollgate**: Cobrança (porta 3712)
- **Wayfinder**: Descoberta (porta 3713)

## Desenvolvimento

### Pré-requisitos

- Docker e Docker Compose
- Node.js 18+
- Python 3.9+

### Execução Local

```bash
# Instalar dependências
cd web && npm install

# Executar frontend (hot reload)
npm run dev

# Executar backend
cd ../api && python -m uvicorn main:app --reload --port 8001

# Executar testes
npm run test          # Unit tests
npm run test:e2e      # End-to-end tests
```

### Execução com Docker

```bash
# Build e execução
docker-compose up harbor

# Apenas build
docker build -t harbor .
```

## Testes

### Unit Tests (TDD)

```bash
npm run test
npm run test:coverage
```

### End-to-End Tests (BDD)

```bash
npm run test:e2e
npm run test:e2e:open
```

## Configuração

### Variáveis de Ambiente

- `DEV_MODE`: Habilita hot reload (true/false)
- `QUARTER_URL`: URL do Quarter (http://localhost)
- `GUARDIAN_URL`: URL do Guardian (http://localhost:3705)
- `FISHER_URL`: URL do Fisher (http://localhost:3702)
- `LEDGER_URL`: URL do Ledger (http://localhost:3703)
- `DATABASE_URL`: URL do PostgreSQL
- `REDIS_URL`: URL do Redis

## Funcionalidades Principais

### Dashboard

- **Visão Geral**: Status de todos os microserviços
- **Métricas**: KPIs em tempo real
- **Alertas**: Notificações de eventos importantes
- **Navegação Rápida**: Links diretos para cada módulo

### Gestão de Usuários

- **Perfis**: Visualização e edição de perfis
- **Permissões**: Controle de acesso granular
- **Sessões**: Gestão de sessões ativas
- **Auditoria**: Logs de atividades

### Monitoramento

- **Status dos Serviços**: Health checks em tempo real
- **Performance**: Métricas de resposta
- **Erros**: Logs de erros e exceções
- **Uso de Recursos**: CPU, memória, disco

## Status

✅ **Implementado**:
- Dashboard principal
- Navegação entre microserviços
- Hot reload em desenvolvimento
- Testes unitários e e2e
- Containerização Docker
- Integração com stack completa

🔄 **Em Desenvolvimento**:
- Métricas avançadas
- Alertas em tempo real
- Gestão de usuários
- Relatórios personalizados

📋 **Planejado**:
- Analytics avançado
- Customização de dashboards
- Integração com ferramentas externas
- API para terceiros 