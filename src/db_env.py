from sqlmodel import create_engine
from dotenv import dotenv_values

config = dotenv_values(".env")

driver = "postgresql"
connection_type = "localhost"
postgres_username = config.get("POSTGRES_USER")
postgres_password = config.get("POSTGRES_PASSWORD")
postgres_database_name = config.get("POSTGRES_DB")
postgres_port = config.get("PORT", 5432)

DATABASE_URL = (
    f"{driver}://{postgres_username}:{postgres_password}@"
    f"{connection_type}:{postgres_port}/{postgres_database_name}"
)

engine = create_engine(DATABASE_URL)
