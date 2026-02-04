

# DSCI-644 Docker Environment Setup

  

  

This is a containerized version of the class environment (Spark + MySQL). It allows you to run the project without setting up a Linux VM or installing Java locally.
#### Installs:
1. `mysql:8.0`
2. `pyspark:3.5.0`
3. `java:17`
4. `JDBC Driver:8.0.33`
5. `mongo:latest`
  

  

## Prerequisites

  

1.  **Install Docker Desktop:** [Download here](https://www.docker.com/products/docker-desktop/)

2.  **Install "Dev Containers" Extension:** In VS Code, search for and install the "Dev Containers" extension (by Microsoft).

3.  **Python 3.12** installed locally.

  

---

  

### Setup & Execution
#### 1. Download the latest release (zip) here: https://github.com/meaton96/DSCI-644-SWEN_DS/releases
Extract to your git repo, or to an empty folder.

  

#### 2. Launch Containers

 Navigate to that folder and run:

```powershell
docker-compose up --build
```

#### 3. Connect via VS Code 

To actually develop inside the Spark environment:

1.  Open the project folder in **VS Code**.
    
2.  Click the **>< Remote Icon** (bottom-left corner) or press `F1` and type `Dev Containers: Attach to Running Container...`.
    
3.  Select the **`_spark`** container.
    
4.  Once the new window opens, go to **File > Open Folder** and select `/app/`.


#### 4. Verify connection
```bash
python test_db.py
```
#### Expected Output:
🔍 Testing MySQL (JDBC)...
✅ SUCCESS: Spark connected to MySQL!

🔍 Testing MongoDB...
✅ SUCCESS: Spark connected to MongoDB and wrote/read data!

#### 5. You can now clone any project repo/files into your container 

###  IMPORTANT
- When setting up the .env file, or attempting to access the database, the server is not running on localhost

 Replace references to [**localhost**] with the name of the spark container ie. [**dsci644_mysql**] or [**dsci644_mongo**]

- You no longer need a python virtual environment. The global environment of the container serves this purpose. (Install pip packages globally)

- To change the database user information, update the **docker-compose.yaml**

- If you want/need to access the databases via command line use:
`docker exec -it dsci644_mysql mysql -u [USER] -p` for mysql or
`docker exec -it dsci644_mongo mongosh` for mongodb cli

