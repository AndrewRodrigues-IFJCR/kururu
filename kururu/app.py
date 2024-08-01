from fastapi import FastAPI
from settings import SessionSettings
from starlette.middleware.sessions import SessionMiddleware

settings = SessionSettings()
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=settings.SESSION_SECRET_KEY)
