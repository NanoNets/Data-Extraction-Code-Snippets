import tabula
import pandas as pd

def extract_tables_from_pdf(pdf_path):
    """
    Extracts tables from a PDF file using Tabula.

    Args:
        pdf_path (str): The file path of the PDF.

    Returns:
        tables (list of pandas.DataFrame): A list of DataFrames extracted by Tabula.
    """
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

    if tables:
        print(f"Found {len(tables)} tables in the PDF.")
    else:
        print("No tables found in the PDF.")
    
    return tables

def display_tables(tables):
    """
    Displays the extracted tables in the console.

    Args:
        tables (list of pandas.DataFrame): A list of DataFrames extracted by Tabula.
    """
    for i, table in enumerate(tables):
        print(f"\nTable {i + 1}:")
        print(table.to_string(index=False))

def main():
    # Specify the path to your PDF file
    pdf_path = 'sample.pdf'

    # Extract tables from the PDF
    tables = extract_tables_from_pdf(pdf_path)
    
    # Display the extracted tables
    display_tables(tables)

# Execute the main function
if __name__ == '__main__':
    main()
