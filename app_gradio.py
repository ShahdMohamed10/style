import gradio as gr
from style_detector import RoomStyleDetector
import tempfile
import os

# Initialize the style detector
detector = RoomStyleDetector()

def detect_style(image):
    """
    Detect the style of a room from an image.
    
    Args:
        image: The input image
        
    Returns:
        tuple: (predicted_style, confidence, style_scores)
    """
    try:
        # Save the image to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
            image.save(temp_file.name)
            
            # Get the style prediction
            predicted_style, confidence = detector.detect_style(temp_file.name)
            
            # Get all style scores
            style_scores = detector.get_all_style_scores(temp_file.name)
            
            # Format the scores for display
            scores_text = "\n".join([f"{style}: {score:.2%}" for style, score in style_scores.items()])
            
            return f"Predicted Style: {predicted_style}\nConfidence: {confidence:.2%}\n\nAll Scores:\n{scores_text}"
            
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        # Clean up the temporary file
        if 'temp_file' in locals() and os.path.exists(temp_file.name):
            try:
                os.unlink(temp_file.name)
            except:
                pass

# Create the Gradio interface
iface = gr.Interface(
    fn=detect_style,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(label="Style Detection Results"),
    title="Room Style Detector",
    description="Upload an image of a room to detect its style. The model can identify Modern, Minimalist, Industrial, Scandinavian, Bohemian, and Traditional styles.",
    examples=[
        ["examples/modern.jpg"],
        ["examples/industrial.jpg"],
        ["examples/bohemian.jpg"]
    ]
)

# Launch the interface
if __name__ == "__main__":
    iface.launch() 