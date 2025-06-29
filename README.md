# Agentic AI Order Assistant (Backend)

A simple Flask API that takes natural language input (e.g., "Order shampoo") and returns product links from a predefined database.

## Features
- Natural language matching
- JSON product memory
- Easily extendable with AI or product APIs

## Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/agentic-ai-backend.git
cd agentic-ai-backend
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Server
```bash
python app.py
```

### 5. Test the API
Send a POST request to `http://localhost:5000/query` with a JSON body:
```json
{
  "message": "Order chai"
}
```

## Notes
- Modify `product_db.json` to include more products or categories.