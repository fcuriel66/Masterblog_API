# Masterblog_API

Masterblog_API is a blog platform project with a Flask-based backend API and a simple frontend. It provides endpoints for creating, retrieving, updating, deleting, and searching blog posts, along with flexible query features like sorting and filtering.

## Features

* RESTful API built with Flask
* Create, read, update, and delete posts
* Search posts by title and content
* Sorting support (by title or content, ascending or descending)
* Frontend to interact with the API
* Modular backend/frontend structure

## Project Structure

```
Masterblog_API/
├── backend/       # Flask API (main app, routes, models)
├── frontend/      # Client-side files (HTML, CSS, JS)
└── README.md
```

## Installation & Setup

### Prerequisites

* Python 3.9+
* pip (Python package manager)

### Backend Setup

1. Navigate into the backend directory:

   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask server:

   ```bash
   flask run
   ```

   The API will be available at `http://127.0.0.1:5000`.

### Frontend Setup

1. Navigate into the frontend directory:

   ```bash
   cd frontend
   ```
2. Open `index.html` in a browser to interact with the API.

## API Endpoints

### Posts

* `GET /api/posts` — Retrieve all posts (supports optional sorting).
* `POST /api/posts` — Create a new post.
* `GET /api/posts/<id>` — Retrieve a single post by ID.
* `PUT /api/posts/<id>` — Update a post by ID.
* `DELETE /api/posts/<id>` — Delete a post by ID.

### Search

* `GET /api/posts/search?title=<text>&content=<text>`
  Search posts by title, content, or both.

### Sorting Parameters

* `?sort=title&direction=asc|desc`
* `?sort=content&direction=asc|desc`

Example:

```
/api/posts?sort=title&direction=desc
```

## Error Handling

* `400 Bad Request` — Invalid query parameters (e.g., unsupported sort field).
* `404 Not Found` — Resource not found.

## License

None required
