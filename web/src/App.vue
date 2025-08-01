<template>
  <MasterPage 
    :serviceConfig="serviceConfig"
    :hasLogin="false"
    @view-changed="handleViewChange"
    @login="handleLogin"
    @logout="handleLogout"
  >
    <!-- Dashboard -->
    <div v-if="currentView === 'dashboard'" class="canonika-view">
      <div class="view-header">
        <h2 class="view-title">Dashboard Principal</h2>
        <p class="view-subtitle">Visão geral do sistema Canonika</p>
      </div>

      <div class="dashboard-grid">
        <!-- Métricas -->
        <div class="canonika-card">
          <div class="card-header">
            <h3 class="card-title">Métricas do Sistema</h3>
            <button @click="refreshMetrics" class="refresh-btn">
              <i class="fas fa-sync-alt"></i>
            </button>
          </div>
          <div class="card-content">
            <div class="metrics-grid">
              <div class="metric-item">
                <div class="metric-value">{{ metrics.active_users }}</div>
                <div class="metric-label">Usuários Ativos</div>
              </div>
              <div class="metric-item">
                <div class="metric-value">{{ metrics.online_services }}/{{ metrics.total_services }}</div>
                <div class="metric-label">Serviços Online</div>
              </div>
              <div class="metric-item">
                <div class="metric-value">{{ metrics.last_24h_requests }}</div>
                <div class="metric-label">Requisições (24h)</div>
              </div>
              <div class="metric-item">
                <div class="metric-value">{{ metrics.average_response_time }}ms</div>
                <div class="metric-label">Tempo Médio</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Status dos Serviços -->
        <div class="canonika-card">
          <div class="card-header">
            <h3 class="card-title">Status dos Serviços</h3>
          </div>
          <div class="card-content">
            <div class="service-status" v-for="service in services" :key="service.name">
              <div class="service-info">
                <div class="service-icon">
                  <i :class="getServiceIcon(service.name)"></i>
                </div>
                <div class="service-details">
                  <span class="service-name">{{ service.name }}</span>
                  <span class="service-description">{{ service.description }}</span>
                </div>
              </div>
              <div class="service-actions">
                <span class="service-status" :class="service.status">{{ service.statusText }}</span>
                <button @click="openService(service)" class="canonika-btn canonika-btn-small">
                  Acessar
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Quarter -->
    <div v-if="currentView === 'quarter'" class="canonika-view">
      <div class="view-header">
        <h2 class="view-title">Quarter - Ponto de Entrada</h2>
        <p class="view-subtitle">Sistema de autenticação centralizada</p>
      </div>

      <div class="service-container">
        <div class="canonika-card">
          <div class="card-header">
            <h3 class="card-title">Informações do Quarter</h3>
          </div>
          <div class="card-content">
            <div class="service-info-grid">
              <div class="info-item">
                <span class="info-label">URL:</span>
                <span class="info-value">{{ config.getServiceUrl('quarter') }}</span>
              </div>
              <div class="info-item">
                <span class="info-label">Status:</span>
                <span class="info-value online">Online</span>
              </div>
              <div class="info-item">
                <span class="info-label">Função:</span>
                <span class="info-value">Ponto de entrada centralizado</span>
              </div>
            </div>
            <div class="service-actions">
              <button @click="openQuarter" class="canonika-btn canonika-btn-primary">
                <i class="fas fa-external-link-alt"></i>
                Acessar Quarter
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Guardian -->
    <div v-if="currentView === 'guardian'" class="canonika-view">
      <div class="view-header">
        <h2 class="view-title">Guardian - Segurança</h2>
        <p class="view-subtitle">Sistema de segurança e monitoramento</p>
      </div>

      <div class="service-container">
        <div class="canonika-card">
          <div class="card-header">
            <h3 class="card-title">Informações do Guardian</h3>
          </div>
          <div class="card-content">
            <div class="service-info-grid">
              <div class="info-item">
                <span class="info-label">URL:</span>
                <span class="info-value">{{ config.getServiceUrl('guardian') }}</span>
              </div>
              <div class="info-item">
                <span class="info-label">Status:</span>
                <span class="info-value online">Online</span>
              </div>
              <div class="info-item">
                <span class="info-label">Função:</span>
                <span class="info-value">Segurança e monitoramento</span>
              </div>
            </div>
            <div class="service-actions">
              <button @click="openGuardian" class="canonika-btn canonika-btn-primary">
                <i class="fas fa-external-link-alt"></i>
                Acessar Guardian
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Fisher -->
    <div v-if="currentView === 'fisher'" class="canonika-view">
      <div class="view-header">
        <h2 class="view-title">Fisher - Coleta de Dados</h2>
        <p class="view-subtitle">Sistema de coleta e processamento de dados</p>
      </div>

      <div class="service-container">
        <div class="canonika-card">
          <div class="card-header">
            <h3 class="card-title">Informações do Fisher</h3>
          </div>
          <div class="card-content">
            <div class="service-info-grid">
              <div class="info-item">
                <span class="info-label">URL:</span>
                <span class="info-value">{{ config.getServiceUrl('fisher') }}</span>
              </div>
              <div class="info-item">
                <span class="info-label">Status:</span>
                <span class="info-value offline">Offline</span>
              </div>
              <div class="info-item">
                <span class="info-label">Função:</span>
                <span class="info-value">Coleta e processamento de dados</span>
              </div>
            </div>
            <div class="service-actions">
              <button @click="openFisher" class="canonika-btn canonika-btn-primary">
                <i class="fas fa-external-link-alt"></i>
                Acessar Fisher
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Ledger -->
    <div v-if="currentView === 'ledger'" class="canonika-view">
      <div class="view-header">
        <h2 class="view-title">Ledger - Financeiro</h2>
        <p class="view-subtitle">Sistema financeiro e contábil</p>
      </div>

      <div class="service-container">
        <div class="canonika-card">
          <div class="card-header">
            <h3 class="card-title">Informações do Ledger</h3>
          </div>
          <div class="card-content">
            <div class="service-info-grid">
              <div class="info-item">
                <span class="info-label">URL:</span>
                <span class="info-value">{{ config.getServiceUrl('ledger') }}</span>
              </div>
              <div class="info-item">
                <span class="info-label">Status:</span>
                <span class="info-value offline">Offline</span>
              </div>
              <div class="info-item">
                <span class="info-label">Função:</span>
                <span class="info-value">Sistema financeiro</span>
              </div>
            </div>
            <div class="service-actions">
              <button @click="openLedger" class="canonika-btn canonika-btn-primary">
                <i class="fas fa-external-link-alt"></i>
                Acessar Ledger
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Usuários -->
    <div v-if="currentView === 'users'" class="canonika-view">
      <div class="view-header">
        <h2 class="view-title">Gestão de Usuários</h2>
        <p class="view-subtitle">Administração de usuários do sistema</p>
      </div>

      <div class="users-container">
        <div class="canonika-card">
          <div class="card-header">
            <h3 class="card-title">Usuários do Sistema</h3>
            <button @click="refreshUsers" class="refresh-btn">
              <i class="fas fa-sync-alt"></i>
            </button>
          </div>
          <div class="card-content">
            <div class="users-list">
              <div class="user-item" v-for="user in users" :key="user.id">
                <div class="user-info">
                  <div class="user-avatar">
                    <i class="fas fa-user"></i>
                  </div>
                  <div class="user-details">
                    <span class="user-name">{{ user.name }}</span>
                    <span class="user-email">{{ user.email }}</span>
                    <span class="user-role">{{ user.role }}</span>
                  </div>
                </div>
                <div class="user-actions">
                  <button @click="editUser(user)" class="canonika-btn canonika-btn-small">
                    <i class="fas fa-edit"></i>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </MasterPage>
</template>

<script>
import MasterPage from './components/MasterPage.vue'
import config from './config/env.js'

export default {
  name: 'App',
  components: {
    MasterPage
  },
  data() {
    return {
      currentView: 'dashboard',
      
      // Configuração do serviço Harbor
      serviceConfig: {
        name: 'HARBOR',
        description: 'Dashboard Principal do Sistema',
        iconClass: 'fas fa-anchor',
        menuItems: [
          {
            id: 'dashboard',
            title: 'Dashboard',
            icon: 'fas fa-tachometer-alt',
            subtitle: 'Visão Geral'
          },
          {
            id: 'quarter',
            title: 'Quarter',
            icon: 'fas fa-home',
            subtitle: 'Ponto de Entrada'
          },
          {
            id: 'guardian',
            title: 'Guardian',
            icon: 'fas fa-shield-alt',
            subtitle: 'Segurança'
          },
          {
            id: 'fisher',
            title: 'Fisher',
            icon: 'fas fa-fish',
            subtitle: 'Coleta de Dados'
          },
          {
            id: 'ledger',
            title: 'Ledger',
            icon: 'fas fa-book',
            subtitle: 'Financeiro'
          },
          {
            id: 'users',
            title: 'Usuários',
            icon: 'fas fa-users',
            subtitle: 'Gestão'
          }
        ]
      },
      user: {
        id: 'admin-001',
        name: 'Administrador',
        email: 'admin@canonika.io',
        role: 'Administrador'
      },
      
      // Métricas do dashboard
      metrics: {
        active_users: 12,
        total_services: 14,
        online_services: 2,
        offline_services: 12,
        last_24h_requests: 1542,
        average_response_time: 245,
        error_rate: 0.02
      },
      
      // Serviços disponíveis
      services: [
        {
          name: 'Quarter',
          description: 'Ponto de entrada',
          url: config.getServiceUrl('quarter'),
          status: 'online',
          statusText: 'Online'
        },
        {
          name: 'Guardian',
          description: 'Sistema de segurança',
          url: config.getServiceUrl('guardian'),
          status: 'online',
          statusText: 'Online'
        },
        {
          name: 'Fisher',
          description: 'Coleta de dados',
          url: config.getServiceUrl('fisher'),
          status: 'offline',
          statusText: 'Offline'
        },
        {
          name: 'Ledger',
          description: 'Sistema financeiro',
          url: config.getServiceUrl('ledger'),
          status: 'offline',
          statusText: 'Offline'
        }
      ],
      
      // Usuários
      users: [
        {
          id: 1,
          name: 'Administrador',
          email: 'admin@canonika.io',
          role: 'Administrador'
        },
        {
          id: 2,
          name: 'João Silva',
          email: 'joao@canonika.io',
          role: 'Analista'
        },
        {
          id: 3,
          name: 'Maria Santos',
          email: 'maria@canonika.io',
          role: 'Operador'
        }
      ]
    }
  },
  
  methods: {
    handleViewChange(viewId) {
      this.currentView = viewId
    },
    
    handleLogin(user) {
      this.user = user
      console.log('Usuário logado:', user)
    },
    
    handleLogout() {
      this.user = null
      console.log('Usuário deslogado')
      // Redirecionar para Quarter usando configuração
      const quarterUrl = config.getServiceUrl('quarter')
      window.location.href = quarterUrl
    },
    
    refreshMetrics() {
      // Implementar refresh das métricas
      console.log('Atualizando métricas...')
    },
    
    refreshUsers() {
      // Implementar refresh dos usuários
      console.log('Atualizando usuários...')
    },
    
    getServiceIcon(serviceName) {
      const icons = {
        'quarter': 'fas fa-home',
        'harbor': 'fas fa-anchor',
        'guardian': 'fas fa-shield-alt',
        'skipper': 'fas fa-compass',
        'beacon': 'fas fa-broadcast-tower',
        'fisher': 'fas fa-fish',
        'tollgate': 'fas fa-door-open',
        'ledger': 'fas fa-book'
      }
      return icons[serviceName.toLowerCase()] || 'fas fa-cog'
    },
    
    openService(service) {
      if (service.status === 'online') {
        window.open(service.url, '_blank')
      }
    },
    
    openQuarter() {
      const quarterUrl = config.getServiceUrl('quarter')
      window.open(quarterUrl, '_blank')
    },
    
    openGuardian() {
      const guardianUrl = config.getServiceUrl('guardian')
      window.open(guardianUrl, '_blank')
    },
    
    openFisher() {
      const fisherUrl = config.getServiceUrl('fisher')
      window.open(fisherUrl, '_blank')
    },
    
    openLedger() {
      const ledgerUrl = config.getServiceUrl('ledger')
      window.open(ledgerUrl, '_blank')
    },
    
    editUser(user) {
      // Implementar edição de usuário
      console.log('Editando usuário:', user.name)
    },

    // Métodos para comunicação com outros serviços
    async checkServiceHealth(serviceName) {
      const healthUrl = config.buildHealthUrl(serviceName)
      try {
        const response = await fetch(healthUrl)
        return response.ok
      } catch (error) {
        console.error(`Erro ao verificar ${serviceName}:`, error)
        return false
      }
    },

    async getGuardianMetrics() {
      const guardianUrl = config.getServiceUrl('guardian')
      const metricsUrl = `${guardianUrl}/api/metrics`
      try {
        const response = await fetch(metricsUrl)
        return await response.json()
      } catch (error) {
        console.error('Erro ao buscar métricas do Guardian:', error)
        return {}
      }
    },

    async getQuarterUsers() {
      const quarterUrl = config.getServiceUrl('quarter')
      const usersUrl = `${quarterUrl}/api/users`
      try {
        const response = await fetch(usersUrl)
        return await response.json()
      } catch (error) {
        console.error('Erro ao buscar usuários do Quarter:', error)
        return []
      }
    },

    async refreshAllServices() {
      const services = ['quarter', 'guardian', 'skipper', 'beacon', 'fisher', 'tollgate', 'ledger']
      const healthChecks = await Promise.allSettled(
        services.map(service => this.checkServiceHealth(service))
      )
      
      // Atualizar status dos serviços
      this.services = this.services.map((service, index) => {
        const serviceName = service.name.toLowerCase()
        const isHealthy = healthChecks.find((check, i) => 
          services[i] === serviceName && check.status === 'fulfilled' && check.value
        )
        
        return {
          ...service,
          status: isHealthy ? 'online' : 'offline',
          statusText: isHealthy ? 'Online' : 'Offline'
        }
      })
    }
  },

  mounted() {
    // Inicializar configurações
    console.log('Configurações carregadas:', {
      quarter: config.getServiceUrl('quarter'),
      harbor: config.getServiceUrl('harbor'),
      guardian: config.getServiceUrl('guardian'),
      skipper: config.getServiceUrl('skipper'),
      beacon: config.getServiceUrl('beacon'),
      fisher: config.getServiceUrl('fisher'),
      tollgate: config.getServiceUrl('tollgate'),
      ledger: config.getServiceUrl('ledger')
    })
    
    // Atualizar status dos serviços
    this.refreshAllServices()
  }
}
</script>

<style scoped>
/* Reset CSS Universal */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body {
  margin: 0 !important;
  padding: 0 !important;
  border: none !important;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  width: 100%;
  height: 100%;
  overflow-x: hidden;
}

/* App Container */
.canonika-app {
  min-height: 100vh;
  background: linear-gradient(135deg, #1e293b 0%, #334155 50%, #475569 100%);
  color: #e2e8f0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Header */
.canonika-header {
  background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 50%, #1e40af 100%);
  padding: 1rem 2rem;
  position: relative;
  overflow: hidden;
  height: 60px;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  z-index: 2;
  height: 100%;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.logo-icon {
  position: relative;
  width: 2.5rem;
  height: 2.5rem;
}

.logo-hexagon {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
  clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-pulse {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 0.25rem;
  height: 0.25rem;
  background: #ffffff;
  border-radius: 50%;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
  50% { opacity: 0.7; transform: translate(-50%, -50%) scale(1.1); }
}

.logo-text-container {
  display: flex;
  flex-direction: column;
}

.logo-text {
  font-size: 1.5rem;
  font-weight: 700;
  color: #ffffff;
  letter-spacing: 0.1em;
  margin: 0;
}

.logo-subtitle {
  font-size: 0.8rem;
  color: #94a3b8;
  font-weight: 500;
  letter-spacing: 0.05em;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.system-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.8rem;
  color: #94a3b8;
}

.status-indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.status-indicator.online {
  background: #10b981;
  animation: pulse 2s infinite;
}

.logout-btn {
  background: rgba(239, 68, 68, 0.2);
  border: 1px solid #ef4444;
  color: #ef4444;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.8rem;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.logout-btn:hover {
  background: #ef4444;
  color: white;
}

/* Layout */
.canonika-layout {
  display: flex;
  min-height: calc(100vh - 60px);
}

/* Sidebar */
.canonika-sidebar {
  width: 280px;
  background: rgba(30, 41, 59, 0.9);
  border-right: 1px solid #475569;
  padding: 1rem 0;
  backdrop-filter: blur(10px);
}

.sidebar-header {
  padding: 0 1.5rem 1rem;
  border-bottom: 1px solid #475569;
  margin-bottom: 1rem;
}

.nav-icon {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #94a3b8;
  font-size: 0.8rem;
  font-weight: 600;
}

.nav-icon.active {
  color: #3b82f6;
}

.nav-dot {
  width: 6px;
  height: 6px;
  background: currentColor;
  border-radius: 50%;
}

.nav-menu {
  list-style: none;
}

.nav-item {
  margin-bottom: 0.5rem;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.75rem 1.5rem;
  color: #94a3b8;
  cursor: pointer;
  transition: all 0.3s;
  border-radius: 0 8px 8px 0;
}

.nav-link:hover {
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
}

.nav-item.active .nav-link {
  background: rgba(59, 130, 246, 0.2);
  color: #3b82f6;
  border-right: 3px solid #3b82f6;
}

.nav-icon {
  width: 20px;
  text-align: center;
}

.nav-text {
  display: flex;
  flex-direction: column;
}

.nav-title {
  font-weight: 600;
  font-size: 0.9rem;
}

.service-subtitle {
  font-size: 0.7rem;
  color: #64748b;
  margin-top: 0.1rem;
}

/* Main Content */
.canonika-main {
  flex: 1;
  padding: 2rem;
  overflow-y: auto;
}

.canonika-view {
  max-width: 1200px;
}

.view-header {
  margin-bottom: 2rem;
}

.view-title {
  font-size: 2rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 0.5rem;
}

.view-subtitle {
  color: #94a3b8;
  font-size: 1rem;
}

/* Cards */
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 1.5rem;
}

.canonika-card {
  background: rgba(30, 41, 59, 0.9);
  border: 1px solid #475569;
  border-radius: 12px;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 1px solid #475569;
}

.card-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: #ffffff;
}

.card-content {
  padding: 1.5rem;
}

.refresh-btn {
  background: none;
  border: none;
  color: #94a3b8;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 6px;
  transition: all 0.3s;
}

.refresh-btn:hover {
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
}

/* Metrics */
.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
}

.metric-item {
  text-align: center;
  padding: 1rem;
  background: rgba(51, 65, 85, 0.5);
  border-radius: 8px;
  border: 1px solid #475569;
}

.metric-value {
  font-size: 2rem;
  font-weight: 700;
  color: #3b82f6;
  margin-bottom: 0.5rem;
}

.metric-label {
  font-size: 0.8rem;
  color: #94a3b8;
}

/* Service Status */
.service-status {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 0;
  border-bottom: 1px solid #334155;
}

.service-status:last-child {
  border-bottom: none;
}

.service-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.service-icon {
  width: 40px;
  height: 40px;
  background: rgba(59, 130, 246, 0.1);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3b82f6;
}

.service-details {
  display: flex;
  flex-direction: column;
}

.service-name {
  font-weight: 600;
  color: #ffffff;
}

.service-description {
  font-size: 0.8rem;
  color: #94a3b8;
  margin-top: 0.2rem;
}

.service-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.service-status {
  font-size: 0.8rem;
  font-weight: 600;
}

.service-status.online {
  color: #10b981;
}

.service-status.offline {
  color: #ef4444;
}

/* Buttons */
.canonika-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  text-decoration: none;
  justify-content: center;
}

.canonika-btn-primary {
  background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
  color: white;
}

.canonika-btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(59, 130, 246, 0.3);
}

.canonika-btn-secondary {
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
  border: 1px solid #3b82f6;
}

.canonika-btn-secondary:hover {
  background: #3b82f6;
  color: white;
}

.canonika-btn-secondary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.canonika-btn-small {
  padding: 0.5rem 0.75rem;
  font-size: 0.8rem;
}

/* Service Info */
.service-container {
  display: grid;
  gap: 1.5rem;
}

.service-info-grid {
  display: grid;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.info-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem;
  background: rgba(51, 65, 85, 0.5);
  border-radius: 6px;
}

.info-label {
  color: #94a3b8;
  font-size: 0.9rem;
}

.info-value {
  font-weight: 600;
}

.info-value.online {
  color: #10b981;
}

.info-value.offline {
  color: #ef4444;
}

.service-actions {
  display: flex;
  justify-content: center;
}

/* Users */
.users-container {
  display: grid;
  gap: 1.5rem;
}

.users-list {
  display: grid;
  gap: 0.5rem;
}

.user-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  background: rgba(51, 65, 85, 0.5);
  border-radius: 8px;
  border: 1px solid #475569;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.user-avatar {
  width: 40px;
  height: 40px;
  background: rgba(59, 130, 246, 0.1);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3b82f6;
}

.user-details {
  display: flex;
  flex-direction: column;
}

.user-name {
  font-weight: 600;
  color: #ffffff;
}

.user-email {
  font-size: 0.8rem;
  color: #94a3b8;
}

.user-role {
  font-size: 0.7rem;
  color: #64748b;
  margin-top: 0.1rem;
}

.user-actions {
  display: flex;
  gap: 0.5rem;
}

/* Responsive */
@media (max-width: 768px) {
  .canonika-sidebar {
    width: 100%;
    position: fixed;
    bottom: 0;
    left: 0;
    z-index: 1000;
    border-right: none;
    border-top: 1px solid #475569;
  }
  
  .canonika-main {
    margin-bottom: 80px;
  }
  
  .dashboard-grid {
    grid-template-columns: 1fr;
  }
  
  .metrics-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style> 