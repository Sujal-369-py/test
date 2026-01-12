from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = AsyncIOMotorClient(os.getenv("MONGO_DB"))
db = client["test_subject_1"]["users"]

class Student(BaseModel):
    name: str
    dept: str
    age: int

@app.post("/add-stud")
async def add_student(stud: Student):
    result = await db.insert_one(stud.dict())
    return {
        "message": "Student added",
        "id": str(result.inserted_id)
    }
