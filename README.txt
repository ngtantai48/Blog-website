# Django Blog
A simple blog website developed using Django Framework (Python language) - follows on MVT (Model-View-Template) architecture.

## Requirements
* MySQL Client 8.0
* Python version >= 3.10

## Install dependencies

##### Create virtual environemnt
* For windows
```
    python -m venv .venv
    source .venv\scripts\activate
```
##### Install dependencies
```
    pip install -r requirements.txt
```

## Config and run

##### Config environment variables
Copy the [Blog-website/config.env.template](Blog-website/config.env.template) to `Blog-website/config.env`, then open the file and change values for environment variables.

##### Migrate data
From the [Blog-website](Blog-website) folder, run this command:
```
python manage.py migrate
```

##### Collect static files
(For production only)
From the [Blog-website](Blog-website) folder, run this command:
```
python manage.py collectstatic
```

##### Run
From the [Blog-website](Blog-website) folder, run this command:
```
python manage.py runserver
```
