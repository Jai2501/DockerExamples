# Overview

This Python script is a basic Flask web service designed to demonstrate the use of Docker in web application deployment. The service handles HTTP GET requests and responds with the message "Hello, World! This is a Web Service". The inclusion of the current working directory (CWD) print statement is particularly useful for illustrating the difference in the environment when running the service inside a Docker container versus directly on the host system.

# Features

- Flask Framework: Employs Flask to create a simple web server.
- GET Request Handling: Configured to respond to GET requests at the root URL (/).
- Plain Text Response: Returns a "Hello, World! This is a Web Service" message.
- Environment Display: Prints the current working directory, highlighting the running environment (useful in Docker containers).

# Installation and Usage

## Prerequisites

- Python and Flask should be installed on your system.
- Docker installed (to run the service in a container).

## Running the Service

Download/Clone the Repository and Navigate into `Docker-Python/Advanced` directory

## Start the Service

- Open a terminal.
- Navigate to the directory containing Sample0.py.
- Execute `python3 Sample.py`
- The server will start, and the CWD will be displayed.

## Access the Service

- Use a browser or a tool like curl or Postman to visit http://localhost:3000/.

## Using Docker

Follow the [Docker Guide](https://github.com/Jai2501/DockerExamples/blob/main/README.md) to run using Docker

## Stopping the Service

- Directly running: Press Ctrl+C in the terminal.
- Docker container: Use docker stop [CONTAINER_ID].

# Notes

- When running in Docker, the printed CWD will show the container's internal directory, typically /app as set in the Dockerfile.

# Troubleshooting

- Port Conflicts: Ensure port 3000 is free or change the port in both the script and Dockerfile.
- Docker Issues: Verify Docker is correctly installed and running on your system.
