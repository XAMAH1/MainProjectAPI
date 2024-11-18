import os
from dotenv import load_dotenv

load_dotenv()


ECHO_MOD = True

def get_settings_connect() -> str:
    db_port = os.getenv("PDB_PORT")
    db_user = os.getenv("PDB_USER")
    db_pass = os.getenv("PDB_PASSWORD")
    db_host = os.getenv("PDB_HOST")
    db_name = os.getenv("PDB_BASE")

    return f"postgresql+asyncpg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    # return f"postgresql+pg8000://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"