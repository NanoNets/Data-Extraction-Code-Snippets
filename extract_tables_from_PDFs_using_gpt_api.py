import openai

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

def extract_tables_from_text(pdf_text):
    """
    Extracts tables from the provided PDF text using GPT-4.
    
    Args:
        pdf_text (str): The text content of the PDF.
    
    Returns:
        str: The extracted tables in text format.
    """
    # Create a detailed prompt
    prompt = (
        "Please extract all tables from the following text. "
        "Ensure that the tables are clearly formatted and separated.\n\n"
        f"{pdf_text}"
    )
    
    # Use the GPT-4 API to process the prompt
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=2000,  # Adjust based on table size
        temperature=0.5
    )
    
    return response.choices[0].text.strip()

def save_tables_to_file(extracted_tables, file_path):
    """
    Saves the extracted tables to a file.
    
    Args:
        extracted_tables (str): The extracted tables in text format.
        file_path (str): The path to save the tables.
    """
    with open(file_path, 'w') as file:
        file.write(extracted_tables)
    print(f"Tables successfully saved to {file_path}.")

def main():
    # Sample PDF text content
    pdf_text = """
    (Paste your extracted PDF text content here)
    """

    # Extract tables from the PDF text using GPT-4
    extracted_tables = extract_tables_from_text(pdf_text)
    
    # Save the extracted tables to a file
    output_file_path = "extracted_tables.txt"
    save_tables_to_file(extracted_tables, output_file_path)

if __name__ == "__main__":
    main()

