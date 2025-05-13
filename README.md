# Room Style Detector

This application uses the CLIP model to detect the style of rooms from images. It can classify rooms into different styles such as Modern, Minimalist, Industrial, Scandinavian, Bohemian, and Traditional.

## Features

- Upload room images to detect their style
- Get confidence scores for all possible styles
- Simple and intuitive interface
- Real-time predictions

## Deployment on Hugging Face Spaces

1. Go to [Hugging Face Spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Choose "Gradio" as the SDK
4. Name your space (e.g., "room-style-detector")
5. Choose "Public" or "Private" visibility
6. Click "Create Space"
7. Push your code to the space:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
   git push -u origin main
   ```

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app_gradio.py
   ```

## API Usage

The application provides a simple interface where you can:
1. Upload an image of a room
2. Get the predicted style and confidence scores
3. View scores for all possible styles

## Requirements

- Python 3.9+
- PyTorch
- CLIP
- Gradio
- Other dependencies listed in requirements.txt 