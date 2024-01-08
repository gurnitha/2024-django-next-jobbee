# 2024-django-next-jobbee
Membuat Jobportal menggunakan Django 4.2 dan NextJs 12.1.0
https://github.com/gurnitha/2024-django-next-jobbee


## 1. SETUP

#### 1. Membuat repositori '2024-django-next-jobbee' di Github

        new file:   .gitignore
        modified:   README.md

#### 2. Membuat virtual environment

        E:\_WORKSPACE\2024\django-api\ghulam-abbas\2024-django-next-jobbee
        λ python -m venv venv31042

        modified:   README.md

#### 3. Install Django versi 4.2.2

        λ venv31042\Scripts\activate.bat
        (venv31042) λ 
        (venv31042) λ python.exe -m pip install --upgrade pip
        (venv31042) λ pip install django==4.2.2

#### 4. Install some drivers/modules

        (venv31042) λ pip install boto3 django-cors-headers django-dotenv django-filter django-storages djangorestframework djangorestframework-simplejwt geocoder gunicorn whitenoise psycopg2 dj-database-url

        modified:   README.md

#### 5. Create proyek django 'backend'

        modified:   README.md
        new file:   backend/backend/__init__.py
        new file:   backend/backend/asgi.py
        new file:   backend/backend/settings.py
        new file:   backend/backend/urls.py
        new file:   backend/backend/wsgi.py
        new file:   backend/manage.py
