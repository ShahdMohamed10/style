# Room Style Detector

This project uses the CLIP (Contrastive Language-Image Pre-training) model to detect room styles from images. It can classify rooms into 6 different styles:
- Modern
- Minimalist
- Industrial
- Scandinavian
- Bohemian
- Traditional

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. The CLIP model will be automatically downloaded when you first run the code.

## Usage

### Testing the Style Detector

You can test the style detector using the test script:

```bash
python test_detector.py path/to/your/image.jpg
```

This will output:
- The predicted style
- The confidence score
- Scores for all possible styles

### Using in Your Code

```python
from style_detector import RoomStyleDetector

# Initialize the detector
detector = RoomStyleDetector()

# Detect style from an image
style, confidence = detector.detect_style("path/to/image.jpg")
print(f"Predicted style: {style}")
print(f"Confidence: {confidence:.2f}%")

# Get scores for all styles
style_scores = detector.get_all_style_scores("path/to/image.jpg")
```

## API Integration

This code is structured to be easily integrated into a web API. The `RoomStyleDetector` class can be used as a service in your API implementation.

## Requirements

- Python 3.7+
- PyTorch
- CLIP
- Pillow
- Other dependencies listed in requirements.txt 