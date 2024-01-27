# Overview

This Node.js script is an educational tool designed to demonstrate the differences between running a JavaScript application in a Docker container versus executing it directly on a local system. The script prints "Hello World!" followed by the current working directory (CWD). The output of the CWD is key for illustrating the variance in the script's running environment when executed inside a container versus on the host system.

# Installation and Usage

## Prerequisites

- Node.js installed on your local system.
- Docker installed on your local system (for running the script in a container).

## Getting Ready

Download or clone the repository and navigate to `Docker-JavaScript/Simple` directory.

## Running the Script

### Locally

- Open a terminal.
- Run `node sample.js`.
- Observe the "Hello World!" message and the printed current working directory.

### Using Docker

#### - Build the Docker Image:

- Run `docker build -t tic3001-sample-docker-js-simple .` in the terminal, within the directory containing the Dockerfile.

#### - Run the Script in a Container:

- Execute `docker run tic3001-sample-docker-js-simple`.

Notice the output and how the CWD differs from local execution.

# Understanding the Output

- When run locally, the CWD printed will be the directory from where you execute the script.
- Inside a Docker container, the CWD will reflect the container's internal directory, `/app` as set in the Dockerfile.

# Troubleshooting

- Node.js Not Found: Ensure Node.js is installed on your system.
- Docker Build or Run Issues: Verify that Docker is correctly installed and that you have permissions to run Docker commands.
