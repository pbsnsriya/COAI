# COAI: Course Outcome AI

Welcome to COAI! This guide will walk you through setting up and using our powerful AI-driven Course Outcome analysis tool. Follow these steps to get started.

## Youtube Link
you can view the model working here in the video, A demo instance.
https://youtu.be/8D9Q4fgBRAw?si=v3pnAS2FIFR6tKJR

## Website link
Responsive website representing our Ideology.
https://pbsnsriya.github.io/COAI/

---

## Installation & Setup

### Step 1: Install Dependencies

Make sure you have Python 3 installed on your system. Then, use the following command to install the required Python libraries:

```bash
pip install -r requirements.txt
```

### Step 2: Download Tesseract OCR Framework

Download and install the Tesseract OCR framework. Ensure it is installed in the Program Files directory on your C drive.

- [Tesseract OCR Releases](https://github.com/tesseract-ocr/tesseract/releases)

### Step 3: Install Ollama

Download and install Ollama.exe for Windows from the official website:

- [Ollama Official Website](https://ollama.com/)

If you want to run Llama 3.3 (requires significant storage), you can download it. By default, we use Llama 2 with 7B parameters.

### Step 4: Set Up and Run Llama

After installing Ollama:

1. Open the Run dialog (Win + R), type `cmd`, and press Enter.
2. Run the following command for Llama 2:
   ```bash
   ollama run llama2
   ```
   If using Llama 3.3, run:
   ```bash
   ollama run llama3.3
   ```

### Step 5: Verify Setup

After installation, you will be prompted to provide input prompts. If you reach this stage, your setup is 95% complete!

---

## Using COAI

### Step 6: Prepare Python and Files

Ensure you have Python 3 installed. If not, download it from:

- [Python Official Website](https://python.org/)

### Step 7: Set File Paths

Update the code to include the file paths for:

- The test paper image
- The CO data files

### Step 8: Run the Code

Run the Python script, and COAI will process the input and provide detailed responses and insights.

---

## Support

If you face any issues during installation or usage, feel free to reach out to our support team.

---



