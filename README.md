# DSCI-644 Mac/Docker Environment Setup

  

This is a containerized version of the class environment (Spark + MySQL). It allows you to run the project without setting up a Linux VM or installing Java locally.

  

## Prerequisites

1.  **Install Docker Desktop:** [Download here](https://www.docker.com/products/docker-desktop/)
2.  **Install "Dev Containers" Extension:** In VS Code, search for and install the "Dev Containers" extension (by Microsoft).

  

## How to Run

1. Fork Repo and clone or clone and copy the *Dockerfile*, *docker-compose.yml* and *requirements.txt* to another folder

2. Open your Terminal and navigate to the folder.

3. Run this command:

```bash

docker compose up -d

```
or use the docker desktop app to spin up the container

4. connect with vs code and run 
```bash
python test_db.py
```
which should print out a successful connection message if everything is working correctly


## Windows

1. Open the Dockerfile and change

```

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64

```

to

```

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

```
2. remove the line:
```
RUN mkdir -p /usr/share/man/man1
```

