import base64
import io
import os
from PIL import Image
from textextract import TextExtractor, OS

def decode_base64_to_image(base64_string: str, output_path: str) -> None:
    """Decode a base64 string and save it as an image file."""
    try:
        # Decode the base64 string
        image_data = base64.b64decode(base64_string)
        # Convert binary data to an image
        image = Image.open(io.BytesIO(image_data))
        # Save the image to a file
        image.save(output_path)
    except Exception as e:
        print(f"Error decoding or saving image: {e}")

def main(base64_string: str) -> str:
    # Path where the decoded image will be saved
    image_path = 's1.png'
    
    # Decode the base64 string and save the image
    decode_base64_to_image(base64_string, image_path)
    
  
    # Create an instance of TextExtractor
    extractor = TextExtractor(os_type=OS.Window)
   
    # Extract text from the image
    extracted_text = extractor.extract_text(image_path)
   
    
    # Optionally, clean up the image file after processing
    if os.path.exists(image_path):
        os.remove(image_path)
    
    return extracted_text

