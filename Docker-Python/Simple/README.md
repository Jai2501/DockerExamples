# Overview

This simple Python script serves as an educational tool for demonstrating the differences between running a Python script in a Docker container versus executing it directly on a local system. The script outputs "Hello World!" and then prints the current working directory (CWD). The CWD output is particularly useful for highlighting the difference in the script's running environment when inside a container versus on the host system.

# Installation and Usage

## Prerequisites

- Python installed on your local system.
- Docker installed on your local system (to run the script in a container).

## Getting Ready

Download/Clone this Repo and navigate to `Docker-Python/Simple` directory.

## Running the Script

### Locally

- Open a terminal.
- Run `python3 Sample.py`.
- Observe the "Hello World!" message and the printed current working directory.

### Using Docker

#### - Build the Docker Image:

In the terminal, run `docker build -t tic3001-sample-python-simple .` within the directory containing the Dockerfile.

#### - Run the Script in a Container:

- Execute `docker run tic3001-sample-python-simple`.

Notice the output and how the CWD differs from the local execution.

## Understanding the Output

- When run locally, the CWD printed will be the directory from where you run the script.
- Inside a Docker container, the CWD will reflect the container's internal directory, that is `/app` as set in the Dockerfile.

# Troubleshooting

- Python Not Found: Ensure Python is installed on your system.
- Docker Build or Run Issues: Verify that Docker is correctly installed and that you have permissions to run Docker commands.
