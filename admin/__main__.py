from fastapi import FastAPI
from sqladmin import Admin
from src.types.settings import settings
from fastapi.middleware.cors import CORSMiddleware
from admin.auth import AdminAuth
from src.database.models import Base
from .model_views import UserAdmin, TaskAdmin

app = FastAPI()

app.add_middleware(middleware_class=CORSMiddleware,
                   **{'allow_methods': ('*',), 'allow_origins': ('*',),
                      'allow_headers': ('*',), 'allow_credentials': True})

sqladmin_auth_backend = AdminAuth(secret_key=settings.SECRET_KEY.get_secret_value())
admin = Admin(
    engine=Base.engine,
    app=app,
    authentication_backend=sqladmin_auth_backend,
    title="Админ панель",
    templates_dir=settings.BASE_DIR / "templates/admin",
)
admin.add_view(UserAdmin)
admin.add_view(TaskAdmin)

if __name__ == '__main__':
    from uvicorn import run

    run(
        app=app,
        host="0.0.0.0",
        port=8050,
    )
