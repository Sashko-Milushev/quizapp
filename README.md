# QuizApp - Online Quiz Application API

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [API Documentation](#api-documentation)
    - [Authentication](#authentication)
    - [User Registration](#user-registration)
    - [Quiz Sessions](#quiz-sessions)
    - [Ranking](#ranking)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to QuizApp - the API for an online quiz application. The application offers a fun and engaging way for users to test
their knowledge through various quizzes. Whether you're looking to challenge yourself, learn new facts, or simply have a
good time, QuizApp provides a diverse range of quizzes that cater to different interests and topics.

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed on your system:

- Python (3.7+)
- Django (3.2+)
- Django REST framework

### Installation

1. **Clone the QuizApp repository:**

   ```
   git clone https://github.com/Sashko-Milushev/quizapp.git
   cd quizapp
   ```

2. **Create a virtual environment (optional but recommended):**
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

   ```
3. **Install the required Python packages:**
    ```
    pip install -r requirements.txt

   ```
4. **Create and apply database migrations:**
    ```
    python manage.py makemigrations
    python manage.py migrate

   ```
5. **Create a superuser account for admin access:**
    ```
    python manage.py createsuperuser

   ```
6. **Start the development server:**
    ```
    python manage.py runserver

   ```

Your QuizApp API should now be running locally at http://localhost:8000/.

## API Documentation

### Authentication

**Get Access Token**

- **URL:** `/api/token/`
- **Method:** `POST`
- **Description:** Obtain an access token by providing valid user credentials.
- **Request:**
  ```json
  {
    "email": "your@email.com",
    "password": "your_password"
  }
  ```
- **Response:**
  ```json
  {"access": "your_access_token",
  "refresh": "your_refresh_token"}
  ```

**Refresh Access Token**

- **URL:** `/api/token/refresh/`
- **Method:** `POST`
- **Description:** Refresh an access token using a refresh token.
- **Request:**
  ```json
  {"refresh": "your_refresh_token"}
  ```
- **Response:**

```json
  {
  "access": "your_new_access_token"
}
```

## User Registration

- **URL:** `/api/accounts/register/`
- **Method:** `POST`
- **Description:** Register a new user.
    - **Request:**
  ```json
    {
      "email": "new@email.com",
      "username": "new_username",
      "password": "new_password"
    }
  ```
- **Response:**
    ```json
    {
      "message": "User registration successful."
    }
    ```

## Quiz Sessions

- **URL:** `/api/quiz/start-quiz-session/`
- **Method:** `POST`
- **Description:** Start a new quiz session.
- **Request:**
  ```json
  {
    "category_id": 1,
    "number_of_correct_answers": 5
  }
  ```
- **Response:**
  ```json
    {
      "points": 10
    }
  ```

## Ranking

- **URL:** `/api/quiz/ranking/`
- **Method:** `GET`
- **Description:** Get the ranking list of users based on their points.
- **Response:**
  ```json
  [
    {
      "user": "username1",
      "points": 20
    },
    {
      "user": "username2",
      "points": 15
    }
  ]
  ```

## Additional Notes

- Authentication in QuizApp is handled using Django REST framework SimpleJWT.
- The django-cors-headers package is used to allow cross-origin resource sharing (CORS) for better communication with
  the frontend.

## Contributing

QuizApp is an open-source project, and contributions are welcome. Feel free to submit pull requests, report issues, or
suggest new features to help enhance the platform.





