import os
from pyspark.sql import SparkSession

# Path to the driver inside the container
jar_path = "/opt/spark/jars/mysql-connector-java.jar"

print("\n" + "="*40)
print("🔍 Testing MySQL Connection...")
print("="*40)

# 1. Physical Check
if not os.path.exists(jar_path):
    print(f"❌ ERROR: JAR file missing at {jar_path}")
    print("Check your Dockerfile 'curl' command and ensure you used the -L flag.")
    exit(1)

# 2. Initialize Spark
# We use both spark.jars and extraClassPath to ensure the JVM sees the driver
spark = SparkSession.builder \
    .appName("TestConnection") \
    .config("spark.jars", jar_path) \
    .config("spark.driver.extraClassPath", jar_path) \
    .getOrCreate()

jdbc_url = "jdbc:mysql://db:3306/my_project_db"
jdbc_driver = "com.mysql.cj.jdbc.Driver"

try:
    # Get the JVM gateway and manually register the driver
    jvm = spark._jvm
    jvm.java.lang.Class.forName(jdbc_driver)
    
    # Attempt the connection
    conn = jvm.java.sql.DriverManager.getConnection(jdbc_url, "user", "password")
    
    if not conn.isClosed():
        print("✅ SUCCESS: Spark can communicate with the MySQL container!")
        conn.close()

except Exception as e:
    print(f"❌ CONNECTION FAILED: {e}")
finally:
    spark.stop()