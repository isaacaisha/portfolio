# ·SìįSí· Portfolio

A responsive, full-stack Django portfolio site showcasing web apps, APIs and AI integrations, with a dynamic projects database, contact form, and admin-only notifications panel.

![Platform Demo](static/assets/img/portfolio.jpg)

---

## 🚀 Features

* **Dynamic Projects**
  All portfolio items are stored in a PostgreSQL database and rendered via Django models & templates.
* **AI Chat & Drawing Generator**
  GPT-4 DBT chatbot + DALL·E art generator
* **E-commerce Platform**
  Dockerized Django shop with Stripe & PayPal
* **FastAPI Microservice**
  Async endpoints, JWT auth, PostgreSQL & Redis
* **Co-Ownership CRM**
  Multi-tenant Django app with role-based dashboards
* **Flask Blog CMS & Cafe Finder**
  Rapid prototypes with user auth, CRUD, WTForms, Flask-Login
* **Contact Form**
  Custom Django form sends email + persists messages; superuser-only notifications page
* **Dockerized**
  Production & development `docker-compose` configurations
* **CI / CD Ready**
  Gunicorn + WhiteNoise + Docker + PostgreSQL

---

## 📦 Prerequisites

* Docker & Docker Compose
* (Or) Python 3.12, PostgreSQL
* A `.env.dev` and `.env.prod` file (see below)

---

## 🛠️ Local Development

1. Copy & edit your development variables:

   ```bash
   cp .env.dev.example .env.dev
   ```
2. Build & start containers:

   ```bash
   docker-compose -f docker-compose.dev.yml up --build
   ```
3. Visit [http://localhost:8079](http://localhost:8079)

Your code is mounted into the container—changes reload automatically.

---

## ⚙️ Production Setup

1. Copy & edit your production variables:

   ```bash
   cp .env.prod.example .env.prod
   ```
2. Build & start containers:

   ```bash
   docker-compose -f docker-compose.prod.yml up --build -d
   ```
3. Migrations, static files & entrypoint run automatically.
4. Your site will be available on port 8085.

---

## ⚙️ Environment Variables

Both `.env.dev` and `.env.prod` share:

```dotenv
SECRET_KEY=...
ENVIRONMENT=dev|prod
DEBUG=True|False
ALLOWED_HOSTS=...
DATABASE_URL=postgresql://USER:PASS@HOST:5432/DB
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=you@example.com
EMAIL_HOST_PASSWORD=...
DEFAULT_FROM_EMAIL=you@example.com
```

---

## 📋 Django Commands

* **Migrations**

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
* **Create superuser**

  ```bash
  python manage.py createsuperuser
  ```
* **Collect static**

  ```bash
  python manage.py collectstatic
  ```
* **Run server**

  ```bash
  python manage.py runserver
  ```

---

## 🔧 Project Structure

```
├── portfolio/                # Django project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio_app/            # Main application
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       └── notifications.html
├── Dockerfile
├── entrypoint.sh
├── docker-compose.dev.yml
├── docker-compose.prod.yml
├── requirements.txt
└── README.md
```

---

## 🎨 Frontend

* Bootstrap 5 & FontAwesome
* Responsive design
* Modal portfolio items with dynamic content

---

## 🔒 Security & Permissions

* Admin panel protected by an `admin_proxy` view—redirects non-superusers with an “Access denied” message.
* Project creation & notifications pages only accessible to superusers.

---

## 📫 Contact

If you run into issues or have suggestions, open an issue or email me at `<medusadbt@gmail.com>`.

---

> Built with ❤️ by ·SìįSí·Dbt· – pushing digital boundaries one line of code at a time.
