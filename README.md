# NLP Curriculum Mini-Project: Text Analysis REST API

## Overview

This repository contains the practical implementations completed as part of the **Natural Language Processing (NLP) curriculum**.

The final mini-project is a fully functional **REST API built using FastAPI**, integrating traditional NLP techniques with modern Transformer-based models.

The application combines:

- **spaCy:** For traditional NLP tasks such as tokenization, sentence segmentation, Part-of-Speech (POS) tagging, dependency parsing, and Named Entity Recognition (NER).
- **Hugging Face Transformers:** For Transformer-based sentiment analysis using a pretrained DistilBERT model.
- **FastAPI:** For developing and exposing NLP functionalities through REST API endpoints.

The objective is to demonstrate how different NLP techniques and pretrained models can be integrated into a scalable API application.

## 🚀 Features

The API provides the following NLP capabilities:

### 1. Sentiment Analysis
- Analyzes the emotional tone of input text.
- Classifies text as **POSITIVE** or **NEGATIVE**.
- Uses a pretrained DistilBERT model from Hugging Face.
- Returns the predicted sentiment and confidence score.

### 2. Named Entity Recognition (NER)
- Identifies and extracts named entities from text using spaCy.
- Supports entity categories such as:
  - Person names
  - Organizations
  - Locations
  - Dates and times
  - Monetary values
  - Other recognized entities

### 3. Advanced Text Analysis
- Combines sentiment analysis and Named Entity Recognition.
- Processes text through both NLP models in a single API request.
- Returns a consolidated response containing sentiment and extracted entities.

## 📚 Curriculum Topics Covered

This project demonstrates the practical implementation of the following NLP concepts:

| No. | Topic | Description |
|---|---|---|
| 1 | spaCy Installation & Configuration | Installing spaCy and configuring language pipelines. |
| 2 | Tokenization | Splitting text into tokens and implementing custom tokenizer rules. |
| 3 | Sentence Segmentation | Identifying and separating individual sentences. |
| 4 | Named Entity Recognition (NER) | Extracting names, organizations, locations, and dates. |
| 5 | POS Tagging | Identifying grammatical categories such as nouns, verbs, and adjectives. |
| 6 | Dependency Parsing | Understanding grammatical relationships between words. |
| 7 | Hugging Face Hub | Downloading and loading pretrained Transformer models. |
| 8 | Transformers Pipeline | Implementing sentiment analysis using pretrained DistilBERT. |
| 9 | FastAPI Development | Building REST API endpoints for NLP operations. |
| 10 | API Testing & Integration | Testing endpoints using Swagger UI, cURL, and Python Requests. |

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.8+ | Core programming language |
| spaCy | Traditional NLP processing |
| Hugging Face Transformers | Pretrained Transformer models |
| DistilBERT | Sentiment classification |
| PyTorch | Deep learning framework |
| FastAPI | REST API development |
| Uvicorn | ASGI server |
| Pydantic | Request and response validation |

## ⚙️ Installation & Setup

Follow the steps below to configure and run the project locally.

### Prerequisites

Ensure the following are installed:

- Python 3.8 or later (use a Python version supported by your selected dependencies).
- pip (Python package manager).
- Git.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git

cd your-repo-name
```

### 2. Create a Virtual Environment

Creating a virtual environment helps isolate project dependencies.

**Windows:**

```bash
python -m venv venv

venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

If the `requirements.txt` file is not available, install the dependencies manually:

```bash
pip install fastapi uvicorn transformers torch spacy pydantic
```

### 4. Download the spaCy Language Model

Download the English language model:

```bash
python -m spacy download en_core_web_sm
```

This model provides the necessary pipeline components for tokenization, POS tagging, dependency parsing, and Named Entity Recognition.

## 🏃 Running the API

Start the FastAPI development server using Uvicorn:

```bash
uvicorn main:app --reload
```

**Command explanation:**

- `main`: Python file name (`main.py`).
- `app`: FastAPI application instance defined inside `main.py`.
- `--reload`: Automatically restarts the server whenever code changes are detected.

Once the server starts successfully, the application will be available at:

**Base URL:** http://127.0.0.1:8000

## 🧪 API Testing

FastAPI automatically generates interactive API documentation, making it easy to test the available endpoints.

### Option 1: Swagger UI (Recommended)

Open the following URL in your browser:

http://127.0.0.1:8000/docs

Steps:

1. Select the required API endpoint.
2. Click **Try it out**.
3. Enter the JSON request body.
4. Click **Execute**.
5. Review the API response.

### Option 2: Using cURL

You can test the advanced text analysis endpoint directly from your terminal:

```bash
curl -X POST "http://127.0.0.1:8000/analyze-full" \
-H "Content-Type: application/json" \
-d '{
    "text": "Apple Inc. was founded by Steve Jobs in April 1976. I absolutely love their products!"
}'
```

### Option 3: Using Python Requests

Create a file named `client.py`:

```python
import requests

url = "http://127.0.0.1:8000/analyze-full"

payload = {
    "text": "The brilliant scientist discovered a new element in London yesterday. It was a great day!"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("API Response:", response.json())
```

Install the Requests library if required:

```bash
pip install requests
```

Execute the script:

```bash
python client.py
```

## 📁 Project Structure

The current project follows a simple structure:

```text
your-repo-name/
│
├── mini-project
    ├── main.py      # FastAPI application and NLP model logic
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── venv/                # Python virtual environment (local only)
```

**Note:** The `venv/` directory should not be committed to Git. Add it to `.gitignore`.

## 📦 Generate requirements.txt

Before pushing the project to GitHub, generate the dependency file:

```bash
pip freeze > requirements.txt
```

This records the installed package versions so the project environment can be recreated more consistently.

## 🔮 Future Enhancements

Potential improvements for the project include:

- Text summarization using pretrained Transformer models.
- Keyword and keyphrase extraction.
- Language detection.
- Text classification for custom categories.
- Custom Named Entity Recognition models.
- Batch text processing.
- API authentication and request validation.
- Docker-based deployment.
- Model optimization and inference performance improvements.

## 📝 License

This project is intended for educational and learning purposes as part of the NLP curriculum.

It is available under the [MIT License](https://choosealicense.com/licenses/mit/).

## 🔗 GitHub Setup & Deployment

After completing the project, follow these commands to initialize the Git repository and push the code to GitHub.

### 1. Initialize Git

```bash
git init
```

### 2. Add Project Files

```bash
git add .
```

### 3. Commit Changes

```bash
git commit -m "Complete NLP mini-project: FastAPI Text Analysis REST API"
```

### 4. Set the Main Branch

```bash
git branch -M main
```

### 5. Connect the GitHub Repository

```bash
git remote add origin https://github.com/your-username/your-repo-name.git
```

### 6. Push Code to GitHub

```bash
git push -u origin main
```

---

**Project Status:** Completed – NLP Text Analysis REST API

**Key Learning Outcome:** Practical implementation of traditional NLP techniques, Transformer-based sentiment analysis, and REST API development using Python, spaCy, Hugging Face, and FastAPI.
