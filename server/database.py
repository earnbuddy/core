import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise



TORTOISE_ORM = {
    "connections": {"default": "sqlite://database.sqlite3"},
    "apps": {
        "models": {
            "models": ["server.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["models"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )