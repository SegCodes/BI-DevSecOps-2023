from fastapi import FastAPI
import uvicorn
import logging
import sys
import json
from fastapi.exceptions import HTTPException

app = FastAPI()
logging.basicConfig(level=logging.INFO,stream=sys.stdout,filemode='w')

authors = None
try:
    with open("db.json", "r") as db_json:
        authors = json.load(db_json)['authors']
except FileNotFoundError as ex:
    logging.error("%s", str(ex))

@app.get('/')
async def get_root():
    return {"message": "Welcome to the book store!"}

@app.get('/authors')
async def get_authors():
    if authors is None:
        raise HTTPException(404 , "message: No authors found")
    return {"statusCode": 200, "message": f"authors: {authors}"}

@app.get('/authors/{name}')
async def get_author(name: str):
    if authors is None:
        raise HTTPException(404 , "message: No authors found")
    else:
        for author in authors:
            if author['name'] == name.title():
                return {"statusCode": 200, "message": f"Name: {author['name']}"}
    raise HTTPException(404 ,f"messge: No author by the name of {name.title()}")

# if __name__ == "__main__":
#      uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")