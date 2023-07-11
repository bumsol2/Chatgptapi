from typing import Optional
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

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

class Item(BaseModel):
    name: str
    price: int

@app.post("/items/{item_id}")
def create_item(item_id:int, item:Item):
    if item_id in items:
        return {"error": "there is already existing key"}
    items[item_id] = item.dict()
    return {"succes": "ok"}


class ItemForUpdate(BaseModel):
    name: Optional[str]
    price: Optional[int] 

@app.put("/items/{item_id}")
def update_item(item_id:int, item: ItemForUpdate):
    if item_id not in items:
        return {"error": "there is no item id: {item_id}"}

    if item.name:
        items[item_id]['name'] = item.name
    
    if item.price:
        items[item_id]['price'] = item.price
    
    return {"succes": "ok"}

@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    items.pop(item_id)
    return {"succes": "ok"}