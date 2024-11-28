# Django Flix API


## Table of Contents
- [Features](#features)
- [Endpoints](#endpoints)
- [Installation and Setup](#installation-and-setup)

---


## Features

## API Endpoints

To get more information on any of the endpoints just try to access them on the browser and check
the information provided by the Django Rest Framework Browsable API.

| Endpoint                    | Method | Description                 |
| --------------------------- | ------ | --------------------------- |
| **Actors**                  |   -    | -                           |
| ```/api/v1/actors/```       | GET    | List actors                 |
| ```/api/v1/actors/```       | POST   | Create a new actor          |
| ```/api/v1/actors/<pk>/```  | GET    | Get information of an actor |
| ```/api/v1/actors/<pk>/```  | PUT    | Update an actor             |
| ```/api/v1/actors/<pk>/```  | DELETE | Delete an actor             |
| **Genres**                  |   -    | -                           |
| ```/api/v1/genres/```       | GET    | List genres                 |
| ```/api/v1/genres/```       | POST   | Create a new genre          |
| ```/api/v1/genres/<pk>/```  | GET    | Get information of a genre  |
| ```/api/v1/genres/<pk>/```  | PUT    | Update a genre              |
| ```/api/v1/genres/<pk>/```  | DELETE | Delete a genre              |
| **Movies**                  |   -    | -                           |
| ```/api/v1/movies/```       | GET    | List movies                 |
| ```/api/v1/movies/```       | POST   | Create a new movie          |
| ```/api/v1/movies/<pk>/```  | GET    | Get information of a movie  |
| ```/api/v1/movies/<pk>/```  | PUT    | Update a movie              |
| ```/api/v1/movies/<pk>/```  | DELETE | Delete a movie              |
| **Reviews**                 |   -    | -                           |
| ```/api/v1/reviews/```      | GET    | List reviews                |
| ```/api/v1/reviews/```      | POST   | Create a new review         |
| ```/api/v1/reviews/<pk>/``` | GET    | Get information of a review |
| ```/api/v1/reviews/<pk>/``` | PUT    | Update a review             |
| ```/api/v1/reviews/<pk>/``` | DELETE | Delete a review             |





## Installation and Setup

### Prerequisites
- Python 3.8+
- Git
- Virtualenv
- Docker

### Steps
1. Clone this repository:
    ```bash
    git clone https://github.com/aguiarjv/django-flix-api
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Create the ```.env``` file. Example:
    ```bash
    POSTGRES_USER=django_testing
    POSTGRES_PASSWORD=postgres_password
    POSTGRES_DB=flix_api
    POSTGRES_PORT=5432
    ```

6. Start the Postgres DB using Docker:
    ```bash
    docker compose up -d
    ```

7. Apply migrations:
    ```bash
    python manage.py migrate
    ```

8. Create a superuser for admin panel access:
    ```bash
    python manage.py createsuperuser
    ```

9. Run the server:
    ```bash
    python manage.py runserver
    ```
