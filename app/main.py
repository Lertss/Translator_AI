import logging
from fastapi import FastAPI, BackgroundTasks, HTTPException, Depends, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from schemas import TranslationRequestSchema
from typing import List
from utils import translate_text, process_translations


from database import engine, SessionLocal, get_db
import models
from models import TranslationRequest, TranslationResult, IndividualTranslations

models.Base.metadata.create_all(engine)



app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

templates = Jinja2Templates(directory="templates")


@app.get("/index", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.post("/translate")
async def translate(request: TranslationRequestSchema, background_tasks: BackgroundTasks,
                    db: Session = Depends(get_db)):
    print(request.text)
    print(request.languages)

    # requests above is a pydantic model, my_dict below is a dict, incase you need to use one or another
    my_dict = request.model_dump()
    #     print(my_dict)


    request_data = models.TranslationRequest(
        text=request.text,
        languages=request.languages)
    db.add(request_data)
    db.commit()
    db.refresh(request_data)

    # background_tasks.add_task(process_translations, request_data.id, request.text, request.languages)
    return {"payload": request_data}



@app.get("/translate/{request_id}")
async def get_translation_status(request_id: int, request: Request, db: Session = Depends(get_db)):
    request_obj = db.query(TranslationRequest).filter(TranslationRequest.id == request_id).first()
    if not request_obj:
        raise HTTPException(status_code=404, detail="Request not found")
    if request_obj.status == "in progress":
        return {"status": request_obj.status}
    translations = db.query(TranslationResult).filter(TranslationResult.request_id == request_id).all()
    return templates.TemplateResponse("results.html", {"request": request, "translations": translations})
