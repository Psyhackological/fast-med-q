from sqlmodel import Session, SQLModel, select
from .models import Hero
from .db_env import engine


class Database:
    def __init__(self):
        self.heroes = [
            Hero(name="Deadpond", secret_name="Dive Wilson"),
            Hero(name="Spider-Boy", secret_name="Pedro Parqueador"),
            Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48),
        ]

    def create_db(self):
        SQLModel.metadata.create_all(engine)
        with Session(engine) as session:
            session.add_all(self.heroes)
            session.commit()

    def select_hero(self, hero_name: str):
        with Session(engine) as session:
            statement = select(Hero).where(Hero.name == hero_name)
            hero = session.exec(statement).first()
            print(hero)


if __name__ == "__main__":
    my_database = Database()
    my_database.create_db()
    my_database.select_hero("Rusty-Man")
