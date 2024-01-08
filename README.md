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

#### 7. Protecting the sensitive file

        STEPS:

        1. Check the installed modules

        λ pip list                                     
        Package                       Version          
        ----------------------------- ------------     
        asgiref                       3.7.2            
        beautifulsoup4                4.12.2           
        boto3                         1.34.14          
        botocore                      1.34.14          
        certifi                       2023.11.17       
        charset-normalizer            3.3.2            
        click                         8.1.7            
        colorama                      0.4.6            
        decorator                     5.1.1            
        dj-database-url               2.1.0            
        Django                        4.2.2            
        django-cors-headers           4.3.1            
        ==> django-dotenv                 1.4.2            
        ==> django-environ                0.11.2           
        django-filter                 23.5             
        django-storages               1.14.2           
        djangorestframework           3.14.0           
        djangorestframework-simplejwt 5.3.1            
        docopt                        0.6.2            
        future                        0.18.3           
        GDAL                          3.4.3            
        geocoder                      1.38.1           
        gunicorn                      21.2.0           
        idna                          3.6              
        jmespath                      1.0.1            
        Js2Py                         0.74             
        packaging                     23.2             
        pip                           23.3.2           
        pipwin                        0.5.2            
        psycopg2                      2.9.9            
        pyjsparser                    2.7.1            
        PyJWT                         2.8.0            
        PyPrind                       2.11.3           
        pySmartDL                     1.3.4            
        python-dateutil               2.8.2
        python-dotenv                 1.0.0
        python-env                    1.0.0            
        python-environ                0.4.54           
        pytz                          2023.3.post1     
        ratelim                       0.1.6            
        requests                      2.31.0           
        s3transfer                    0.10.0           
        setuptools                    63.2.0           
        six                           1.16.0           
        soupsieve                     2.5              
        sqlparse                      0.4.4            
        typing_extensions             4.9.0            
        tzdata                        2023.4           
        tzlocal                       5.2              
        urllib3                       2.0.7            
        whitenoise                    6.6.0

        Note: requirements to setup environ variables are full filled.

        2. Setup environ variables in settings.py
           
        modified:   README.md
        modified:   backend/backend/settings.py

#### 8. Install a fresh new PostgreSQL 16.1 and create a new db

        modified:   README.md

        Note:

        1. Create a new db '2024_django_next_jobbee_api' 
        2. Password: root
        3. Port    : 5433
        4. Tested: (venv31042) λ python manage.py runserver

        :)

#### 9. ALTER USER postgres WITH PASSWORD 'alamatrmhdibali'

        modified:   README.md

        Note:

        1. Sukses alter user dengan password baru
        2. Tested

        :) 


## 2. START WITH JOB RESOURCE                                   

#### 1. Create a new app 'job'

        modified:   README.md
        new file:   backend/job/__init__.py
        new file:   backend/job/admin.py
        new file:   backend/job/apps.py
        new file:   backend/job/migrations/__init__.py
        new file:   backend/job/models.py
        new file:   backend/job/tests.py
        new file:   backend/job/views.py                                   

#### 2. Register job app to settings.py

        modified:   README.md
        modified:   backend/backend/settings.py

        Note: tested :)