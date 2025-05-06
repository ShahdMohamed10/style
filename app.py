from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from style_detector import RoomStyleDetector
import uvicorn
import tempfile
import os
from typing import Dict

app = FastAPI(title="Room Style Detector API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize the style detector
detector = RoomStyleDetector()

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("templates/index.html", "r") as f:
        return f.read()

@app.post("/detect-style")
async def detect_style(file: UploadFile = File(...)) -> Dict:
    """
    Detect the style of a room from an uploaded image.
    
    Args:
        file: The image file to analyze
        
    Returns:
        Dict containing the predicted style and confidence scores
    """
    temp_file = None
    try:
        # Create a temporary file to store the uploaded image
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1])
        
        # Write the uploaded file to the temporary file
        content = await file.read()
        temp_file.write(content)
        temp_file.close()  # Close the file before processing
        
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080) 