from sqlalchemy import text

from empregai.database.connection import create_sqlalchemy_engine


def main() -> None:
    engine = create_sqlalchemy_engine("master")

    with engine.connect() as conn:
        version = conn.execute(text("SELECT @@VERSION"))
        print(version.scalar())


if __name__ == "__main__":
    main()