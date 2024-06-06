from sqladmin.authentication import AuthenticationBackend
from fastapi import Request
from src.types.settings import settings


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        """Validate username/password credentials and update session"""
        form = await request.form()
        username, password = form["username"], form["password"]

        if username == settings.DEFAULT_USERNAME and password == settings.DEFAULT_PASSWORD:
            request.session.update({"token": settings.SECRET_KEY.get_secret_value()})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        """logout logic"""
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        """Token check"""
        token = request.session.get("token")

        if not token:
            return False

        return True
