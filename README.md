
# DSCI-644 Docker Environment Setup

  

  

This is a containerized version of the class environment (Spark + MySQL). It allows you to run the project without setting up a Linux VM or installing Java locally.
#### Installs:
1. `mysql:8.0`
2. `pyspark:3.5.0`
3. `java:17`
4. `JDBC Driver:8.0.33`
  

  

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
docker-compose up -d
```

#### 3. Connect to container in VS Code
connect to `_spark` container 
navigate to the `/app/` folder

#### 4. Init the python environment

```bash
# Create the environment
python -m venv .venv

# select it (unix command from inside container is same on windows and mac)
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

#### 5. Verify connection
```bash
python test_db.py
```
#### Expected Output:
``✅ SUCCESS: Spark can communicate with the MySQL container!``
