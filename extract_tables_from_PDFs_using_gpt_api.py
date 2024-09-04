import openai
import pandas as pd
import tabula

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"
def extract_tables_from_pdf(pdf_path):
    """
    Extracts tables from a PDF file using Tabula.

    Args:
        pdf_path (str): The file path of the PDF.

    Returns:
        tables (list of pandas.DataFrame): A list of DataFrames extracted by Tabula.
    """
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    return tables
def create_prompt_from_tables(tables):
    """
    Create a detailed prompt for GPT-4 to extract structured data from tables.

    Args:
        tables (list of pandas.DataFrame): A list of DataFrames representing the tables.

    Returns:
        str: A formatted prompt for GPT-4.
    """
    prompt = "Extract the following information from the PDF tables:\n"
    for index, table in enumerate(tables):
        prompt += f"Table {index + 1}:\n{table.to_string(index=False)}\n\n"
    return prompt
def extract_data_using_gpt(prompt):
    """
    Sends the prompt to GPT-4 and extracts the response.

    Args:
        prompt (str): The formatted prompt for GPT-4.

    Returns:
        str: The text response from GPT-4.
    """
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response['choices'][0]['text']
def parse_extracted_data(text):
    """
    Parses GPT-4's response to extract structured table data.

    Args:
        text (str): The text response from GPT-4.

    Returns:
        dict: Parsed data with table content.
    """
    # Implement a parsing logic based on the response structure.
    # This example assumes GPT-4 returns a structured JSON-like response.
    parsed_data = {}
    # Example parsing (adjust based on actual output format)
    return parsed_data
def save_data_to_excel(parsed_data, excel_path):
    """
    Saves parsed data to an Excel file.

    Args:
        parsed_data (dict): The parsed table data.
        excel_path (str): The output file path for the Excel file.
    """
    df = pd.DataFrame(parsed_data)
    df.to_excel(excel_path, index=False)
    print(f"Data successfully saved to {excel_path}.")
def main(pdf_path, excel_path):
    # Step 1: Extract tables from PDF
    tables = extract_tables_from_pdf(pdf_path)
    
    # Step 2: Create a detailed prompt
    prompt = create_prompt_from_tables(tables)
    
    # Step 3: Extract data using GPT API
    extracted_text = extract_data_using_gpt(prompt)
    
    # Step 4: Parse extracted data
    parsed_data = parse_extracted_data(extracted_text)
    
    # Step 5: Save parsed data to Excel
    save_data_to_excel(parsed_data, excel_path)

# Example usage
pdf_path = 'tables.pdf'  # Path to your PDF file
excel_path = 'output.xlsx'  # Path where you want to save the Excel file

main(pdf_path, excel_path)
