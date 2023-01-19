from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

posts = []


class Post(BaseModel):
    id: str
    title: str


@app.get('/')
def read_root():
    return {"cl": "Fabio Arango Grajales"}


@app.get('/post')
def get_post():
    return posts


@app.post('/pots')
def save_post(post: Post):
    posts.append(post.dict())
    return 'received'
