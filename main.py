from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


class Database:
    def __init__(
        self,
        driver: str = "postgresql",
        username: str = "postgres",
        password: str = "mysecretpassword",
        connection_type: str = "localhost",
        port: int = 5432,
        database_name: str = "postgres",
    ):
        self.engine = create_engine(
            f"{driver}://{username}:{password}@{connection_type}:{port}/{database_name}"
        )

        self.hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
        self.hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
        self.hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
        self.heroes = [self.hero_1, self.hero_2, self.hero_3]

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


if "__main__" == __name__:
    my_database = Database()
    my_database.create_db()
    my_database.select_hero("Spider-Boy")
