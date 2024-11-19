from fastapi import FastAPI # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore
from pydantic import BaseModel # type: ignore

class Memo(BaseModel):
    id: str
    content: str
    
memos = []

app = FastAPI()

@app.post("/memos")
def create_memo(memo: Memo):
    memos.append(memo)
    return '메모 추가에 성공했습니다.'

@app.get("/memos")
def read_memo():
    return memos    

app.mount("/", StaticFiles(directory="static",html=True),name="static")