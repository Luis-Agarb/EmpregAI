from sqlalchemy.orm import sessionmaker

from empregai.database.connection import create_sqlalchemy_engine

engine = create_sqlalchemy_engine()

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)