import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "postgresql+psycopg://disciplinas_uvv:disciplinas_uvv@localhost:5432/disciplinas_uvv_dev",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
