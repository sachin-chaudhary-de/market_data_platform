from fastapi import FastAPI

from app.routes.oauth import router as oauth_router


app = FastAPI(title="Upstox OAuth")

app.include_router(oauth_router)