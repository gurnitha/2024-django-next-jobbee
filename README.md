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

#### 6. Create Postgres DB dan konek DB dengan proyek

        STEPS:

        1. PostgreSQL db was installed
        2. Open PgAdmin 4 + password: postgres
        3. Create a new db: 
           - name: 2024_django_next_jobbee_api
           - owner: postgres
           - password:postgres? not sure
        4. Start server 

        Note: It raised issues as seen bellow:

        raise ImproperlyConfigured(
        django.core.exceptions.ImproperlyConfigured: Could not find the GDAL library (tried "gdal306", "gdal305", "gdal304", "gdal303", "gdal302", "gdal301", "gdal300", "gdal204", "gdal203", "gdal202"). Is GDAL installed? If it is, try setting GDAL_LIBRARY_PATH in your settings.

        modified:   README.md
        modified:   backend/backend/settings.py

         NEXT: Setup GDAL on Windows

#### 6. Setup GDAL on Windows

        STEPS:

        1. GeoDjango Installation
           > https://docs.djangoproject.com/en/4.2/ref/contrib/gis/install/
        2. Download gdal source: https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal
           GDAL-3.4.3-cp310-cp310-win_amd64.whl
        3. Download and install osgeo source: https://trac.osgeo.org/osgeo4w/
        4. Modify Windows environment
           1. Create a new file: setup.txt (any where) + open it
           2. Copy and paste this code:

           set OSGEO4W_ROOT=C:\OSGeo4W
           set GDAL_DATA=%OSGEO4W_ROOT%\apps\gdal\share\gdal
           set PROJ_LIB=%OSGEO4W_ROOT%\share\proj
           set PATH=%PATH%;%OSGEO4W_ROOT%\bin
           reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path /t REG_EXPAND_SZ /f /d "%PATH%"
           reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v GDAL_DATA /t REG_EXPAND_SZ /f /d "%GDAL_DATA%"
           reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PROJ_LIB /t REG_EXPAND_SZ /f /d"%PROJ_LIB%"
           
           3. Save the file
           4. Change the file extention from .txt to .bat
           5. Run it as administrator
           6. Resutls
              - Path file will change automatically
              - New folder added automaically to C:\OSGeo4W
        5. Run the server

        DONE :)

        modified:   README.md
        modified:   backend/backend/settings.py