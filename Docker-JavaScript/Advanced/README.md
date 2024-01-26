# Overview

This code creates a basic HTTP server using Node.js. It is designed to respond to HTTP requests by sending a plain text response "Hello, World! This is a Web Service". This server is intended to be a simple example of how to use Node.js for creating web services, and also demonstrate how Docker can be utilised for creating such services.

# Features

- HTTP Server: Utilizes Node.js's built-in http module to create an HTTP server.

- Basic Response: Sends a simple text response to any HTTP request it receives.

- Host and Port Configuration: The server is configured to listen on all network interfaces (0.0.0.0) at port 3000.

- Working Directory Logging: On server start, it logs the current working directory. This is useful for understanding the server's operating context, especially when running inside containers.

# How to Use

## Prerequisites

Node.js must be installed on your system. You can download it from Node.js official website.

## Start the Server

- Open a terminal or command prompt.
- Navigate to the directory where server.js is located.
- Run the command `node server.js` or follow the [Docker Guide](https://github.com/Jai2501/DockerExamples/blob/main/README.md) to run it using Docker
- You should see a message indicating that the server is running, along with the current working directory.

## Interact with the Server

- Open a web browser or a tool like curl or Postman.
- Navigate to http://0.0.0.0:3000/ or http://localhost:3000/.
- You should receive a response saying "Hello, World! This is a Web Service".

## Stopping the Server

- To stop the server, go back to the terminal where it's running and press Ctrl+C.

# Notes

- The server is configured to listen on 0.0.0.0, which means it will be accessible from any IP address that your machine has.
- Port 3000 is used by default. Ensure that this port is not being used by another service on your system.

# Troubleshooting

- Port Already in Use: If you get an error that the port is already in use, try changing the port number in the server.js file.
- Node.js Not Found: Ensure that Node.js is correctly installed and that your system's PATH environment variable includes the path to the Node.js executable.
