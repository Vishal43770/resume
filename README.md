# Resume Ranking Application

## Overview
The Resume Ranking Application is a Streamlit-based tool that ranks resumes according to their relevance to a given job description. By leveraging Python libraries such as PyPDF2, Scikit-learn, and Streamlit, this project simplifies the hiring process by providing a similarity score for each uploaded resume.

## Features
- Extracts text from PDF resumes.
- Accepts multiple resume uploads.
- Calculates relevance scores using **TF-IDF Vectorization** and **Cosine Similarity**.
- Displays rankings in a clear, sortable table format.

## Tech Stack
- Python
- **Libraries Used**:
  - PyPDF2: Extract text from PDFs.
  - Scikit-learn: Perform TF-IDF vectorization and calculate cosine similarity.
  - Pandas: Handle and display tabular data.
  - Streamlit: Build the user interface.

## How It Works
1. **Input Job Description**: Enter the job description in the provided text box.
2. **Upload Resumes**: Add PDF files for the resumes you want to rank.
3. **Process and Rank**: The app extracts text from resumes, calculates similarity scores, and displays rankings in a sortable table.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Vishal43770/resume
   ```
2. Navigate to the project folder:
   ```bash
   cd resume
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```
   Activate it:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the application using Streamlit:
```bash
streamlit run app.py
```
This will start a local development server. Open the provided URL in your browser to use the application.

## Project Structure
```plaintext
resume/
├── app.py              # Main application script.
├── README.md           # Project documentation.
├── requirements.txt    # Dependencies.
├── temp_resumes/       # Temporary folder for uploaded resume processing (created during execution).
```

## Future Enhancements
- Expand support for other document formats (e.g., DOCX).
- Add more ranking criteria based on industry-specific keywords.
- Improve text extraction for PDFs with complex layouts.
- Enhance UI/UX for better user interaction.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Contributing
Contributions are welcome! Submit a pull request or open an issue on GitHub if you'd like to improve this application.
