from fastapi import FastAPI
import uvicorn
import logging
import sys
import json
from fastapi.exceptions import HTTPException

app = FastAPI()
logging.basicConfig(level=logging.INFO,stream=sys.stdout,filemode='w')

books = None
try:
    with open("db.json", "r") as db_json:
        books = json.load(db_json)['books']
except FileNotFoundError as ex:
    logging.error("%s", str(ex))

@app.get('/books')
async def get_books():
    if books is None:
        raise HTTPException(404 ,"messge: No books found")
    return {"statusCode": 200, "message": f"books: {books}"}

@app.get('/books/{name}')
async def get_book(name: str):
    if books is None:
        raise HTTPException(404 ,"messge: No books found")
    for book in books:
        if book['name'] == name.title():
            return {"statusCode": 200, "message": f"Name: {book['name']}, Author: {book['author']}"}
    raise HTTPException(404 ,f"messge: No book by the name of {name.title()}")

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8001, log_level="info")