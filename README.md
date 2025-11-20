# 🧠 The Learning Log

The Learning Log is a Django-based web application that lets users track topics they are learning about and record their progress over time. This app was built by following the [Python Crash Course](https://nostarch.com/pythoncrashcourse) by Eric Matthes and serves as a hands-on introduction to Django and web development.

---

## 🚀 Features

- User registration and authentication
- Add and manage learning topics
- Write journal-style entries under each topic
- View all topics and their related entries
- Clean, minimalist UI using Django templates and Bootstrap

---

## 🛠 Tech Stack

- **Python 3.x**
- **Django 4.x**
- HTML, CSS, Bootstrap (optional)
- SQLite (default) or PostgreSQL/MySQL (optional)

---

## 📦 Installation

> ⚠️ Ensure Python and pip are installed. Recommended: Use a virtual environment.

```bash
# Clone the repository
git clone https://github.com/E-Conners-Lab/The_Learning_log.git
cd The_Learning_log

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run initial migrations
python manage.py migrate

# Start the development server
python manage.py runserver

```
## 🧪 Usage

- Visit `http://127.0.0.1:8000/admin` to manage Topics and Entries
- Use the Django admin interface to:
  - Add new topics (e.g. "Python", "APIs", "Networking")
  - Add journal entries under each topic

> ⚠️ The public-facing user interface (registration, login, add/view entries) is not yet implemented.
