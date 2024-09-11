import openai
import PyPDF2
import pandas as pd

# Set your GPT API key
openai.api_key = 'your-api-key'

# Step 1: Extract text from the PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.getNumPages()):
            page = reader.getPage(page_num)
            text += page.extract_text()
    return text

# Step 2: Extract structured data using GPT API
def extract_data_with_gpt(pdf_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Extract the following information from this invoice:\n\n{pdf_text}\n\nExtract the following fields:\n- Customer Name\n- Invoice Number\n- Date\n- Line Items (Description, Quantity, Unit Price, Total)\n- Total Amount",
        max_tokens=300
    )
    return response.choices[0].text.strip()

# Step 3: Parse the GPT output into structured data
def parse_gpt_output(gpt_output):
    data = {}
    
    lines = gpt_output.split("\n")
    for line in lines:
        if "Customer Name" in line:
            data['Customer Name'] = line.split(":")[1].strip()
        if "Invoice Number" in line:
            data['Invoice Number'] = line.split(":")[1].strip()
        if "Total Amount" in line:
            data['Total Amount'] = line.split(":")[1].strip()
    
    # You can parse line items similarly
    return data

# Step 4: Export structured data to Excel
def export_to_excel(data, output_path):
    df = pd.DataFrame([data])
    df.to_excel(output_path, index=False)

# Main function
def main(pdf_path, output_path):
    # Extract text from PDF
    pdf_text = extract_text_from_pdf(pdf_path)
    
    # Extract structured data using GPT
    extracted_data = extract_data_with_gpt(pdf_text)
    
    # Parse the GPT output
    parsed_data = parse_gpt_output(extracted_data)
    
    # Export the parsed data to Excel
    export_to_excel(parsed_data, output_path)

if __name__ == "__main__":
    main('invoice.pdf', 'invoice_output.xlsx')
