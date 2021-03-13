from datetime import datetime
from ninja import Schema


class UserSchema(Schema):
    id: int
    username: str
    email: str


class ArticleIn(Schema):
    author: int
    title: str
    content: str


class ArticleOut(Schema):
    id: int
    author: UserSchema
    created: datetime
    updated: datetime
    title: str
    content: str
