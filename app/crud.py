from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models

def create_translation_task(db: Session, text:str, languages: list):
    task = models.TranslationTask(text=text, languages=languages)

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def get_translation_task(db: Session, task_id: int):
    task = db.query(models.TranslationTask).filter(models.TranslationTask.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Translation task not found")

    return task

def update_translation_task(db: Session, task_id: int, translations: dict):
    task = db.query(models.TranslationTask).filter(models.TranslationTask.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Translation task not found")

    task.translations = translations
    task.status = "completed"

    db.commit()
    db.refresh(task)

    return task
