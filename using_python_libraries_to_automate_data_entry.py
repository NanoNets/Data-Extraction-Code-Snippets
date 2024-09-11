import cv2
import numpy as np
from PIL import Image
import pytesseract

# Preprocess the image to enhance OCR accuracy
def preprocess_image(image_path):
    # Load the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply thresholding to binarize the image (black & white)
    _, img_bin = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
    
    # Apply median blur to reduce noise
    img_cleaned = cv2.medianBlur(img_bin, 3)
    
    return img_cleaned

# Extract text using Tesseract OCR
def extract_text_from_image(image_path):
    # Preprocess the image for better OCR results
    img = preprocess_image(image_path)
    
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(img, config='--psm 6')  # PSM 6: assumes a block of text
    return text

# Main function to execute the entire process
def main(image_path):
    # Extract text from the given image
    extracted_text = extract_text_from_image(image_path)
    
    # Output the extracted text
    print("Extracted Text:")
    print(extracted_text)

if __name__ == "__main__":
    # Replace 'handwritten_sample.jpg' with the path to your image
    main('handwritten_sample.jpg')
