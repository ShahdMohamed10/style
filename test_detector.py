from style_detector import RoomStyleDetector
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='Detect room style from an image')
    parser.add_argument('image_path', type=str, help='Path to the input image')
    args = parser.parse_args()

    # Convert the path to absolute path and handle spaces
    image_path = os.path.abspath(args.image_path)
    
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at {image_path}")
        return

    try:
        # Initialize the style detector
        detector = RoomStyleDetector()
        
        # Get the predicted style and confidence
        predicted_style, confidence = detector.detect_style(image_path)
        print(f"\nPredicted Style: {predicted_style}")
        print(f"Confidence: {confidence:.2f}%")
        
        # Get all style scores
        print("\nAll style scores:")
        style_scores = detector.get_all_style_scores(image_path)
        for style, score in sorted(style_scores.items(), key=lambda x: x[1], reverse=True):
            print(f"{style}: {score:.2f}%")
    except Exception as e:
        print(f"Error processing image: {str(e)}")

if __name__ == "__main__":
    main() 