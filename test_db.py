import os
from pyspark.sql import SparkSession

# Path to the MySQL driver inside the container (Ensure this matches your Dockerfile filename)
mysql_jar_path = "/opt/spark/jars/mysql-connector-j.jar"

# Maven coordinate for the MongoDB Spark Connector
# This will be downloaded automatically by Spark when the session starts
mongo_connector_package = "org.mongodb.spark:mongo-spark-connector_2.12:10.4.0"

print("\n" + "="*50)
print("Initializing Multi-DB Connection Test...")
print("="*50)

# 1. Physical Check for MySQL JAR
if not os.path.exists(mysql_jar_path):
    print(f"ERROR: MySQL JAR file missing at {mysql_jar_path}")
    exit(1)

# 2. Initialize Spark with both MySQL JAR and Mongo Maven Package
spark = SparkSession.builder \
    .appName("MultiDBTest") \
    .config("spark.jars", mysql_jar_path) \
    .config("spark.driver.extraClassPath", mysql_jar_path) \
    .config("spark.jars.packages", mongo_connector_package) \
    .config("spark.mongodb.read.connection.uri", "mongodb://mongodb:27017/test_db.test_collection") \
    .config("spark.mongodb.write.connection.uri", "mongodb://mongodb:27017/test_db.test_collection") \
    .getOrCreate()

# --- TEST MYSQL ---
print("\n🔍 Testing MySQL (JDBC)...")
jdbc_url = "jdbc:mysql://db:3306/project1_db"
jdbc_driver = "com.mysql.cj.jdbc.Driver"

try:
    # Use the JVM gateway to check the driver
    jvm = spark._jvm
    jvm.java.lang.Class.forName(jdbc_driver)
    conn = jvm.java.sql.DriverManager.getConnection(jdbc_url, "root", "rootpassword")
    
    if not conn.isClosed():
        print("✅ SUCCESS: Spark connected to MySQL!")
        conn.close()
except Exception as e:
    print(f"❌ MYSQL FAILED: {e}")

# --- TEST MONGODB ---
print("\n🔍 Testing MongoDB...")
try:
    # We test Mongo by attempting to create a small DataFrame and writing it
    test_df = spark.createDataFrame([("test_data", 1)], ["name", "id"])
    test_df.write.format("mongodb").mode("overwrite").save()
    
    # Read it back to verify
    read_df = spark.read.format("mongodb").load()
    if read_df.count() > 0:
        print("✅ SUCCESS: Spark connected to MongoDB and wrote/read data!")
except Exception as e:
    print(f"❌ MONGODB FAILED: {e}")
    print("Tip: Make sure the 'mongodb' service is running in docker-compose.")

print("\n" + "="*50)
spark.stop()