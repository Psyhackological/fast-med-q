from typing import List

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Session, SQLModel, select, func
from .models import Hero
from .db_env import engine
from .gui import router as gui_router

app = FastAPI()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    with Session(engine) as session:
        # Use func.count() to get the number of heroes
        heroes_count = session.exec(select(func.count()).select_from(Hero)).one()
        if heroes_count == 0:
            initial_heroes = [
                Hero(name="Deadpond", secret_name="Dive Wilson"),
                Hero(name="Spider-Boy", secret_name="Pedro Parqueador"),
                Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48),
            ]
            session.add_all(initial_heroes)
            session.commit()


@app.post("/heroes/", response_model=Hero)
def create_hero(hero: Hero, session: Session = Depends(get_session)):
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero


@app.get("/heroes/", response_model=List[Hero])
def read_heroes(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    session: Session = Depends(get_session),
):
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes


@app.get("/heroes/{hero_id}", response_model=Hero)
def read_hero(hero_id: int, session: Session = Depends(get_session)):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@app.delete("/heroes/{hero_id}")
def delete_hero(hero_id: int, session: Session = Depends(get_session)):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"ok": True}


app.include_router(gui_router)
