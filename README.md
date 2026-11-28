# ReviseAI 

ReviseAI is an AI-powered revision website built with Python and Flask. It is designed to help students organise their revision, create flashcards and test their knowledge using automatically generated quizzes.

## Features

- **Revision Notes:** Browse subjects and topics and access organised revision notes.
- **Flashcards:** Create, view and manage your own flashcards.
- **AI Flashcard Generation:** Generate flashcards from revision notes using AI.
- **AI Quiz Generation:** Generate 10-question quizzes from revision notes, containing 5 multiple-choice questions and 5 written questions.
- **Automatic Marking:** Multiple-choice answers are automatically marked, while written answers are assessed using AI.
- **Quiz Results:** Save quiz results for later reference.
- **Local Data Storage:** Uses SQLite to store application data locally.

## Technologies Used

- **Python** – Main programming language.
- **Flask** – Web framework used to build the application.
- **HTML, CSS and JavaScript** – Front-end structure, styling and interactivity.
- **SQLite** – Local database.
- **Groq API** – Powers AI flashcard generation, quiz generation and written-answer marking.
- **Git and GitHub** – Version control and project hosting.

## Installation and Setup

### 1. Clone the repository

Open a terminal and run:

```bash
git clone https://github.com/Maalik009/ReviseAI.git
```

Navigate into the project folder:

```bash
cd ReviseAI
```

### 2. Navigate to the application folder

```bash
cd AIProj
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure your environment variables

Create a file called `.env` inside the `AIProj` folder.

Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace `your_groq_api_key_here` with your own API key.

You can obtain an API key from [Groq](https://console.groq.com/).

**Important:** Never upload your `.env` file or share your API key publicly.

### 6. Run the application

From inside the `AIProj` folder, run:

```bash
python ReviseAI.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

The website should now be running locally.

## Internet Requirements

ReviseAI runs locally on your computer.

**Features that work without an internet connection:**
- Browsing locally stored revision notes.
- Creating and managing flashcards.
- Accessing locally saved data.
- Viewing previously saved quiz results.

**Features that require an internet connection:**
- AI flashcard generation.
- AI quiz generation.
- AI marking of written answers.

The Flask application must still be running to use the local website.

## Database

ReviseAI uses SQLite for local data storage. The database is initialised by the application when it starts.

The database file is stored locally and is not intended to be uploaded to GitHub.

## Project Structure

```text
ReviseAI/
│
├── AIProj/
│   ├── ReviseAI.py
│   ├── requirements.txt
│   ├── .env
│   ├── reviseai.db
│   │
│   ├── notes/
│   │   └── Subject revision notes
│   │
│   ├── static/
│   │   ├── style.css
│   │   └── Subject images
│   │
│   └── templates/
│       └── HTML templates
│
└── README.md
```

*Note: `.env` and `reviseai.db` are local files and should not be committed to GitHub.*

## Future Improvements

Possible future improvements include:
- Progress tracking.
- More detailed revision statistics.
- Additional subjects and revision resources.
- Further testing and improvements to AI reliability.

## Author

Developed as a personal programming project to explore Python, Flask, web development, databases and AI integration.
