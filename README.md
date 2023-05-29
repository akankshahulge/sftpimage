# sftpimage
Clone this repository to your local machine.
git clone https://github.com/your-username/repository-name.git

Create a Dockerfile in the root directory of your project. Paste the Dockerfile contents you provided in your previous message:
Also.. add requirements.txt file: so that it will install dependencies to run docker image 

Update the connection details in the Python script:

SFTP connection details (host, username, password, and file path)
Hive connection details (host, port, username, database, and table name)
Add path of txt file in the sftp for that we have to put it in.

Run the script.
The script will establish an SFTP connection, read the file contents, split the data, create a Hive table, and load the data into the table.

Verify the data in the Hive table.
Build the Docker image.
docker build -t your-image-name .
docker run --network host your-image-name python your-pyhton-script
Verify the data in the Hive table.
