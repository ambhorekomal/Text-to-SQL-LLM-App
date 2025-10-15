
# Text-to-SQL Gemini Streamlit App

This project converts natural language questions into SQL queries using **Google Gemini API** and displays the results using **Streamlit**. It allows users to ask questions in English, and automatically generates SQL queries for a SQLite database.

---

## Features

- Convert English questions to SQL queries automatically
- Works with a SQLite database (`student.db`) containing columns: `NAME`, `CLASS`, `SECTION`, `MARKS`
- Uses **Google Gemini models** (like `gemini-2.5-flash`) for natural language understanding
- Interactive Streamlit web interface

---

## Project Structure

```

TEXT_TO_SQL/
│
├── app.py                  # Main Streamlit app
├── student.db              # SQLite database (local)
├── .env                    # API key (not included in repo)
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── .gitignore              # Ignored files like env and API keys

````

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/ambhorekomal/Text-to-SQL-LLM-App.git
cd Text-to-SQL-LLM-App
````

2. **Create a virtual environment and activate it**

```bash
python -m venv env
# Windows
.\env\Scripts\activate
# macOS / Linux
source env/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Add your API key**

Create a `.env` file in the project root and add:

```
GOOGLE_API_KEY=your_api_key_here
```

> **Do not push your `.env` file to GitHub** — it contains sensitive keys.

5. **Run the Streamlit app**

```bash
streamlit run app.py
```

6. **Ask questions in English** and see SQL results displayed interactively.

---

## Notes

* Make sure `student.db` is present in the project folder. You can create your own SQLite database if needed.
* The app uses the latest **Google Gemini model** (like `gemini-2.5-flash`). 
* `.gitignore` excludes `.env` and virtual environment files.


Do you want me to do that next?
```
