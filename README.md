🌐 Translator Service
Translator Service is a FastAPI-based web application that allows translating text into multiple languages simultaneously, storing requests in a database, and processing translations asynchronously in the background.

⚙️ Technologies  
Python 3.10+

FastAPI — web framework for building APIs

SQLAlchemy — ORM for database interaction

SQLite/PostgreSQL — supported databases

Bootstrap 5 — UI/UX design framework

Jinja2 — templating engine for HTML pages

dotenv — environment variable management

🧩 Key Features  
📄 Submit text for translation via web form or API.

🌍 Select multiple target languages at once.

📬 Store translation requests in the database.

🔄 Asynchronous background processing of translations.

📊 Check request status and view translation results.

🖥️ User interface rendered with HTML templates (index.html, results.html).

✅ CORS support for frontend integration.

📁 Project Structure  
.  
├── app/  
│   ├── main.py                # FastAPI main application  
│   ├── models.py              # SQLAlchemy models  
│   ├── schemas.py             # Pydantic schemas  
│   ├── crud.py                # CRUD utility functions  
│   ├── utils.py               # Translation processing logic  
│   ├── templates/  
│   │   ├── index.html         # Main page template  
│   │   └── results.html       # Results page template  
├── database.py                # Database connection and session  
├── .env                       # Environment variables config  
🚀 Quick Start  
Clone the repository  
  
git clone https://github.com/Lertss/Translator_AI
cd translator-service
Create a virtual environment and install dependencies
  

python -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  
Create .env file  


DATABASE_URL=sqlite:///./translations.db  
Run the application  


uvicorn app.main:app --reload  
Open in browser  


http://localhost:8000/index  
📬 API Endpoints  
Method	Endpoint	Description  
POST	/translate	Submit text for translation  
GET	/translate/{id}	Check status or get translation  
GET	/index	Web form for user interaction  

📌 Notes  
The translation system (e.g. translate_text()) is currently a stub — implementation or third-party API integration is needed.

Intended primarily for demonstration or educational purposes.  

🧑‍💻 Author  
Lert

