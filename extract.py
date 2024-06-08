import PyPDF2
import re
import pandas as pd

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text() + "\n"
    return text

def categorize_text(text):
    categories = ["Introduction", "Methodology", "Results", "Conclusion"]
    
    # Dictionary to hold categorized text
    categorized_data = {category: "" for category in categories}
    
    current_category = None
    for line in text.splitlines():
        line = line.strip()
        
        # Check if the line indicates a new category
        for i, category in enumerate(categories):
        
            if re.search(rf'\b{category}\b', line, re.IGNORECASE):
                current_category = category
                break
      
        # If the line does not indicate a new category, append it to the current category
        if current_category and line != current_category:
            categorized_data[current_category] += " " + line
        
    
    # Convert the dictionary to a list of tuples
    categorized_list = [(category, categorized_data[category].strip()) for category in categories if categorized_data[category].strip()]
    
    return categorized_list

def save_to_csv(categorized_data, output_csv):
    df = pd.DataFrame(categorized_data, columns=["Category", "Text"])
    df.to_csv(output_csv, index=False)

def main():
    pdf_path = r'C:\Users\USER\Desktop\Desktop\Projects\pdf extractor\Introduction.pdf'
    output_csv = 'categorized_text.csv'
    
    # Step 1: Extract text from PDF
    text = extract_text_from_pdf(pdf_path)
    
    # Step 2: Categorize the extracted text
    categorized_data = categorize_text(text)
    
    # Step 3: Save the categorized text to CSV
    save_to_csv(categorized_data, output_csv)
    
    print(f"Categorized text saved to {output_csv}")

if __name__ == "__main__":
    main()
