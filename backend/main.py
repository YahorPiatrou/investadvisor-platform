from fastapi import FastAPI
from app.api.v1 import auth, profile, portfolio, recommendations

app = FastAPI(
    title="InvestAdvisor API",
    description="Интеллектуальная система рекомендаций инвестиционных портфелей",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(profile.router, prefix="/profile", tags=["profile"])
app.include_router(portfolio.router, prefix="/portfolio", tags=["portfolio"])
app.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"])

@app.get("/")
async def root():
    return {"message": "InvestAdvisor API запущен. Документация: /docs"}
