from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select
from dotenv import dotenv_values


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


class Database:
    def __init__(
        self,
    ):
        self.config = dotenv_values(r".env")
        self.assemble_engine()

        self.hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
        self.hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
        self.hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
        self.heroes = [self.hero_1, self.hero_2, self.hero_3]

    def assemble_engine(
        self,
        driver: str = "postgresql",
        connection_type: str = "localhost",
    ):
        postgres_username = self.config.get("POSTGRES_USER")
        postgres_password = self.config.get("POSTGRES_PASSWORD")
        postgres_database_name = self.config.get("POSTGRES_DB")
        postgres_port = self.config.get("PORT")
        self.engine = create_engine(
            f"{driver}://{postgres_username}:{postgres_password}@{
                connection_type}:{postgres_port}/{postgres_database_name}"
        )

    def create_db(self):
        SQLModel.metadata.create_all(self.engine)
        with Session(self.engine) as session:
            for hero in self.heroes:
                session.add(hero)
            session.commit()

    def select_hero(self, hero_name: str) -> None:
        with Session(self.engine) as session:
            statement = select(Hero).where(Hero.name == hero_name)
            hero = session.exec(statement).first()
            print(hero)


if __name__ == "__main__":
    my_database = Database()
    my_database.create_db()
    my_database.select_hero("Rusty-Man")
