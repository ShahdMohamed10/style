import requests
import json
import os
from pathlib import Path

def test_api(image_path=None):
    url = "http://localhost:8080/detect-style"
    
    # If no image path is provided, use a default test image
    if image_path is None:
        # Try to find an image in the style directories
        style_dirs = [
            "modern-20250506T110430Z-001/modern",
            "classic-20250506T110415Z-001/classic",
            "boho-20250506T110413Z-001/boho",
            "industiral-20250506T110426Z-001/industiral"
        ]
        
        for dir_path in style_dirs:
            if os.path.exists(dir_path):
                # Get the first image file in the directory
                image_files = [f for f in os.listdir(dir_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
                if image_files:
                    image_path = os.path.join(dir_path, image_files[0])
                    break
    
    if not image_path or not os.path.exists(image_path):
        print("Error: No valid image found for testing")
        return
    
    try:
        print(f"\nTesting with image: {image_path}")
        with open(image_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(url, files=files)
            
        print("Status Code:", response.status_code)
        if response.status_code == 200:
            print("Response:")
            print(json.dumps(response.json(), indent=2))
        else:
            print("Error Response:", response.text)
        
    except Exception as e:
        print(f"Error: {str(e)}")

def test_multiple_images():
    """Test the API with multiple images from different style directories"""
    style_dirs = [
        "modern-20250506T110430Z-001/modern",
        "classic-20250506T110415Z-001/classic",
        "boho-20250506T110413Z-001/boho",
        "industiral-20250506T110426Z-001/industiral"
    ]
    
    for dir_path in style_dirs:
        if os.path.exists(dir_path):
            print(f"\nTesting images from {dir_path}:")
            image_files = [f for f in os.listdir(dir_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            for image_file in image_files[:2]:  # Test first 2 images from each directory
                image_path = os.path.join(dir_path, image_file)
                test_api(image_path)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Test with specific image
        test_api(sys.argv[1])
    else:
        # Test with multiple images
        test_multiple_images() 