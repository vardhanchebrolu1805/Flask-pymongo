## Flask Application for CRUD operations on MongoDB

This application performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using a REST API. The REST API endpoints are accessible via HTTP requests and can be tested using Postman.

## Requirements

Python 3.8+
Flask
PyMongo
Docker

## Setup

1. Create a new Python virtual environment and activate it.
2. Install the Flask and PyMongo libraries using pip:
    pip install Flask PyMongo
3. Install Postman for testing the REST API endpoints.
4. Create a new MongoDB database and collection for the application.

## Implementation

1. Open the `app.py` file in your code editor.
2. Import the necessary libraries: Flask, PyMongo, and jsonify.
3. Create a new Flask application instance.
4. Set the MongoDB URI and database name in the Flask application configuration.
5. Create a new PyMongo client and database instance.
6. Create the necessary routes and functions for the REST API endpoints.
7. Run the Flask application using the `flask run` command.

## Testing

1. Open Postman and create a new HTTP request for each of the REST API endpoints.
2. Send requests to the endpoints to test the CRUD operations on the User resource.
3. Verify that the responses are correct and the database is being updated correctly.

## Running the application with Docker

1. Build the Docker image:
docker build -t flask-app .
2. Run the Docker image:
docker run -p 5000:5000 flask-app

This will run the Docker image and expose port 5000 on the host machine. You can then access the Flask application at http://localhost:5000.

## Author
This application was created by Naga Vardhan Chebrolu.
