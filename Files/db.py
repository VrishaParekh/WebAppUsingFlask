import os
import pymysql
from flask import jsonify

#Retriving database connections from app.yaml
databaseUser = os.environ.get('CLOUD_SQL_USERNAME')
databasePassword = os.environ.get('CLOUD_SQL_PASSWORD')
databaseName = os.environ.get('CLOUD_SQL_DATABASE_NAME')
databaseConnectionName = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


#Connecting to MYSQL Database with the credentials
def start_connection():
    unix_socket= '/cloudsql/{}'.format(databaseConnectionName)
    try:
        
        #if os.environ.get('GAE_ENV')== 'standard':
        connection= pymysql.connect(user=databaseUser, password=databasePassword,
                                 unix_socket=unix_socket, db=databaseName,
                                 cursorclass=pymysql.cursors.DictCursor)
            
    except pymysql.MySQLError as e:
        print(e)
        
    return connection

#Get all the songs from the database
def get_songs():
    connection = start_connection()
    with connection.cursor as cursor:
        query= cursor.execute('SELECT * FROM songs;')
        songs= cursor.fetchall()
        if result>0:
            all_songs= jsonify(songs)
            
        else:
            all_songs= 'No songs in Database'
            
    connection.close()
    return all_songs

#Post a song into the database
def add_songs(song):
    connection = start_connection()
    with connection.cursor as cursor:
        cursor.execute('INSERT INTO songs (title,artist,genre) VALUES (%s,%s,%s)',(songs["title"],songs["artist"],songs["genre"]))
    connection.commit()
    connection.close()
        
        
    