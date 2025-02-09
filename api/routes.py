from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from models import Book
from database.config import collection_name
from database.schemas import list_serial
from bson import ObjectId
from security import encode_token, get_current_user  
import os
from dotenv import load_dotenv

if not os.getenv("ADMIN_USERNAME"):
    load_dotenv()

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

router = APIRouter()

# show all the data
@router.get("/")
async def get_books():
    books = list_serial(collection_name.find())
    return books

# log in to perform post, put, and delete operations
@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != ADMIN_USERNAME or form_data.password != ADMIN_PASSWORD:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = encode_token({"username": ADMIN_PASSWORD})
    return { "access_token": token }

@router.post("/")
async def post_book(book: Book, user: dict = Depends(get_current_user)):
    collection_name.insert_one(book.model_dump())
    return {"message": "Book inserted successfully"}

@router.put("/{id}")
async def put_book(id: str, book: Book, user: dict = Depends(get_current_user)):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": book.model_dump()})
    return {"message": f"Book {id} updated successfully"}

@router.delete("/{id}")
async def delete_book(id: str, user: dict = Depends(get_current_user)):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": f"Book {id} deleted successfully"}