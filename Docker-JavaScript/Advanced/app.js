// Using the http module
const http = require("http");

// Setting the hostname and port for the server to listen on
const hostname = "0.0.0.0";
const port = 3000;

// Creating an HTTP server with a request handler function
const server = http.createServer((req, res) => {
  console.log("Request received!");

  // Setting the HTTP response status code and headers
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");

  // Sending the response body
  res.end(`Hello, World! This is a Web Service\n`);
});

// Start the server and listen on the specified hostname and port
server.listen(port, hostname, () => {
  // To help see the difference when running on container vs on system
  console.log("Current Working Directory:", process.cwd());

  console.log(`Server running at http://${hostname}:${port}/`);
});
