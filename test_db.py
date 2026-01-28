from pyspark.sql import SparkSession

# 1. Initialize Spark
spark = SparkSession.builder \
    .appName("TestConnection") \
    .config("spark.jars", "/opt/spark/jars/mysql-connector-java.jar") \
    .getOrCreate()

# 2. Connection Details (Note the url uses 'db', not 'localhost')
jdbc_url = "jdbc:mysql://db:3306/my_project_db"
properties = {
    "user": "user",
    "password": "password",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# 3. Try to read (This will fail gracefully if table doesn't exist, but proves connection)
try:
    print("Attempting to connect to MySQL...")
    df = spark.read.jdbc(url=jdbc_url, table="test_table", properties=properties)
    print("Connection successful!")
except Exception as e:
    # We expect an error because 'test_table' doesn't exist yet,
    # but if the error mentions "Access denied" or "Communications link failure", then we have a problem.
    print(f"Connection attempted! Error details (this is normal if table is missing): {e}")

spark.stop()