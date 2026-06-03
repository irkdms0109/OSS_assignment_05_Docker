from fastapi import FastAPI
from model import Course
import uvicorn
import json

app = FastAPI()

DATA_FILE = "courses.json"


@app.get("/")
async def root():
    return {
        "msg": "FastAPI Course Records Server"
    }


@app.get("/courses")
async def get_courses():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


@app.post("/courses")
async def add_course(course: Course):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    data.append(course.model_dump())

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return {
        "msg": "course added successfully",
        "added_course": course
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)