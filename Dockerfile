# Use a lightweight Python image
FROM python:3.12-slim-bookworm

# Fix for Debian-based images where man page directories might be missing
RUN mkdir -p /usr/share/man/man1

# Install OpenJDK 17 and curl
RUN apt-get update && \
    apt-get install -y openjdk-17-jre-headless curl procps && \
    apt-get clean;

# Use dirname to dynamically find where Java is installed
RUN export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which java))))

# Or, use the Debian-specific stable link (Recommended for Debian/Ubuntu)
ENV JAVA_HOME=/usr/lib/jvm/default-java
RUN ln -s /usr/lib/jvm/java-17-openjdk-$(dpkg --print-architecture) /usr/lib/jvm/default-java

# Download the MySQL JDBC Driver
RUN mkdir -p /opt/spark/jars && \
    curl -L -o /opt/spark/jars/mysql-connector-java.jar https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/8.0.33/mysql-connector-j-8.0.33.jar

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["tail", "-f", "/dev/null"]