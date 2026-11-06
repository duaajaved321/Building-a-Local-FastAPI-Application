# Building a Local FastAPI Application

A beginner-friendly REST API built with **FastAPI**, **Uvicorn**, and **Pydantic**. The application demonstrates HTTP routing, request validation, JSON responses, and interactive API documentation through Swagger UI.

## Features

- `GET /` — returns a welcome message.
- `GET /patients` — retrieves all sample patient records.
- `POST /patients` — validates and adds a patient record.
- Pydantic validates names and ages before the endpoint function runs.
- FastAPI generates interactive Swagger documentation automatically.

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- Swagger UI

## Project Structure

```text
Building-a-Local-FastAPI-Application/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/duaajaved321/Building-a-Local-FastAPI-Application.git
cd Building-a-Local-FastAPI-Application
```

### 2. Create and activate an environment

Using Conda:

```bash
conda create -n fastapi_env python=3.11 -y
conda activate fastapi_env
```

Or create a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\\Scripts\\Activate.ps1
```

macOS / Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start the server

Run this command from the directory containing `main.py`:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

| Method | Endpoint | Description | Success status |
|---|---|---|---|
| GET | `/` | Welcome message | 200 |
| GET | `/patients` | Retrieve all patient records | 200 |
| POST | `/patients` | Add a patient record | 201 |

### Example POST request

Send JSON to `/patients`:

```json
{
  "name": "Ayesha",
  "age": 28
}
```

Example response:

```json
{
  "id": 3,
  "name": "Ayesha",
  "age": 28
}
```

### Validation rules

- `name` is required, must contain 1–100 characters after whitespace trimming, and must be a string.
- `age` is required, must be an integer greater than 0 and no greater than 120.
- Unexpected request fields are rejected.
- Invalid request data is rejected automatically with HTTP `422 Unprocessable Entity`.

## Interactive API Documentation

While the server is running, open:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

Use Swagger UI to send GET and POST requests and inspect the responses.

## Testing the API

1. Open `/docs`.
2. Expand `GET /` and select **Try it out**, then **Execute**.
3. Execute `GET /patients` to view the sample records.
4. Expand `POST /patients`, enter a valid JSON body, and execute it.
5. Run `GET /patients` again to confirm the new record appears.
6. Try an invalid age such as `0`, `-2`, or `121`; FastAPI should return `422`.

## Important Limitations

- Patient records are stored in a Python list in memory.
- All changes are lost when the server restarts.
- There is no database, authentication, authorization, or persistence layer.
- The sample records are fictional. Do not use real patient information.

This project is an introductory learning exercise, not a production-ready patient management system.

## What I Practised

- Setting up a dedicated Python environment.
- Running an API server with Uvicorn.
- Connecting HTTP routes to Python functions with FastAPI decorators.
- Understanding GET and POST requests.
- Validating request bodies with Pydantic models and `Field`.
- Testing successful requests and validation errors.
- Using automatically generated Swagger UI documentation.

## Author

**Dua Javed**
