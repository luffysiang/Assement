Technologies Used
    FastAPI (Backend)
    JavaScript (Frontend)
    SQLite (Database)

Project Structure
project-root/
    backend/
        main.py           # FastAPI backend code
        database.db       # SQLite database file
        requirements.txt  # List of backend dependencies

    frontend/
        index.html        # Main HTML file for the frontend
        style.css         # CSS styling for the frontend
        script.js         # JavaScript code for the frontend

Backend Setup
1. Install required packages by running: 
    pip install -r backend/requirements.txt
2. Start the FastAPI server:
    uvicorn backend.main:app --reload
The server should be running at http://127.0.0.1:8000.

Frontend Setup
Open the frontend/index.html file in a web browser. You can use a local server or directly open the file in your browser.

Database
The SQLite database is stored in the backend/database.db file.

Usage
1. Register an account with username and password.
2. Log in the account which you registered.




