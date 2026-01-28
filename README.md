# DSCI-644 Mac/Docker Environment Setup

This is a containerized version of the class environment (Spark + MySQL). It allows you to run the project without setting up a Linux VM or installing Java locally.

## Prerequisites
1. **Install Docker Desktop:** [Download here](https://www.docker.com/products/docker-desktop/)
2. **Install VS Code:** [Download here](https://code.visualstudio.com/)
3. **Install "Dev Containers" Extension:** In VS Code, search for and install the "Dev Containers" extension (by Microsoft).

## How to Run
1. Fork Repo and clone or clone and copy the Dockerfile, docker-compose.yml and requirements.txt to another folder
2. Open your Terminal and navigate to this folder.
3. Run this command:
   ```bash
   docker compose up -d
    ```
## Windows
1. Open the Dockerfile and change
```
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64
```
to
```
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
```
