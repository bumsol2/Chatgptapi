from typing import Union
from fastapi import FastAPI

app = FastAPI()

items = {
            0: {"name": "bread",
                "price": 1000},
            1: {"name": "water",
                "price": 500},
            2: {"name": "라면",
                "price": 1200}
            }

number: int = 10
name: str = "genji"

# Path parameter

@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = items[item_id]
    return item


@app.get("/items/{item_id}/{key}")
def read_item_and_key(item_id: int, key:str):
    item = items[item_id][key]
    return item

#Query parameter
@app.get("/item-by-name")
def read_item_by_name(name: str):
    for item_id, item in items.items():
        if item['name'] == name:
            return item
    return {"error": "data not found"}
