from fastapi import APIRouter, Form
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from app.library.helpers import *

import os                      # .env
from dotenv import load_dotenv # .env
load_dotenv()                  # .env

router = APIRouter(
    prefix="/pages",
    tags=['pages'],
)


templates = Jinja2Templates(directory="templates")
router.mount("/static", StaticFiles(directory="static"), name="static")

@router.get("/{page_name}", response_class=HTMLResponse)
async def show_page(request: Request, page_name: str):
    data = openfile(page_name+".md")
    return templates.TemplateResponse("page.html", {"request":request,
                                                    "data":data})
                                            

@router.get("/topnav/{page_name}", response_class=HTMLResponse)
async def topnav(request: Request, page_name: str):
    key = os.getenv("unsplash_key") # .env
    print(key)  #.env
    if page_name == 'twoforms':
        result = 'Введите число'
        return templates.TemplateResponse(f"{page_name}.html", 
                                          context={'request':request,
                                                   'result': result})
    elif page_name == 'accordion':
        tag = "flower"
        result = 'Введите число'
        return templates.TemplateResponse(f"{page_name}.html", 
                                          context={'request':request,
                                                   'result': result,
                                                   'tag': tag})
    else:
        return templates.TemplateResponse(f"{page_name}.html", context={"request":request})

@router.post("/topnav/form1", response_class=HTMLResponse)
def form_post1(request: Request, number: int = Form(...)):
    result = number + 2
    return templates.TemplateResponse('twoforms.html', 
                                        context={'request':request,
                                                 'result': result,
                                                 'yournum': number})

@router.post("/topnav/form2", response_class=HTMLResponse)
def form_post2(request: Request, number: int = Form(...)):
    result = number + 100
    return templates.TemplateResponse('twoforms.html', 
                                        context={'request':request,
                                                 'result': result,
                                                 'yournum': number})


@router.post("/topnav/accordion", response_class=HTMLResponse)
def post_accordion(request: Request, tag: int = Form(...)):
    return templates.TemplateResponse('accordion.html', 
                                        context={'request':request,
                                                 'tag': tag})
