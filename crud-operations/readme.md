# 📖 Book Management API with FastAPI

This is a simple FastAPI application for managing books. It supports creating, retrieving, updating, and deleting book records using RESTful endpoints.

---

## 🚀 Setup & Run

Install dependencies:

```bash
pip install fastapi uvicorn
```

Run the API:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

## 📂 Endpoints

### `GET /books`

**Description:** Retrieve all books.

**Response:**

```json
[
  {
    "id": 1,
    "title": "Example Book",
    "author": "Author Name",
    "publisher": "Publisher Name",
    "published_date": "2022-01-01",
    "page_count": 250,
    "language": "en"
  }
]
```

---

### `POST /books`

**Description:** Add a new book.

**Request Body:**

```json
{
  "id": 2,
  "title": "New Book",
  "author": "Author Name",
  "publisher": "Publisher Name",
  "published_date": "2023-01-01",
  "page_count": 300,
  "language": "en"
}
```

**Response:**

```json
{
  "id": 2,
  "title": "New Book",
  "author": "Author Name",
  "publisher": "Publisher Name",
  "published_date": "2023-01-01",
  "page_count": 300,
  "language": "en"
}
```

---

### `GET /book/{book_id}`

**Description:** Retrieve a single book by its ID.

**Success Response:**

```json
{
  "id": 1,
  "title": "Example Book",
  "author": "Author Name",
  "publisher": "Publisher Name",
  "published_date": "2022-01-01",
  "page_count": 250,
  "language": "en"
}
```

**Failure Response:**

```json
{
  "detail": "Book not found"
}
```

---

### `PATCH /book/{book_id}`

**Description:** Update a book's details (except ID and published\_date).

**Request Body:**

```json
{
  "title": "Updated Title",
  "author": "Updated Author",
  "publisher": "Updated Publisher",
  "page_count": 320,
  "language": "fr"
}
```

**Response:**

```json
{
  "id": 1,
  "title": "Updated Title",
  "author": "Updated Author",
  "publisher": "Updated Publisher",
  "published_date": "2022-01-01",
  "page_count": 320,
  "language": "fr"
}
```

---

### `DELETE /book/{book_id}`

**Description:** Delete a book by its ID.

**Success Response:**

```json
{}
```

**Failure Response:**

```json
{
  "detail": "Book not found"
}
```

---

## 🧱 Data Models

### `Book`

| Field           | Type | Required |
| --------------- | ---- | -------- |
| id              | int  | ✅ Yes    |
| title           | str  | ✅ Yes    |
| author          | str  | ✅ Yes    |
| publisher       | str  | ✅ Yes    |
| published\_date | str  | ✅ Yes    |
| page\_count     | int  | ✅ Yes    |
| language        | str  | ✅ Yes    |

### `BookUpdateModel`

| Field       | Type | Required |
| ----------- | ---- | -------- |
| title       | str  | ✅ Yes    |
| author      | str  | ✅ Yes    |
| publisher   | str  | ✅ Yes    |
| page\_count | int  | ✅ Yes    |
| language    | str  | ✅ Yes    |

---

## ⚠️ Notes

* `books` list must be defined globally to avoid runtime errors.
* The `published_date` field is not updatable in PATCH.
* This is an in-memory API — changes will reset on server restart.
* For production, use a database like PostgreSQL or MongoDB.
