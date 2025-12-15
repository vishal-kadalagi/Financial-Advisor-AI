from flask import Flask, render_template, request, redirect, url_for, session
import google.generativeai as genai
import fitz  # PyMuPDF for PDF extraction
import io
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Configure Gemini API
genai.configure(api_key="AIzaSyDs2FPZtkNotJm_Okdz791hMOr7J_qdvy4")
model = genai.GenerativeModel('gemini-1.5-flash')

# Dummy user database
users = {}

# Supported language codes and models
LANG_CODE_TO_MODEL = {
    "hi": ("Helsinki-NLP/opus-mt-hi-en", "Helsinki-NLP/opus-mt-en-hi"),
    "fr": ("Helsinki-NLP/opus-mt-fr-en", "Helsinki-NLP/opus-mt-en-fr"),
    "es": ("Helsinki-NLP/opus-mt-es-en", "Helsinki-NLP/opus-mt-en-es"),
    # Add more as needed
}

def load_translation_models(src_lang):
    if src_lang == "en":
        return None, None, None, None
    to_en_model_name, from_en_model_name = LANG_CODE_TO_MODEL.get(src_lang, (None, None))
    if not to_en_model_name or not from_en_model_name:
        return None, None, None, None
    to_en_tokenizer = MarianTokenizer.from_pretrained(to_en_model_name)
    to_en_model = MarianMTModel.from_pretrained(to_en_model_name)
    from_en_tokenizer = MarianTokenizer.from_pretrained(from_en_model_name)
    from_en_model = MarianMTModel.from_pretrained(from_en_model_name)
    return to_en_tokenizer, to_en_model, from_en_tokenizer, from_en_model

def translate(text, tokenizer, model):
    if not tokenizer or not model:
        return text
    batch = tokenizer([text], return_tensors="pt", padding=True)
    gen = model.generate(**batch)
    return tokenizer.decode(gen[0], skip_special_tokens=True)

@app.route("/")
def home():
    # When the app is first loaded, it should go to the login page
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        # Check if the username exists and the password is correct
        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("index"))  # After login, redirect to index (PDF extraction page)
        else:
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        # Check if the username already exists
        if username in users:
            return render_template("signup.html", error="Username already exists")

        users[username] = password
        return redirect(url_for("login"))

    return render_template("signup.html")

@app.route("/logout")
def logout():
    session.pop("user", None)  # Remove user from session
    return redirect(url_for("login"))  # Redirect to login page after logging out

@app.route("/index", methods=["GET", "POST"])
def index():
    # Ensure the user is logged in, else redirect to login page
    if "user" not in session:
        return redirect(url_for("login"))

    pdf_explanation = None

    if request.method == "POST":
        pdf_file = request.files.get("pdf_file")

        if pdf_file and pdf_file.filename != "":
            pdf_explanation = extract_text_from_pdf(pdf_file)

    return render_template("index.html",
                           username=session["user"],
                           pdf_explanation=pdf_explanation)

@app.route("/advisor", methods=["GET", "POST"])
def advisor():
    if "user" not in session:
        return redirect(url_for("login"))

    advice = None
    translated_input = None
    user_input = None
    output_language = "en"

    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        language = request.form.get("language", "en")
        output_language = language

        if user_input:
            if language != "en":
                # Load MarianMT models for the selected language
                to_en_tokenizer, to_en_model, from_en_tokenizer, from_en_model = load_translation_models(language)
                # Translate input to English
                prompt_in_english = translate(user_input, to_en_tokenizer, to_en_model)
                translated_input = f"Translated ({language} → en): {prompt_in_english}"
            else:
                prompt_in_english = user_input
                translated_input = None

            # Get advice from Gemini
            response = model.generate_content(prompt_in_english)
            advice_in_english = response.text

            # Translate advice back to user's language if needed
            if language != "en":
                advice = translate(advice_in_english, from_en_tokenizer, from_en_model)
            else:
                advice = advice_in_english

    return render_template("advisor.html",
                           username=session["user"],
                           advice=advice,
                           user_input=user_input,
                           translated_input=translated_input,
                           output_language=output_language)

def extract_text_from_pdf(pdf_file):
    try:
        pdf_data = pdf_file.read()
        pdf_bytes = io.BytesIO(pdf_data)
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")

        pdf_text = ""
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            pdf_text += page.get_text()

        return pdf_text
    except Exception as e:
        return f"Error extracting text from PDF: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
