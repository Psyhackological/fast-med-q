# db_config.py
from dotenv import dotenv_values

# Load environment variables from .env
config = dotenv_values(".env")

# Set driver to use asyncpg for async PostgreSQL connections
driver = "postgresql+asyncpg"
connection_type = config.get("HOST", "localhost")
postgres_username = config.get("POSTGRES_USER")
postgres_password = config.get("POSTGRES_PASSWORD")
postgres_database_name = config.get("POSTGRES_DB")
postgres_port = config.get("PORT", "5432")

# Build the async connection string
DATABASE_URL = (
    f"{driver}://{postgres_username}:{postgres_password}@"
    f"{connection_type}:{postgres_port}/{postgres_database_name}"
)

# Print it for debug (optional)
print("DATABASE_URL =", DATABASE_URL)
