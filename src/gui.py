from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastui import FastUI, AnyComponent, prebuilt_html, components as c
from fastui.components.display import DisplayLookup
from fastui.events import GoToEvent, BackEvent
from sqlmodel import Session, select

from .models import Hero
from .db_env import engine

router = APIRouter()


@router.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def heroes_table() -> list[AnyComponent]:
    """
    Show a table of all heroes.
    """
    with Session(engine) as session:
        heroes = session.exec(select(Hero)).all()
    return [
        c.Page(
            components=[
                c.Heading(text="Heroes", level=2),
                c.Table(
                    data=heroes,
                    columns=[
                        # Hero's name as a clickable link to their profile
                        DisplayLookup(
                            field="name", on_click=GoToEvent(url="/hero/{id}/")
                        ),
                        # Display secret name
                        DisplayLookup(field="secret_name", title="Secret Name"),
                        # Display age as text
                        DisplayLookup(field="age", title="Age"),
                    ],
                ),
            ]
        ),
    ]


@router.get(
    "/api/hero/{hero_id}/", response_model=FastUI, response_model_exclude_none=True
)
def hero_profile(hero_id: int) -> list[AnyComponent]:
    """
    Hero profile page.
    """
    with Session(engine) as session:
        hero = session.get(Hero, hero_id)
        if not hero:
            raise HTTPException(status_code=404, detail="Hero not found")
    return [
        c.Page(
            components=[
                c.Heading(text=hero.name, level=2),
                c.Link(components=[c.Text(text="Back")], on_click=BackEvent()),
                c.Details(data=hero),
            ]
        ),
    ]


@router.get("/", response_class=HTMLResponse)
@router.get("/{path:path}", response_class=HTMLResponse)
async def html_landing() -> HTMLResponse:
    """Serve the React app."""
    return HTMLResponse(prebuilt_html(title="Heroes UI Demo"))
