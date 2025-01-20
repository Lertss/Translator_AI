from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from app import engine, get_db
import schemas
import crud
import models

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

templates = Jinja2Templates(directory="app/templates")


origins = [
    "http://127.0.0.1:8000",  # local development
    "http://localhost:8000",  # local development
]

app.add_middleware(
    CORSMiddleware,          # adds CORS support
    allow_origins=origins,   # allows requests from origins domains
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # allowed HTTP methods
    allow_headers=["*"],     # allows all headers (for example, Authorization, Content-Type)
)


@app.get("/index", response_class=HTMLResponse)
def index(request:Request):
    return templates.TemplateResponse("index.html", {"request":request})

# @app.post("/translate", response_model=schemas.TaskResponse)
# def translate(request: schemas.TranslationRequest):
#     # task = crud.create_translation_task(get_db.db, request.text, request.languages)