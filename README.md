# Intro into Docker via Examples

Ensure that you have Docker installed and running

## Navigate into the directory you wish to try

For the Simple JavaScript Example

```
cd Docker-JavaScript/Simple
```

For the Advanced JavaScript Example

```
cd Docker-JavaScript/Advanced
```

For the Python Example

```
cd Docker-Python
```

## Building a Docker Image

Command Format:

```
docker build -t "image-name" "."
```

> `.` specifies the directory to look in for the Dockerfile and build. Here `.` represents to look into the current directory for the Dockerfile

### Flags

> `-t` is to specify a tag for the image

Example: To build the Python Example

```
docker build -t tic3001-sample-python .
```

## Running a Docker Container

Command Format:

```
docker run -p PORT:PORT -d "image-name"
```

### Flags

> `-p` is to map port number from Container to PC

> `-d` is to run in detached mode

Example: To run the Python Example

```
docker run -p 3000:3000 -d tic3001-sample-python
```

## Stopping a Docker Container

Use the command `docker ps` to obtain the container ID.

Run `docker stop "container_id"` to stop the container.

Example: To stop the Python Example

```
docker stop 1a2b3c4d5e6f
```

> The container ID is unique and the above is just a dummy container ID
