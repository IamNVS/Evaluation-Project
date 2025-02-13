
# Evaluation Project

## 🚀 Project Overview
A Django REST API for submitting evaluation requests. This project includes:
- **Django Rest Framework** for building the API.
- **Celery + Redis** for asynchronous processing.
- **PostgreSQL** as the database.
- **Resend API** for email notifications.

## ⚙️ Tech Stack
- **Django Rest Framework**
- **Celery + Redis** (for background tasks)
- **PostgreSQL** (database)
- **Resend API** (for email notifications)

## 📦 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/evaluation-project.git
cd evaluation-project
```

### 2️⃣ Set Up Virtual Environment
```sh
python -m venv venv
venv\Scripts\activate      
```

### 3️⃣ Install Dependencies
```sh
pip install djangorestframework
pip install celery redis
pip install resend
```

### 4️⃣Configure PostgreSQL in settings.py

```ini
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5️⃣ Run Migrations
```sh
python manage.py makemigrations evaluations
python manage.py migrate
```

### 6️⃣ Start Redis Server
```sh
redis-server
```

### 7️⃣ Start Celery Worker
```sh
celery -A evaluation_project worker --loglevel=info
```

### 8️⃣ Run Django Server
```sh
python manage.py runserver
```

## 📌 API Usage
### 1️⃣ Submit Evaluation Request
**Endpoint:** `POST /api/evaluate/`

**Request Body:**
```json
{
    "input_prompt": "Evaluate this text",
    "email": "user@example.com"
}
```

**Response:**
```json
{
    "id": 1,
    "message": "Evaluation request submitted."
}
```

### 2️⃣ Retrieve Evaluation Status
**Endpoint:** `GET /api/evaluate/1/`

**Response:**
```json
{
    "id": 1,
    "input_prompt": "Evaluate this text",
    "status": "completed",
    "result": "Simulated evaluation result: 78",
    "created_at": "2024-02-13T12:34:56Z",
    "updated_at": "2024-02-13T12:35:56Z"
}
```

---

### 🎯 Focus on
- ✅ Clean API design (proper request validation, clear responses).
- ✅ Async processing using Celery.
- ✅ External integration (Resend API for emails).
- ✅ Code quality (comments, unit tests, best practices).
- ✅ Clear documentation (README, API usage, setup guide).
- ✅This readme.md is made by help of ChatGPT.

 
