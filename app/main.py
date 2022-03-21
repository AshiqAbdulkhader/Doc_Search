from fastapi import FastAPI
from pydantic import BaseModel
import json
from docsearch import query
app = FastAPI()


class Item(BaseModel):
    id: str
    lang: str
    query: str


@app.post("/search/")
async def search(item: Item):
    result = query(item.query)
    data = {
        'id': item.id,
        'result': result
    }
    data = json.dumps(data)
    return data
