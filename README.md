# User-profile-management

Login, registration and manage profile :-
Small Django app for login, register and User profile management.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development purposes.

### Prerequisites

What things you need to install the software and how to install them

```
You will need to install dependencies given in requirements.txt file.
```

### Steps to run the app

1. create virtualenv

```
virtualenv djangoenv -p python3
```

Use this virtualenv
```
source ./djangoenv/bin/activate
```

2. Clone the project on your local machine
```
git clone https://github.com/arun3q/User-profile-management.git

or

download it in zip format.
```
3. cd into User-profile-management
```
cd User-profile-management
```

4. install dependencies
```
pip install -r requirements.txt
```

5.	Configure the database in settings.py file

```
first cd into authProject:
cd authProject

make changes in settings.py file to use MySQL DB.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

```
OR

You also have the option of utilizing MySQL option files. 
You can accomplish this by setting your DATABASES array like this:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}
```
You also need to create the /path/to/my.cnf file with similar settings from below
```
[client]
database = yourDBName
host = 0.0.0.0
user = username
PORT = 3306
PASSWORD = yourDBPassword
default-character-set = utf8
```

6. Make migrations and migrate
```
python manage.py makemigrations
python manage.py migrate
```
7. Build the static files
```
python manage.py collectstatic
```
8. Run the project
```
python manage.py runserver 0.0.0.0:8080

```
## Authors

* **Arun Yadav** - *Initial work*


## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details
