# 📚 Learning Log (Django Learning Tracker)

Learning Log is a **Django-based web application** built by following the later chapters of *Python Crash Course* by Eric Matthes. It started as a simple project scaffold and has grown into a fully functional, login-protected web app that allows users to track topics they’re learning and write timestamped entries for each topic.

The application is styled with Bootstrap (via `django-bootstrap5`), supports user registration and authentication, and is configured for both local development and cloud deployment.

---

## 📖 Project Overview

Learning Log lets users:

- Create topics they’re actively learning about
- Add detailed, timestamped entries under each topic
- View and edit their own topics and entries
- Keep their data private and separated from other users

Key user flows:

- New users can **register an account**, log in, and immediately start adding topics.
- Each user sees only their own topics and entries.
- Logged-in users can:
  - Add new topics
  - Add new entries for a topic
  - Edit existing entries
  - Delete topics and entries (if implemented in views/templates)
- The UI adapts based on authentication state (different navbar options for logged-in vs anonymous users).

The project is configured to run locally with SQLite and can be deployed using Gunicorn and a managed PostgreSQL database via platform configuration files and `render.yaml`.

---

## 🧠 Skills & Concepts Demonstrated

- **Django Fundamentals**
  - Project and app structure (`ll_project`, `learning_logs`, `accounts`)
  - Models for `Topic` and `Entry`, linked to the built-in `User` model
  - Function-based views, URL routing, and templates
- **User Authentication & Authorization**
  - User registration flow using `UserCreationForm`
  - Login/logout integration using Django’s auth system
  - `@login_required` decorators to protect views
  - Per-user data ownership checks to restrict access to topics and entries
- **Forms and Validation**
  - Custom `ModelForm` classes for topics and entries
  - Handling GET vs POST requests for create/edit workflows
  - Inline form validation and error display
- **Templates & UI**
  - Base template with Bootstrap 5 layout and navigation
  - Auth-aware navbar (shows Register/Login or greeting + Logout)
  - Clean topic and entry pages with timestamped content
- **Deployment & DevOps**
  - `requirements.txt` for dependencies
  - `render.yaml` for deployment with Gunicorn
  - `.platform.app.yaml` and `platformshconfig` for Platform.sh-style deployment
  - `requirements_remote.txt` for production dependencies
  - Basic GitHub Actions workflow (`.github/workflows/django.yml`) to install dependencies and run tests on pushes/PRs
- **Data Management**
  - SQLite for local development
  - PostgreSQL configuration for production, driven by environment variables
  - Django migrations and database schema management

---

## 🚀 Development Progress

**Completed Milestones**

1. Created the base Django project and apps (`learning_logs`, `accounts`).
2. Defined models for `Topic` and `Entry`, linked to Django’s `User` model.
3. Implemented views and URL patterns for:
   - Home page
   - Listing user topics
   - Viewing a single topic and its entries
   - Creating new topics and entries
   - Editing existing entries
4. Added user registration, login, and logout flows using a dedicated `accounts` app.
5. Secured data access so each user only views and edits their own topics and entries.
6. Built templates with a shared Bootstrap-based layout (`base.html`).
7. Configured static file handling and `collectstatic` for deployment.
8. Added deployment configuration:
   - `render.yaml` (Gunicorn entrypoint)
   - `.platform.app.yaml` and `platformshconfig` for environment-based DB settings
   - `requirements_remote.txt` for production dependencies
9. Set up CI with GitHub Actions to run Django tests on pushes and pull requests.

**Planned Enhancements**

- Search or filtering for topics and entries
- Tagging or categorization of topics
- Rich-text support for entries (e.g., Markdown)
- Pagination or archiving for long-running topic histories
- Additional tests to cover more views and edge cases

---

## 📂 File Structure

```text
ll_project/
├── manage.py                 # Django management script (runserver, migrate, etc.)
├── db.sqlite3                # Local development database (SQLite)
├── requirements.txt          # Core Python/Django dependencies
├── requirements_remote.txt   # Extra dependencies for remote deployment
├── render.yaml               # Render.com deployment configuration
├── .platform.app.yaml        # Platform.sh app configuration
├── .github/
│   └── workflows/
│       └── django.yml        # GitHub Actions CI for tests
├── ll_project/               # Project settings and configuration
│   ├── __init__.py
│   ├── settings.py           # Installed apps, DB config, static files, etc.
│   ├── urls.py               # Site-wide URL routing
│   ├── wsgi.py               # WSGI entrypoint for Gunicorn
│   └── asgi.py               # ASGI entrypoint (if needed)
├── learning_logs/            # Core app for topics and entries
│   ├── models.py             # Topic and Entry models
│   ├── views.py              # Views for listing/creating/editing topics and entries
│   ├── urls.py               # App URL patterns
│   ├── forms.py              # Model forms for topics and entries
│   ├── templates/
│   │   └── learning_logs/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── topics.html
│   │       ├── topic.html
│   │       ├── new_topic.html
│   │       ├── new_entry.html
│   │       └── edit_entry.html
│   └── admin.py              # Admin registration for models
├── accounts/                 # Authentication and registration app
│   ├── views.py              # Register view
│   ├── urls.py               # Auth-related URLs
│   ├── templates/
│   │   └── registration/
│   │       ├── login.html
│   │       └── register.html
│   └── admin.py
├── .gitignore                # Git and environment ignores
├── main.py                   # IDE stub (not used to run the app)
└── README.md                 # Project documentation (this file)
```

> Note: The Django entrypoint is `manage.py`, not `main.py`.

---

## ▶️ How to Run (Local Development)

1. **Clone the project**

   ```bash
   git clone <your-repo-url>.git
   cd ll_project
   ```

2. **Create and activate a virtual environment** (recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate        # On macOS/Linux
   # venv\Scriptsctivate         # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional but useful for admin access)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to:

   - `http://127.0.0.1:8000/` – Home page  
   - `http://127.0.0.1:8000/admin/` – Admin site (for superuser)

---

## 💻 Requirements

- Python 3.10+  
- Django 5.2+  
- django-bootstrap5  
- SQLite (for local development)  
- PostgreSQL (for production deployments, via platform configuration)

All core dependencies are listed in `requirements.txt`. Production-specific extras are in `requirements_remote.txt`.

---

## 🌐 Deployment Notes

This project includes multiple deployment-oriented files:

- **Render.com**
  - `render.yaml` configures the app to:
    - Install requirements
    - Run `collectstatic`
    - Serve via Gunicorn using `ll_project.wsgi`
- **Platform.sh**
  - `.platform.app.yaml` and `platformshconfig` dynamically configure the database as PostgreSQL based on environment variables.
- **Static Files**
  - `STATIC_URL` and `STATIC_ROOT` are configured in `settings.py` so `collectstatic` can gather assets for production.

You can also adapt these configs for other platforms that support Python, Gunicorn, and Django.

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file (if present in your repository) or add one if you plan to open-source the project.

---

## 🔗 Related Projects

- [Alien Invasion](https://github.com/E-Conners-Lab/Alien_Invasion) – Pygame-based arcade shooter built from the final chapters of *Python Crash Course*.  
- [Python Crash Course Projects](https://github.com/ECbball333/Python-Crash-Course-Project) – Additional exercises and projects from the book (data visualization, simulations, etc.).

If you are hosting Learning Log publicly (for example on Render), you can add your live URL here:

- **Live Demo:** `https://the-learning-log.onrender.com/` 

---

## 📣 Developer Note

Learning Log marks a major step in moving from scripts and small exercises into **full-stack web development**. Building this project end-to-end has strengthened my experience with:

- Django models, views, templates, and forms
- Authentication and authorization in a real application
- Bootstrap-based UI design
- Environment-aware configuration for local development and cloud deployment
- Automated testing and CI using GitHub Actions

With this project complete and deployed, I’m using the same Python skills to tackle automation and testing in network engineering, bridging the gap between web development, scripting, and large-scale infrastructure.
