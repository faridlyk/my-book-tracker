# My Book Tracker

A web application that allows you to track the books you are currently reading. 
Inspired by [Kayce Basques](https://kayce.basqu.es/).

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python (FastAPI)  
- **Database**: MongoDB  

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/faridlyk/my-book-tracker.git
   cd my-book-tracker/api
   ```

2. **Set up the virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the environment variables**:

   Create a `.env` file with the following content:
   
   ```env
   ADMIN_USERNAME=admin
   ADMIN_PASSWORD=password
   SECRET_KEY=secreKey
   MONGO_URI="mongoUri"
   MONGO_DB_NAME=name
   MONGO_COLLECTION_NAME=collection
   EXP_TIME_MIN=20
   ```

5. **Update API configuration in JavaScript**:

   Ensure that API endpoints in JavaScript files are correctly pointing to your backend.

6. **Configure the database**:

   Make sure MongoDB is installed and running. Set up the database connection in the `config.py` file.

7. **Run the application**:

   ```bash
   uvicorn main:app --reload
   ```

   The application will be available at `http://localhost:8000`.
 
