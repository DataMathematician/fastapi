from fastapi import Depends, FastAPI

from sql_app import models
from sql_app.database import engine

from routers import admin, users, items, pages

models.Base.metadata.create_all(bind=engine)

description = """
Приложение управления данными в СберФакторинг 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_implemented_).
* **Read users** (_implemented_).
"""

app = FastAPI(
    title='FactoringInfo',
    description=description,
    version='0.1.1',
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Волков Георгий",
        "url": "http://SBERFACTORING_CONFLUENCE",
        "email": "GAVolkov@sberfactoring.com",},
    license_info={
        "name": "SberFactoring",
        "url": "https://sberfactoring.ru/",},
    
)


app.include_router(admin.router)
app.include_router(items.router)
app.include_router(users.router)
app.include_router(pages.router)

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Request

from .library.helpers import *

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """
    Главная страница
    """
    data = openfile("home.md")
    return templates.TemplateResponse("page.html", {"request": request, 
                                                    "data": data})


