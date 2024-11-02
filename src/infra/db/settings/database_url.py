from decouple import config as decouple_config

def get_database_url() -> str:
    """Returns the database URL assembled from environment variables."""
    return (
        f"{decouple_config('DB_DIALECT_DRIVER')}://"
        f"{decouple_config('DB_USER')}:"
        f"{decouple_config('DB_PASSWORD')}@"
        f"{decouple_config('DB_HOST')}:"
        f"{decouple_config('DB_PORT')}/"
        f"{decouple_config('DB_NAME')}"
    )
