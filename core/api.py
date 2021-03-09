from ninja import files
from .schemas import Filters, Item, PathDate
from typing import List
from django.db import router
from django.utils.translation import ugettext_lazy as _
from ninja import Body, Cookie,  File, Form, Header, Path, Query, Router
from ninja.files import UploadedFile


from django.contrib.auth import get_user_model
User = get_user_model()


router = Router()

# path parameters


@router.post('/events/{year}/{month}/{date}')
def events(request, date: PathDate = Path(...)):
    return{"date": date.value()}


# Query Parameters
weapons = ['Ninjato', 'Shuriken', 'Katana', 'Katana',
           'Kama', 'Kunai', 'Naginata', 'Yari']


@router.get('weapons/search')
def search_weapons(request, q: str, offset: int = 0):
    results = [w for w in weapons if q in w.lower()]
    print(q, results)
    return results[offset: offset+10]


@router.get('/filter')
def events(request, filters: Filters = Query(...)):
    return{"filters": filters.dict()}

# request body


@router.post('/items')
def create_item(request, item: Item):
    return item

# request body+path parameters


@router.put('items/{item_id}')
def update(request, item_id: int, item: Item):
    return {"item_id": item_id, "item": item.dict()}

# request body + path + query parameters


@router.put('/items2/{item_id}')
def update(request, item_id: int, item: Item, q: str):
    return {"item_id": item_id, "item": item.dict(), "q": q}


'''
The function parameters will be recognized as follows:

If the parameter is also declared in the path, it will be used as a path parameter.
If the parameter is of a singular type (like int, float, str, bool, etc.), it will be interpreted as a query parameter.
If the parameter is declared to be of the type of Schema (or Pydantic BaseModel), it will be interpreted as a request body.
'''

# Form Data
@router.post('/login')
def login(request, username: str = Form(...), password: str = Form(...)):
    return{"usernme": username, "password": '*****'}

# File Upload
@router.post('/updload')
def upload(request, file: UploadedFile = File(...)):
    #chuncks, multiple_chunks, size
    data = file.read()
    return {'name': file.name, 'len': len(data)}