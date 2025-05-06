import torch
import clip
from PIL import Image
import numpy as np

class RoomStyleDetector:
    def __init__(self):
        # Load the CLIP model
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.preprocess = clip.load("ViT-B/32", device=self.device)
        
        # Define the room styles we want to detect
        self.styles = [
            "Modern",
            "Minimalist",
            "Industrial",
            "Scandinavian",
            "Bohemian",
            "Traditional"
        ]
        
        # Prepare the text prompts
        self.text_inputs = torch.cat([clip.tokenize(f"a photo of a {style} style room") for style in self.styles]).to(self.device)
        
        # Encode the text prompts
        with torch.no_grad():
            self.text_features = self.model.encode_text(self.text_inputs)
            self.text_features /= self.text_features.norm(dim=-1, keepdim=True)

    def detect_style(self, image_path):
        """
        Detect the style of a room from an image.
        
        Args:
            image_path (str): Path to the input image
            
        Returns:
            tuple: (predicted_style, confidence_score)
        """
        # Load and preprocess the image
        image = Image.open(image_path)
        image_input = self.preprocess(image).unsqueeze(0).to(self.device)
        
        # Get image features
        with torch.no_grad():
            image_features = self.model.encode_image(image_input)
            image_features /= image_features.norm(dim=-1, keepdim=True)
        
        # Calculate similarity scores
        similarity = (100.0 * image_features @ self.text_features.T).softmax(dim=-1)
        values, indices = similarity[0].topk(1)
        
        # Get the predicted style and confidence
        predicted_style = self.styles[indices[0].item()]
        confidence = values[0].item()
        
        return predicted_style, confidence

    def get_all_style_scores(self, image_path):
        """
        Get similarity scores for all styles.
        
        Args:
            image_path (str): Path to the input image
            
        Returns:
            dict: Dictionary containing style names and their confidence scores
        """
        # Load and preprocess the image
        image = Image.open(image_path)
        image_input = self.preprocess(image).unsqueeze(0).to(self.device)
        
        # Get image features
        with torch.no_grad():
            image_features = self.model.encode_image(image_input)
            image_features /= image_features.norm(dim=-1, keepdim=True)
        
        # Calculate similarity scores
        similarity = (100.0 * image_features @ self.text_features.T).softmax(dim=-1)
        
        # Create a dictionary of styles and their scores
        style_scores = {
            style: score.item() 
            for style, score in zip(self.styles, similarity[0])
        }
        
        return style_scores 