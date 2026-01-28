# Use a lightweight Python image
FROM python:3.12-slim-bookworm
RUN mkdir -p /usr/share/man/man1
# Install OpenJDK 17 (Required for Spark) and curl
RUN apt-get update && \
    apt-get install -y openjdk-17-jre-headless curl && \
    apt-get clean;

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64
# Download the MySQL JDBC Driver
# We place it in a standard location so we can reference it easily
RUN mkdir -p /opt/spark/jars && \
    curl -o /opt/spark/jars/mysql-connector-java.jar https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.30/mysql-connector-java-8.0.30.jar

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Keep the container running so you can execute scripts manually
CMD ["tail", "-f", "/dev/null"]