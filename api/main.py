from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from datetime import datetime

app = FastAPI(
    title="Harbor - Canonika",
    description="Dashboard principal do Canonika",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Página inicial do Harbor"""
    return {
        "service": "Harbor",
        "description": "Dashboard principal do Canonika",
        "status": "online",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/api/health")
async def health():
    """Health check do Harbor"""
    return {
        "service": "Harbor",
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }

@app.get("/api/services")
async def get_services():
    """Lista de serviços disponíveis"""
    return {
        "services": [
            {
                "name": "Quarter",
                "description": "Ponto de entrada",
                "url": "http://localhost",
                "port": 80,
                "status": "online"
            },
            {
                "name": "Guardian",
                "description": "Sistema de segurança",
                "url": "http://localhost:3705",
                "port": 3705,
                "status": "online"
            },
            {
                "name": "Fisher",
                "description": "Coleta de dados",
                "url": "http://localhost:3702",
                "port": 3702,
                "status": "offline"
            },
            {
                "name": "Ledger",
                "description": "Gestão financeira",
                "url": "http://localhost:3703",
                "port": 3703,
                "status": "offline"
            }
        ]
    }

@app.get("/api/dashboard/metrics")
async def get_dashboard_metrics():
    """Métricas do dashboard"""
    return {
        "active_users": 12,
        "total_services": 14,
        "online_services": 2,
        "offline_services": 12,
        "last_24h_requests": 1542,
        "average_response_time": 245,
        "error_rate": 0.02
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 