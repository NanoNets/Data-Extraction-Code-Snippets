import openai
import pandas as pd
from PIL import Image
import pytesseract
from io import StringIO

# Function to extract text from the image using Tesseract OCR
def extract_text_from_image(image_path):
    img = Image.open(image_path)
    return pytesseract.image_to_string(img)

# Function to process text into CSV format using GPT API
def process_text_with_gpt(extracted_text):
    prompt = f"Here is the raw text from a bank statement:\n\n{extracted_text}\n\nCan you convert this into a CSV format with columns Date, Description, and Amount?"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Function to convert structured CSV data into an Excel file
def convert_to_excel(csv_data, output_file):
    df = pd.read_csv(StringIO(csv_data))
    df.to_excel(output_file, index=False)
    print(f"Excel file saved as {output_file}.")

# Main function that ties everything together
def main(image_path, output_file):
    # Step 1: Extract text from the image
    extracted_text = extract_text_from_image(image_path)
    print("Extracted text:", extracted_text)

    # Step 2: Process extracted text using GPT to convert it into a structured CSV format
    structured_text = process_text_with_gpt(extracted_text)
    print("Structured CSV format:\n", structured_text)

    # Step 3: Convert the structured text into an Excel file
    convert_to_excel(structured_text, output_file)

# Example usage
if __name__ == "__main__":
    image_path = 'path_to_your_bank_statement_image.jpg'
    output_file = 'bank_statement.xlsx'
    main(image_path, output_file)
