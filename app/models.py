from dotenv import load_dotenv
import os
from anyio.streams.file import FileStreamAttribute
from sqlalchemy import Column, Integer, String, Text, JSON

from sqlalchemy.ext.declarative import declarative_base

load_dotenv()
Base = declarative_base()

class TranslationTask(Base):
    __tablename__ = "translation_tasks"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    languages = Column(JSON, nullable=False)
    status = Column(String, default="in progress")
    translation = Column(JSON, default={})

