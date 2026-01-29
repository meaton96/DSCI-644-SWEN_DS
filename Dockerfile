FROM python:3.12-slim-bookworm

RUN mkdir -p /usr/share/man/man1

# Added git so you can clone the lab invite directly in the container
RUN apt-get update && \
    apt-get install -y openjdk-17-jre-headless curl procps git && \
    apt-get clean;

# Set JAVA_HOME explicitly for PySpark
RUN J_PATH=$(dirname $(dirname $(readlink -f $(which java)))) && \
    echo "export JAVA_HOME=$J_PATH" >> /etc/environment

ENV JAVA_HOME=/usr/lib/jvm/default-java
RUN ln -s /usr/lib/jvm/java-17-openjdk-$(dpkg --print-architecture) /usr/lib/jvm/default-java
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Download the MySQL JDBC Driver
RUN mkdir -p /opt/spark/jars && \
    curl -L -o /opt/spark/jars/mysql-connector-j.jar https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/8.3.0/mysql-connector-j-8.3.0.jar

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["tail", "-f", "/dev/null"]