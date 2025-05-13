from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from style_detector import RoomStyleDetector
import tempfile
import os
from typing import Dict

app = FastAPI(title="Room Style Detector API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the style detector
detector = RoomStyleDetector()

@app.get("/")
async def root():
    return {"message": "Room Style Detector API is running"}

@app.post("/api/detect-style")
async def detect_style(file: UploadFile = File(...)) -> Dict:
    """
    Detect the style of a room from an uploaded image.
    """
    temp_file = None
    try:
        # Create a temporary file to store the uploaded image
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1])
        
        # Write the uploaded file to the temporary file
        content = await file.read()
        temp_file.write(content)
        temp_file.close()
        
        # Get the style prediction
        predicted_style, confidence = detector.detect_style(temp_file.name)
        
        # Get all style scores
        style_scores = detector.get_all_style_scores(temp_file.name)
        
        return {
            "predicted_style": predicted_style,
            "confidence": confidence,
            "all_scores": style_scores
        }
            
    except Exception as e:
        return {"error": str(e)}
    finally:
        # Clean up the temporary file
        if temp_file and os.path.exists(temp_file.name):
            try:
                os.unlink(temp_file.name)
            except Exception as e:
                print(f"Warning: Could not delete temporary file: {str(e)}") 