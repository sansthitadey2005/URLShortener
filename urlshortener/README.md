# URL Shortener - CodeAlpha

## Description
A simple URL Shortener backend built using Django REST Framework.

## Features
- Shortens long URLs
- Generates unique short codes
- Redirects short URLs to original URLs
- Stores URLs in SQLite database

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite

## API Endpoint

POST /shorten/

Request:

```json
{
    "url":"https://www.google.com"
}
```

Response:

```json
{
    "short_code":"ABC123",
    "short_url":"http://127.0.0.1:8000/ABC123"
}
```

Run:

```
python manage.py runserver
```