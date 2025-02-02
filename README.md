# FAQ Management System

A Django-based FAQ management system with multilingual support and a REST API.

## Table of Contents
- [Project Structure](#project-structure)

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Docker Setup](#docker-setup)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)



## Project Structure

The project structure is as follows:

```
faq-management/
├── Faqs_management/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── pytest.ini
│   └── .flake8
├── Faqsapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── languages.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_faq_options_faq_answer_bn_faq_answer_hi_and_more.py
│   │   └── 0003_alter_faq_options_remove_faq_answer_bn_and_more.py
│   ├── models.py
│   ├── redis_handler.py
│   ├── serializer.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── requirements.txt
├── .dockerignore
├── .env
├── .gitignore
└── README.md
```


## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.8+
- Django 5.1+
- Redis
- Docker (optional, for containerization)
- pip

### Steps

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/faq-management.git
    cd faq-management
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up Redis:**

    Ensure Redis is installed and running on your machine. You can download it from [here](https://redis.io/download).

5. **Run migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

8. **Access the admin panel:**

    Open your browser and go to `http://127.0.0.1:8000/admin` and log in with the superuser credentials.

## Usage

### API Endpoints

- **List FAQs:** `GET /api/faqs/`
- **Create FAQ:** `POST /api/faqs/`
- **Retrieve FAQ:** `GET /api/faqs/{id}/`
- **Update FAQ:** `PUT /api/faqs/{id}/`
- **Delete FAQ:** `DELETE /api/faqs/{id}/`

### Examples

#### List FAQs

```sh
curl -X GET "http://127.0.0.1:8000/api/faqs/"
```

#### Create FAQ

```sh
curl -X POST "http://127.0.0.1:8000/api/faqs/" -H "Content-Type: application/json" -d '{
    "question": "What is Django?",
    "answer": "Django is a web framework."
}'
```

#### Retrieve FAQ

```sh
curl -X GET "http://127.0.0.1:8000/api/faqs/1/"
```

#### Update FAQ

```sh
curl -X PUT "http://127.0.0.1:8000/api/faqs/1/" -H "Content-Type: application/json" -d '{
    "question": "What is Django?",
    "answer": "Django is a high-level Python web framework."
}'
```

#### Delete FAQ

```sh
curl -X DELETE "http://127.0.0.1:8000/api/faqs/1/"
```

### Language Selection

You can select the language for the question using the `?lang=` query parameter. 
You can translate to all languages supported by Google Translate by specifying the desired language code. 
For example:

To translate to Bengali, use `?lang=bn`:

```sh
curl -X GET "http://127.0.0.1:8000/api/faqs/?lang=bn"
```

To translate to Hindi, use `?lang=hi`:

```sh
curl -X GET "http://127.0.0.1:8000/api/faqs/?lang=hi"
```

To translate to Spanish, use `?lang=es`:

```sh
curl -X GET "http://127.0.0.1:8000/api/faqs/?lang=es"
```

## Running Tests

We use pytest for running tests. Ensure all tests pass before submitting a pull request.

```sh
pytest
```

## Docker Setup

To run the project using Docker, follow these steps:

1. **Build and run the Docker container:**

    ```sh
    docker-compose build
    docker-compose up
    ```

2. **Apply migrations:**

    After the container is up and running, open a new terminal and run the following command to apply migrations:

    ```sh
    docker-compose exec web python manage.py migrate
    ```
