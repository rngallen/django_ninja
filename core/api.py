from .schemas import PathDate
from typing import List
from django.db import router
from django.utils.translation import ugettext_lazy as _
from ninja import Router, Path


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

