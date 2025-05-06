import requests
import json

def test_api():
    url = "http://localhost:8080/detect-style"
    image_path = "industiral-20250506T110426Z-001/industiral/2cb8a90369a2b44963fe3075d5f1d3d6.jpg"
    
    try:
        with open(image_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(url, files=files)
            
        print("Status Code:", response.status_code)
        print("Response:")
        print(json.dumps(response.json(), indent=2))
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_api() 