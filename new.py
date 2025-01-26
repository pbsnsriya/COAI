import pandas as pd
from PIL import Image
import pytesseract as tess
import subprocess

# Path to Tesseract OCR
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Function to extract text from image (OCR)
def extract_text_from_image(image_path):
    img_obj = Image.open(image_path)
    text = tess.image_to_string(img_obj)
    return text

# Function to read CO data from Excel file
def extract_co_data(excel_file):
    df = pd.read_excel(excel_file, engine='openpyxl')
    return df.to_string(index=False)

# Function to call Llama-2 locally using subprocess
def get_local_ai_response(prompt):
    try:
        # Call Llama-2 using subprocess and Ollama (replace 'llama2' with correct command)
        result = subprocess.run(
            ['ollama', 'run', 'llama2', prompt],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            return result.stdout  # Return the output from Llama-2
        else:
            return f"Error: {result.stderr}"
    except Exception as e:
        return f"Error generating AI response: {e}"

# Main processing function
def process():
    # Extract text from the image
    image = "test_paper_1.png"
    text = extract_text_from_image(image)
    with open("question_paper.txt", "w+") as file:
        file.write(text)

    # Extract CO data from the Excel file
    excel_file = r"C:\Users\pbsns\OneDrive\Documents\hack123\co.xlsx"
    co_data = extract_co_data(excel_file)
    with open("cod.txt", "w+") as file:
        file.write(co_data)

    # Combine the extracted text and CO data for AI processing
    prompt = f"Analyze the following question paper and course outcome data to identify the learning gaps and provide a detailed response:\n\n{text}\n\nCO Data:\n{co_data}"

    # Get AI response from local Llama-2 model
    ai_response = get_local_ai_response(prompt)
    # with open("ai_response.txt", "w+") as file:
    #     file.write(ai_response)
    print(ai_response)
    print("Processing complete! Results saved in 'question_paper.txt', 'cod.txt', and 'ai_response.txt'.")

# Run the process
if __name__ == "__main__":
    process()
