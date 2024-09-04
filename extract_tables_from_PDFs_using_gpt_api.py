import openai
import PyPDF2

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file using PyPDF2.
    
    Args:
        pdf_path (str): The path to the PDF file.
    
    Returns:
        str: The extracted text content.
    """
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_tables_from_text(text):
    """
    Extracts tables from the provided text using GPT-4.
    
    Args:
        text (str): The extracted text content.
    
    Returns:
        str: The extracted tables in text format.
    """
    prompt = (
        "Please extract all tables from the following text. "
        "Format them as CSV-like structures with columns and rows clearly defined:\n\n"
        f"{text}"
    )
    
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=2000,
        temperature=0.5
    )
    
    return response.choices[0].text.strip()

def display_extracted_tables(extracted_tables):
    """
    Displays the extracted tables.
    
    Args:
        extracted_tables (str): The extracted tables in text format.
    """
    print("Extracted Tables:")
    print(extracted_tables)

def main():
    # Path to your PDF file
    pdf_path = "your_pdf_file.pdf"
    
    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_path)
    
    # Extract tables from the text using GPT-4
    extracted_tables = extract_tables_from_text(pdf_text)
    
    # Display the extracted tables
    display_extracted_tables(extracted_tables)

if __name__ == "__main__":
    main()
