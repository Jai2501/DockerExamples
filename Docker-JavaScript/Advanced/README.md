# Overview

This JavaScript code creates a basic HTTP server using Node.js. It's designed to demonstrate the usage of Docker for deploying Node.js applications. The server responds to HTTP requests with a plain text message and logs the current working directory (CWD), which is particularly useful for illustrating differences when running the application inside a Docker container versus directly on the host system.

# Features

- Node.js HTTP Server: Leverages the Node.js http module to create an HTTP server.
- Simple Text Response: Sends "Hello, World! This is a Web Service" in response to HTTP requests.
- Environment Logging: Prints the current working directory, useful for distinguishing between running in a container and on the host system.

# Installation and Usage

## Prerequisites

- Node.js installed on your system.
- Docker installed if running inside a container.

## Getting Ready

Download/Clone this Repo and Naviagte to `Docker-JavaScript/Advanced` folder

## Starting the Server

### On Local System (Regular Way)

- Open a terminal.
- Navigate to the directory containing server.js.
- Run `node app.js`.
- A message indicating the server is running and the CWD will be displayed.

### Using Docker

- Run `docker build -t tic3001-sample-docker-js-adv .` in the directory with the Dockerfile to build an image.
- Execute `docker run -p 3000:3000 tic3001-sample-docker-js-adv`
- This starts the Node.js server inside a Docker container.

## Access the Server:

- Open a web browser or use a tool like curl or Postman.
- Navigate to `http://localhost:3000/`.

## Stopping the Server

- If directly running: Press Ctrl+C in the terminal.
- If using Docker container: Use `docker stop [CONTAINER_ID]`.

# Notes

- When running in Docker, the CWD printed will reflect the container's internal directory set in the Dockerfile (that is `/app`).

# Troubleshooting

- Port Already in Use: Change the port number in both the script and Dockerfile if required.
- Docker Issues: Ensure Docker is properly installed and running on your system
