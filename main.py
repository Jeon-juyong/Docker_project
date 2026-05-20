from fastapi import FastAPI
from courses import course_router
import uvicorn

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
        "msg": "수강기록 API 서버입니다!"
    }

app.include_router(course_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)