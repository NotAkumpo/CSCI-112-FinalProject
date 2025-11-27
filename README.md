## File structure

- `Backend/` - Flask server with all the routes and business logic
- `Frontend/` - HTML templates and JavaScript for the UI
- `Database/` - Database schema and setup files

## How to run it

1. Make sure MongoDB is running on localhost:27017
2. Install dependencies: `pip install -r requirements.txt`
3. Run the backend: `python Backend/app.py`
4. Open a browser and go to `http://localhost:8000`

## How to populate the MongoDB database in localhost
1. Make sure MongoDB is running on localhost:27017
2. Run the database and schema creation: `python Database/Schema.py`
3. Run the document inserts: `python Database/Inserts.py`
