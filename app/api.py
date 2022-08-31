from fastapi import Depends, FastAPI

from sql_app import models
from sql_app.database import engine

from routers import admin, users, items, pages

models.Base.metadata.create_all(bind=engine)

description = """
Сервис управления данными СберФакторинг 🚀

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
        "url": "https://confluence.sberfactoring.ru/pages/viewpage.action?pageId=74848322",
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

from fastapi.middleware.wsgi import WSGIMiddleware
from app.data.dash1.plot import create_dash_app

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates2")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """
    Главная страница
    """
    data = openfile("home.md")
    return templates.TemplateResponse("base.html", {"request": request, # page.html
                                                    "data": data})

@app.get("/dataregistry", response_class=HTMLResponse)
async def dataregistry(request: Request):
    """
    Реестр данных
    """
    data = openfile("home.md")
    return templates.TemplateResponse("dataregistry.html", {"request": request, 
                                                    "data": data})


dash_app = create_dash_app(requests_pathname_prefix="/dash/")
app.mount("/dash/",WSGIMiddleware(dash_app.server))

