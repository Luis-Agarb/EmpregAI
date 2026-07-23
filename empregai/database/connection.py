"""
Database connection management.
"""

from urllib.parse import quote_plus

from sqlalchemy import Engine, create_engine

from empregai.config.settings import settings


def get_connection_url(database: str | None = None) -> str:
    """
    Build the SQL Server connection URL.

    Args:
        database: Optional database name. If omitted,
                  the configured database is used.

    Returns:
        SQLAlchemy connection URL.
    """

    db_name = database or settings.DB_NAME

    connection_string = (
        f"DRIVER={{{settings.DB_ODBC_DRIVER}}};"
        f"SERVER={settings.DB_SERVER};"
        f"DATABASE={db_name};"
        f"Trusted_Connection={settings.DB_TRUSTED_CONNECTION};"
        f"Encrypt={settings.DB_ENCRYPT};"
        f"TrustServerCertificate={settings.DB_TRUST_SERVER_CERTIFICATE};"
    )

    return (
        "mssql+pyodbc:///?odbc_connect="
        + quote_plus(connection_string)
    )


def create_sqlalchemy_engine(database: str | None = None) -> Engine:
    """
    Create a SQLAlchemy Engine.
    """

    return create_engine(
        get_connection_url(database),
        pool_pre_ping=True,
        future=True,
    )