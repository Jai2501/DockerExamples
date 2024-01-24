# Importing relevant libraries
import os
from flask import Flask

app = Flask(__name__)

# Defining a route for handling GET requests
@app.route("/")
def hello():
    print("Request received!")

    # Setting the response status and headers
    return "Hello, World! This is a Web Service\n", 200, {"Content-Type": "text/plain"}

# Starting the Flask development server
if __name__ == "__main__":
    # Setting the hostname and port
    hostname = "0.0.0.0"
    port = 3000

    # Printing the current working directory
    print("Current Working Directory:", os.getcwd()) 

    # To run the Flask app
    app.run(host=hostname, port=port)
