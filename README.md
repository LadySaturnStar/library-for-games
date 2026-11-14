# Library for a games list

A small project to track and manage my games list.

## Setup

1. Create a virtual environment:

   ```
   python3 -m venv .venv
   ```

2. Activate the virtual environment (macOS):

   ```
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run the Flask app:

   ```
   export FLASK_APP=game_library
   export FLASK_ENV=development
   flask run
   ```

## Environment variables

There is a file called `.env.example` in the project and there are 2 variables: `DATABASE_URL` and `JWT_SECRET_KEY`.  
You can make a copy of it named `.env` and change values in `.env` to real ones.

## Migrations

This project will use database migrations later.  
Right now there are no models or migrations yet, so you don’t need to run any migration commands.