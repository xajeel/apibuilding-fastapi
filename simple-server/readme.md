# 📘 FastAPI Simple Server API – Documentation

This API is a simple demonstration using **FastAPI**, showcasing:

- Path Parameters
- Query Parameters
- Optional Parameters
- Request Body
- HTTPException handling

---

## 🚀 Setup & Run

Make sure you have FastAPI and Uvicorn installed:

```bash
pip install fastapi uvicorn
```

Run the API using:

```bash
uvicorn main:app --host 0.0.0.0 --port 8010 --reload
```

---

## 📁 Endpoints

### `GET /`

**Description**: Returns a welcome message.

**Response:**

```json
{
  "message": "Hello World"
}
```

---

### `GET /greet/{name}`

**Path Parameter**: `name` (str)\
**Description**: Greets the user using their name.

**Example Request:**

```
GET /greet/sajeel
```

**Response:**

```json
{
  "message": "Hello, sajeel"
}
```

---

### `GET /details?username=`

**Query Parameter**: `username` (str)\
**Description**: Searches for a username in a hardcoded list.

**Example Request:**

```
GET /details?username=ali
```

**Success Response:**

```json
{
  "message": "Found User details abour ali"
}
```

**Failure Response:**

```json
{
  "detail": "malik not found"
}
```

---

### `GET /greeting?username=`

**Query Parameter (Optional)**: `username` (str)\
**Description**: Greets the given user, defaults to "sajeel" if not provided.

**Example Request:**

```
GET /greeting
```

**Response:**

```json
{
  "message": "Hello sajeel "
}
```

---

### `POST /adduser`

**Request Body**:

```json
{
  "username": "new_user",
  "email": "new_user@example.com"
}
```

**Description**: Adds a new user to the in-memory `user_list`.

**Response:**

```json
{
  "message": "New user Added",
  "user": {
    "username": "new_user",
    "email": "new_user@example.com"
  },
  "list": [
    "sajeel",
    "ali",
    "malik",
    {
      "username": "new_user",
      "email": "new_user@example.com"
    }
  ]
}
```

---

## 🧱 Data Models

### `NewUser`

| Field    | Type | Required |
| -------- | ---- | -------- |
| username | str  | ✅ Yes    |
| email    | str  | ✅ Yes    |

---

## ⚠️ Notes

- `user_list` is a mix of strings and dicts after POST — not ideal for production.
- In `/details`, return `raise HTTPException(...)` instead of `return HTTPException(...)`.
- For better consistency, use dictionaries or Pydantic models uniformly in lists.

