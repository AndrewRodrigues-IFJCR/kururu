from fastapi import Depends, FastAPI
from fastapi.requests import Request
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.account import Account
from models.connection import get_async_session_maker
from schemas import Token
from security import (
    create_access_token,
    create_refresh_token,
    generate_password_hash,
)


def subscribe_controller(app: FastAPI):
    @app.get('/signup')
    async def _(request: Request) -> RedirectResponse:
        return RedirectResponse('/view/signup')

    @app.post('/signup', response_model=Token)
    async def _(
        account_req: OAuth2PasswordRequestForm = Depends(),
        async_session_maker=Depends(get_async_session_maker),
    ) -> Token:
        with async_session_maker() as session:
            session.add(
                account := Account(
                    username=account_req.username,
                    password=generate_password_hash(account_req.password),
                )
            )
            await session.commit()
            await session.refresh(account)

        return Token(
            access_token=create_access_token(account.id),
            refresh_token=create_refresh_token(account.id),
        )
