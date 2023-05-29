# import pysftp
# import gzip
# from pyspark.sql import SparkSession

# spark = SparkSession.builder.getOrCreate()

# # SFTP connection details
# sftp_host = 'localhost'
# sftp_username = 'sftp'
# sftp_password = 'iauro100'
# sftp_path = "/sftp/uploads/CDR_PSA_20230405.txt.gz"

# # Establish the SFTP connection
# with pysftp.Connection(host=sftp_host, username=sftp_username, password=sftp_password) as sftp:
#     print("SFTP connection established successfully.")

#     try:
#         # Open the remote file for reading in binary mode
#         with sftp.open(sftp_path, 'rb') as remote_file:
#             # Decompress the gzip file
#             gzip_file = gzip.GzipFile(fileobj=remote_file)
#             file_contents = gzip_file.read()
#             file_contents = file_contents.decode('utf-8')
#             rows = file_contents.split("\n")
#             delimiter = ";"
#             data = [row.split(delimiter) for row in rows]
#             column_names = [f"Column {i+1}" for i in range(len(data[0]))]
#             df = spark.createDataFrame(data).toDF(*column_names)

#             # Show the DataFrame
#             df.show(2)
#     except Exception as e:
#         print("Error reading remote file:", str(e))

import pysftp
from pyhive import hive

# SFTP connection details
sftp_host = 'localhost'
sftp_username = 'sftp'
sftp_password = 'iauro100'
sftp_path = "/sftp/uploads/sample_cdr.txt"

# Hive table details
hive_host = 'localhost'
hive_port = 10000
hive_username = 'hive'
# hive_password = 'your_hive_password'
hive_database = 'testdb'
hive_table = 'new'

# Establish the SFTP connection
with pysftp.Connection(host=sftp_host, username=sftp_username, password=sftp_password) as sftp:
    print("SFTP connection established successfully.")

    try:
        with sftp.open(sftp_path, 'rb') as remote_file:
            file_contents = remote_file.read()
            file_contents = file_contents.decode()
            rows = file_contents.split("\n")
            delimiter = ";"
            data = [row.split(delimiter) for row in rows]
            column_names = [
                f"column_{i+1} STRING" for i in range(len(data[0]))]

            # Connect to Hive
            hive_conn = hive.Connection(host=hive_host, port=hive_port, username=hive_username,
                                        database=hive_database)
            cursor = hive_conn.cursor()
            print("connected ")
            # Create the Hive table
            cursor.execute(f"USE {hive_database}")
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {hive_table} ("
                           f"{', '.join(column_names)}"
                           ") STORED AS ORC")

            # Load data into Hive table
            for row in data:
                values = [f"'{value}'" for value in row]
                query = f"INSERT INTO {hive_table} VALUES ({', '.join(values)})"
                cursor.execute(query)

            print("Data loaded into Hive table successfully.")
    except Exception as e:
        print("Error reading remote file:", str(e))
