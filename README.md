# DSCI-644 Mac/Docker Environment Setup

  

This is a containerized version of the class environment (Spark + MySQL). It allows you to run the project without setting up a Linux VM or installing Java locally.

  

## Prerequisites

1.  **Install Docker Desktop:** [Download here](https://www.docker.com/products/docker-desktop/)
2.  **Install "Dev Containers" Extension:** In VS Code, search for and install the "Dev Containers" extension (by Microsoft).
3. **Python 3.12** installed locally.

---

### 🚀 Setup & Execution

#### 1. Launch Containers
Since the Dockerfile is now architecture-agnostic, you no longer need to manually edit paths for Windows or Mac. Simply run:
```powershell
docker-compose up -d --build