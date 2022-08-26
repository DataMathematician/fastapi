from fastapi import APIRouter, Depends, HTTPException

from sql_app import schemas, crud
from sql_app.database import get_db

from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/items",
    tags=['items'],
    responses={404: {"description": "Not found"}}
)


@router.get("/", response_model=list[schemas.Item])
def read_items(skip:int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db=db, skip=skip, limit=limit)
    return items