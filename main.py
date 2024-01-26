from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlite3

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

conn=sqlite3.connect('user_db.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)''')
conn.commit()

class User(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login (user: User):
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?',(user.username, user.password)) 
    result = cursor.fetchone()
    if result:
        return {"message":"Login successful"}
    else:
        raise HTTPException(status_code=401, detail= "Invalid credentials")

@app.post("/register")
async def  register(user: User):
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (user.username, user.password))
    conn.commit()
    return{"message":"User registered successfully"}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})
