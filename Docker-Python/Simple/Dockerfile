# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Define environment variable (if any) in format ENV KEY value
ENV NAME World

# Run app.py when the container launches
CMD ["python3", "Sample.py"]
