import camelot
import pandas as pd

def extract_tables_from_pdf(pdf_path):
    """
    Extracts tables from a PDF file using Camelot.

    Args:
        pdf_path (str): The file path of the PDF.

    Returns:
        tables (camelot.core.TableList): A list of tables extracted by Camelot.
    """
    tables = camelot.read_pdf(pdf_path, pages='all', flavor='lattice')

    if tables:
        print(f"Found {tables.n} tables in the PDF.")
    else:
        print("No tables found in the PDF.")
    
    return tables

def convert_tables_to_excel(tables, output_path):
    """
    Converts extracted tables into an Excel file.

    Args:
        tables (camelot.core.TableList): A list of tables extracted by Camelot.
        output_path (str): The file path for the output Excel file.
    """
    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')

    for i, table in enumerate(tables):
        table.df.to_excel(writer, sheet_name=f'Table_{i+1}', index=False)

    writer.save()
    print(f"Tables have been successfully written to {output_path}.")

def main():
    # Specify the path to your PDF file
    pdf_path = 'sample.pdf'
    
    # Specify the path where the Excel file will be saved
    output_path = 'output.xlsx'

    # Extract tables from the PDF
    tables = extract_tables_from_pdf(pdf_path)
    
    # Convert tables to Excel
    convert_tables_to_excel(tables, output_path)

# Execute the main function
if __name__ == '__main__':
    main()
