import json
import os

import google.generativeai as genai
from fastapi import FastAPI
#from app.api.endpoints import project, datafono
from app.config import settings

# 🔥🔥 FILL THIS OUT FIRST! 🔥🔥
# Get your Gemini API key by:
# - Selecting "Add Gemini API" in the "Project IDX" panel in the sidebar
# - Or by visiting https://g.co/ai/idxGetGeminiKey
#genai.configure(api_key=settings.GENAI_API_KEY)

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# Incluir los routers de los endpoints
#app.include_router(project.router, prefix="/projects", tags=["projects"])
#app.include_router(datafono.router, prefix="/datafonos", tags=["datafonos"])

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de integración de datafonos"}