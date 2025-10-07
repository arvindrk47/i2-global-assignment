# To-Do List API Documentation

This document provides complete setup and usage instructions for the **To-Do List API**.  
You can run the project either with **Python (manage.py)** or using **Docker Compose**.

---

## 1. Installation and Setup

### Option A: Run Locally (Using Python)

1. **Clone the repository**
   ```bash
   git clone https://github.com/arvindrk47/i2-global-assignment
   cd i2-global-assignment/backend
   ```

2. **Create and activate the virtual enviroment**
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Server**
   ```
   python manage.py runserver
   ```

### Option B: Run with Docker Compose
6. **Run with Docker compose**
   ```
   docker compose up --build
   ```

## 2. API Usage
> All API requests require a valid JWT token in the Authorizatoion header

```
Authorization: Bearer <access_token>
```

## 3. Endpoints

### Login
8. **Login URL**
   ```
   http://localhost:8000/api/login/
   ```
   Request output
   ```
   {
     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczODk0NzAwMCwiaWF0IjoxNzM4ODYwNjAwLCJqdGkiOiJhYmNkZWYxMjM0NTY3ODkwYWJjZCIsInVzZXJfaWQiOjF9.-2fB5RzZVZyA0vH5cWbnLxYF6R3nO0sLjDgfDeP8-rQ",
     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM4ODY0MjAwLCJpYXQiOjE3Mzg4NjA2MDAsImp0aSI6ImRmZTg3NjU0MzIxMWFiY2RlZmdoaSIsInVzZXJfaWQiOjF9.PW9DcO3P7slR3mZ2eJgUPlT9Bj49Tg6LkNwA8E4e8x8"
   }
   ```

### Logout
9. **Logout URL**
   > Logs out the user and blacklists the refresh token.
   > http://localhost:8000/api/logout/

### Register a New User
10. **Register a new User**

   > POST http://localhost:8000/api/register/

   Allows the User to register

   Request Body
   ```
   {
     "username": "arvindrk",
     "email": "arvind@example.com",
     "password": "password",
     "confirm_password": "password"
   }
   ```

   Response
   ```
   {
     "message": "User registered successfully"
   }
   ```

### Get All Users
11. **Get All Users**
   > http://localhost:8000/api/users/

   > Headers Should be present

   Response
   ```
   [
     {
       "id": 1,
       "username": "arvindrk",
       "email": "arvind@example.com",
       "created": "2025-10-06",
       "last_update": "2025-10-06"
     },
     {
       "id": 2,
       "username": "testuser",
       "email": "test@example.com",
       "created": "2025-10-07",
       "last_update": "2025-10-07"
     }
   ]
   ```

### List All Notes
12. **List All Notes**
   > GET http://localhost:8000/api/notes/

   > Lists all notes belonging to the logged-in user.

   ```
   [
     {
       "id": 1,
       "note_title": "Meeting Notes",
       "note_content": "Discuss project deadlines",
       "created_on": "2025-10-06",
       "updated_on": "2025-10-06T12:20:45.234Z",
       "user": 9
     }
   ]
   ```

### Create New Note
13. **Create New Note**
   > POST http://localhost:8000/api/notes/

   > Request Body
   ```
   {
     "note_title": "Project Plan",
     "note_content": "Finalize deliverables for next sprint"
   }
   ```

   > Response 
   ```
   {
     "id": 2,
     "note_title": "Project Plan",
     "note_content": "Finalize deliverables for next sprint",
     "created_on": "2025-10-06",
     "updated_on": "2025-10-06T13:10:12.120Z",
     "user": 9
   }
   ```

### Retrieve a Single Note
14. **Retrieve a single note**
   > GET http://localhost:8000/api/notes/2/

   > Response
   ```
   {
     "id": 2,
     "note_title": "Project Plan",
     "note_content": "Finalize deliverables for next sprint",
     "created_on": "2025-10-06",
     "updated_on": "2025-10-06T13:10:12.120Z",
     "user": 9
   }
   ```

### Delete a Note
15. **Delete the note**
   > DELETE http://localhost:8000/api/notes/2/

   > Response
   ```
   {
     "message": "Note deleted successfully"
   }
   ```

Note: This documnet may have some small typos, but it shoud be easy to follow. If you spot any isues, feel free to corect them in your local copy.
