# Financial Advisor AI

A Flask-based web application that combines PDF text extraction with AI-powered financial advice using Google's Gemini model and multilingual translation capabilities for personalized financial guidance.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/flask-v3.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 🌟 Features

- **User Authentication**: Secure signup and login system
- **PDF Analysis**: Upload and extract text from loan agreement documents
- **AI-Powered Advisor**: Get personalized financial advice using Google's Gemini AI
- **Multi-language Support**: Ask questions in multiple languages (English, Hindi, French, Spanish)
- **Responsive Design**: Works seamlessly across devices

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vishal-kadalagi/Financial-Advisor-AI.git
   cd nlp_final
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python setup_db.py
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open your browser and navigate to `http://localhost:5000`

### Running the Project in Terminal

To run the project in your terminal, follow these steps:

1. Activate your virtual environment (if not already activated):
   ```bash
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. You should see output similar to:
   ```
   * Running on http://127.0.0.1:5000
   * Debug mode: on/off
   ```

4. Press `Ctrl+C` to stop the application when finished.

## 🛠️ Technical Architecture

### Backend
- **Framework**: Flask (Python)
- **AI Integration**: Google Gemini API for natural language processing
- **Translation**: MarianMT models for multi-language support
- **PDF Processing**: PyMuPDF (fitz) for document text extraction
- **Database**: SQLite for user authentication

### Frontend
- **Templates**: Jinja2 templating engine
- **Styling**: Custom CSS with responsive design
- **Assets**: Static images and styling

### Key Components

#### 1. User Management
- Secure user registration and authentication
- Session-based login system
- Password storage (note: in production, use proper hashing)

#### 2. Document Analysis
- PDF upload functionality
- Text extraction from loan agreements
- Display of extracted content

#### 3. AI Advisory System
- Natural language question processing
- Multi-language translation support
- Gemini AI integration for financial advice
- Response formatting and presentation

## 📁 Project Structure

```
nlp_final/
├── app.py              # Main Flask application
├── gemini.py           # Gemini API integration
├── setup_db.py         # Database initialization
├── requirements.txt    # Python dependencies
├── users.db            # SQLite user database
├── static/             # CSS stylesheets and images
│   └── style.css       # Global styling
└── templates/          # HTML templates
    ├── index.html      # PDF upload page
    ├── login.html      # User login page
    ├── signup.html     # User registration page
    └── advisor.html    # AI advisor interface
```

## 🔧 Configuration

### API Keys
The application uses Google's Gemini API. You'll need to:
1. Obtain an API key from Google AI Studio
2. Update the API key in `app.py` and `gemini.py`



Additional languages can be added by extending the `LANG_CODE_TO_MODEL` dictionary.

## 🎯 Usage Guide

### 1. Account Setup
1. Navigate to the signup page
2. Create a new account with username and password
3. Login with your credentials

### 2. Document Analysis
1. Click on "Upload PDF" after login
2. Select a loan agreement document
3. View the extracted text content

### 3. Financial Advisory
1. Click on "Ask Question" to access the advisor
2. Enter your financial query
3. Receive AI-powered advice tailored to your question

## ⚠️ Important Notes

- This is a demonstration application with simplified security measures
- In production, implement proper password hashing and validation
- API keys should be stored securely using environment variables
- The user database implementation is basic and should be enhanced for production use

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini API for powering the AI advisory system
- Flask framework for web application development
- PyMuPDF for PDF processing capabilities
- MarianMT models for language translation
