from fastapi import APIRouter
from model import Course
import json

course_router = APIRouter()

DATA_FILE = "courses.json"

def load_courses():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_courses(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@course_router.get("/courses")
async def get_courses() -> dict:
    courses = load_courses()
    return {
        "courses": courses
    }

@course_router.post("/courses")
async def add_course(course: Course) -> dict:
    courses = load_courses()
    courses.append(course.model_dump())
    save_courses(courses)
    return {
        "msg": "수강기록이 추가되었습니다."
    }