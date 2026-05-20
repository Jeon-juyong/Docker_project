from pydantic import BaseModel
 
class Course(BaseModel):
    course_name: str
    year: int
    semester: int
    grade: str