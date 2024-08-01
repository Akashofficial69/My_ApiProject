# My_ApiProject

## Overview

My_ApiProject is a public transit service RESTful API web application built using Python 3.9+. This API provides
endpoints to retrieve upcoming public transit schedules from an origin station to a destination station based on the
provided parameters. The project is containerized using Docker and includes optional features such as API documentation,
unit testing, and geocoding integration.

## Project Structure

The project structure includes:

- `app/`: Contains the application code.
- `tests/`: Contains unit tests for the application.
- `Dockerfile`: Dockerfile for building the Docker image.
- `docker-compose.yml`: Docker Compose configuration for managing multi-container applications.
- `requirements.txt`: List of Python dependencies.
- `README.md`: This documentation file.

## Installation

### Prerequisites

- Python 3.9+
- Docker (for containerization)
- Docker Compose (for managing multi-container Docker applications)

### Clone the Repository

1. Open a terminal or command prompt.
2. Run the following command to clone the repository:

   ```sh
   git clone https://github.com/yourusername/My_ApiProject.git

### Navigate into the project directory:

- cd My_ApiProject
- Set Up the Environment

#### 1. Create and activate a virtual environment:

- python -m venv venv
- source venv/bin/activate # On Windows use `venv\Scripts\activate`

#### Install dependencies:

    pip install -r requirements.txt

## Docker Setup

1. Ensure Docker is installed and running.

2. Build the Docker image using Docker Compose:
   ```sh 
     docker-compose build

3. Start the application using Docker Compose:
   ```sh
    docker-compose up

The application will be available at http://localhost:5000/api/schedules.

### Running the Application Without Docker

1. Ensure your virtual environment is activated.

2. Run the application:
    ```sh
   python main.py

- The application will be available at http://localhost:5000/api/schedules.

### Running Tests

1. Run tests using pytest:
   ```sh
     pytest

2. Run tests in Docker:
   ```sh
    docker run --rm -v $(pwd):/app -w /app python:3.9-slim bash -c "pip install -r requirements.tx

