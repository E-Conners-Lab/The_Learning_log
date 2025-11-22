
# Learning Log

Learning Log is a Django-based web application built by following the Python Crash Course by Eric Matthes. 
This project started from scratch and gradually developed into a fully functional web-based platform 
that allows users to track topics they’re learning and make timestamped entries about them.

## Key Features

- User registration, login, and logout functionality
- Each user has a private dashboard of their topics and entries
- CRUD operations:
  - Add, edit, and delete topics
  - Add, edit, and delete entries under each topic
- Data access restricted per user
- Navigation tailored based on login state
- Responsive front-end using Bootstrap
- Deployed on Render.com using a custom `render.yaml` config
- GitHub for version control and CI/CD integration

## Lessons Learned

This project provided hands-on experience across the **entire Django framework**, including:
- Views, URLs, templates, models, and forms
- Customizing templates using Bootstrap and template tags
- Handling user permissions and authentication
- Creating dynamic links, context-driven templates, and database logic
- Deployment using modern cloud tools

Additionally, I explored writing YAML files and honed my HTML/CSS skills to improve frontend presentation. 
The learning journey required switching from the suggested deployment on platform.sh to Render.com, and 
resolving several build, environment, and template issues along the way.

## Developer Note

Although I'm a network engineer at heart, this project has opened my eyes to the world of **full-stack development**. 
With Learning Log complete, I plan to build the final Python Crash Course project — a simple alien invasion game — 
before shifting my focus back to network automation. Next, I’ll explore networking APIs and begin building tools 
and dashboards with Python, and even experiment with LLM integration for network tasks.

## Live Demo

You can view the live project here:
https://the-learning-log.onrender.com/

## Get Started Locally

```bash
git clone https://github.com/YOUR_USERNAME/The_Learning_log.git
cd The_Learning_log
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

---

Built with passion, learning, and a lot of troubleshooting.
