# Project Setup

### 1. Setting up Virtual Environment

First, set up a virtual environment to isolate your project dependencies:

```bash
# Create a virtual environment named 'venv'
python -m venv venv
```

### 2. Activating Virtual Environment

Activate the virtual environment based on your operating system:

**For Windows:**
```bash
venv\Scripts\activate
```

**For macOS and Linux:**
```bash
source venv/bin/activate
```

### 3. Installing Dependencies

Install project dependencies from `requirements.txt` using pip:

```bash
pip install -r requirements.txt
```

### 4. Running the Server

Start the Django server to run your API:

```bash
python manage.py runserver
```

# API Documentation

### 1. Uploading CSV Endpoint

This endpoint allows uploading a CSV file that will be used for future data queries.

#### Endpoint:
```
POST /api/upload-csv/
```

#### Request:
- **Method:** POST
- **Parameters:** 
  - `csv_file`: The CSV file to upload.

#### Restrictions:
- The file should be publicly accessible and can be up to 150 MB in size.

#### Notes:
- The uploaded CSV file should maintain the same column names, data types, and format as the sample CSV.

---

### 2. Query Endpoint

This endpoint allows querying data from the uploaded CSV file based on specified parameters.

#### Endpoint:
```
GET /api/query-data/
```

#### Request:
- **Method:** GET
- **Parameters:**
  - `field=value`: Query by any field in the CSV.
  
#### Querying Rules:
- **Numerical Fields:** Exact match (`age=20` matches records where `age` is exactly 20).
- **String Fields:** Substring match (`name=Raj` matches `Raj`, `Rajesh`, `Rajan`, etc.).
- **Date Fields:** Exact match (`date=2023-01-01` matches records where `date` is exactly `2023-01-01`).

#### Bonus Features:
- Aggregate Searches: (Example: `total>100` retrieves records where `total` is greater than 100).
- Range Queries for Dates: (Example: `date>2023-01-01` retrieves records where `date` is after `2023-01-01`).

#### Notes:
- The API design for handling input parameters and values is flexible based on your needs.

### Testing on Postman:

<img width="930" alt="image" src="https://github.com/RabbiaSajjad/django_assignment/assets/58911684/05d6bb49-be2f-4a04-98d4-2e4e1a8e247b">
<img width="930" alt="image" src="https://github.com/RabbiaSajjad/django_assignment/assets/58911684/fd25effd-545a-4964-b25d-7c9f6d104e7c">


---
