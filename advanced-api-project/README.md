# Django REST Framework API

This API manages books and authors using Django REST Framework.

## Endpoints
| Method | URL | Description | Permissions |
|--------|-----|-------------|-------------|
| GET | `/api/books/` | List all books | Public |
| GET | `/api/books/<id>/` | Retrieve a book | Public |
| POST | `/api/books/create/` | Add a new book | Authenticated users |
| PUT | `/api/books/<id>/update/` | Update a book | Authenticated users |
| DELETE | `/api/books/<id>/delete/` | Delete a book | Authenticated users |

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Alx_DjangoLearnLab.git

