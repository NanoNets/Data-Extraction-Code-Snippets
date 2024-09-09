import cv2
import pytesseract
from PIL import Image
import numpy as np
# Step 1: Pre-process the image
def preprocess_image(image_path):
    """
    Pre-processes the input image by converting to grayscale,
    thresholding, and removing noise to enhance OCR accuracy.
    
    Parameters:
        image_path (str): Path to the image file.
    Returns:
        numpy.ndarray: Pre-processed image.
    """
    # Load image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply thresholding (binarize the image)
    _, img_bin = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
    
    # Optionally, apply noise removal
    img_noise_removal = cv2.medianBlur(img_bin, 3)
    
    # Save the processed image for inspection
    cv2.imwrite("preprocessed_image.jpg", img_noise_removal)
    
    return img_noise_removal
# Step 2: Extract text from the pre-processed image
def extract_text_from_image(preprocessed_img):
    """
    Extracts text from the pre-processed image using Tesseract OCR.
    
    Parameters:
        preprocessed_img (numpy.ndarray): Pre-processed image data.
    Returns:
        str: Extracted text.
    """
    # Use Tesseract to extract text
    text = pytesseract.image_to_string(preprocessed_img, config='--psm 6')
    return text
# Main function
def main(image_path):
    """
    Main function to run the entire process of image preprocessing
    and text extraction.
    
    Parameters:
        image_path (str): Path to the handwritten image file.
    """
    # Step 1: Pre-process the image
    preprocessed_img = preprocess_image(image_path)
    
    # Step 2: Extract text from the pre-processed image
    extracted_text = extract_text_from_image(preprocessed_img)
    
    # Output the extracted text
    print("Extracted Text:\n", extracted_text)
# Run the script
if __name__ == "__main__":
    image_path = 'handwritten_sample.jpg'  # Replace with your image file path
    main(image_path)