## File structure

- `Backend/` - Flask server with all the routes and business logic
- `Frontend/` - HTML templates and JavaScript for the UI
- `Database/` - Database schema and setup files

## Importing Files to AWS Server
This project was made with the use of Amazon's AWS Environment. Make sure you've imported the files to your AWS Environment. If you haven't:
1. Open up the console to your application server.
2. Input `git clone https://github.com/NotAkumpo/CSCI-112-FinalProject/` to the AWS console.
3. Ensure that you `cd` into the folder -- in this case, `cd CSCI-112-FinalProject`. You can double check by inputting `ls`.

## Running the GAME STORE Browser using Amazon AWS.
1. Make sure MongoDB is running on localhost:27017.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the backend: `python Backend/app.py`
4. Open a browser and go to `http://localhost:8000`

## Populating the MongoDB database in localhost.
1. Make sure MongoDB is running on localhost:27017.
2. Run the database and schema creation: `python Database/Schema.py`
3. Run the document inserts: `python Database/Inserts.py`
