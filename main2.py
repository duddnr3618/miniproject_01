from typing import Union
from fastapi import FastAPI, File, UploadFile, Depends, HTTPException, WebSocket, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
import models
from datetime import datetime
import cv2
import numpy as np
from insightface.app import FaceAnalysis
from PIL import Image
import io 
import os
import base64
from base64 import b64encode

app = FastAPI()

# HTML 파일(템플릿) 위치
templates = Jinja2Templates(directory="templates")

# 데이터베이스 모델 생성
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 회원가입
@app.get("/signup2")
async def signup(request: Request):
    return templates.TemplateResponse("signup2.html", {"request": request})
