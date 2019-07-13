# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

# Creating songplays table
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
songplay_id SERIAL PRIMARY KEY,
start_time TIMESTAMP REFERENCES time (start_time) NOT NULL,
user_id INTEGER REFERENCES users (user_id) NOT NULL,
level VARCHAR(10) NOT NULL,
song_id VARCHAR(50) REFERENCES songs(song_id),
artist_id VARCHAR(50) REFERENCES artists(artist_id),
session_id INTEGER NOT NULL,
location TEXT NOT NULL,
user_agent TEXT NOT NULL)""")

# Creating users table
user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
user_id INTEGER PRIMARY KEY, 
first_name VARCHAR(50) NOT NULL, 
last_name VARCHAR(50) NOT NULL, 
gender VARCHAR(1) NOT NULL,
level VARCHAR(10) NOT NULL)""")

# Creating songs table
song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
song_id VARCHAR(50) PRIMARY KEY, 
title VARCHAR(100) NOT NULL,
artist_id VARCHAR(50) NOT NULL, 
year INTEGER NOT NULL, 
duration DOUBLE PRECISION NOT NULL)""")

# Creating artists table
artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
artist_id VARCHAR(50) PRIMARY KEY, 
name VARCHAR(100) NOT NULL, 
location TEXT NOT NULL,
latitude DOUBLE PRECISION, 
longitude DOUBLE PRECISION)""")

# Creating time table
time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
start_time TIMESTAMP PRIMARY KEY,
hour INTEGER NOT NULL, 
day INTEGER NOT NULL, 
week INTEGER NOT NULL, 
month INTEGER NOT NULL, 
year INTEGER NOT NULL, 
weekday INTEGER NOT NULL)""")

# INSERT RECORDS

# Inserting into songplays table
songplay_table_insert = ("""INSERT INTO songplays ( 
start_time, 
user_id, 
level, 
song_id,
artist_id,
session_id,
location,
user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""")

# Inserting into users table
user_table_insert = ("""INSERT INTO users (
user_id, 
first_name, 
last_name, 
gender, 
level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET first_name=users.first_name, last_name=users.last_name, gender=users.gender, level=users.level""")

# Inserting into songs table
song_table_insert = ("""INSERT INTO songs (
song_id, 
title, 
artist_id, 
year, 
duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO UPDATE SET title=songs.title, artist_id=songs.artist_id, year=songs.year, duration=songs.duration""")

# Inserting into artists table
artist_table_insert = ("""INSERT INTO artists (
artist_id, 
name, 
location, 
latitude, 
longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO UPDATE SET name=artists.name, location=artists.location, latitude=artists.latitude, longitude=artists.longitude""")

# Inserting into time table
time_table_insert = ("""INSERT INTO time (
start_time, 
hour, 
day, 
week, 
month,
year,
weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO UPDATE SET hour=time.hour, day=time.day, week=time.week, month=time.month, year=time.year, weekday=time.weekday""")

# FIND SONGS
song_select = (""" select songs.song_id, artists.artist_id from songs, artists where 
songs.artist_id = artists.artist_id and 
songs.title = %s and 
artists.name = %s and 
songs.duration = %s
""")

# QUERY LISTS
create_table_queries = [time_table_create, artist_table_create, user_table_create, song_table_create, songplay_table_create]
drop_table_queries = [time_table_drop, artist_table_drop, user_table_drop, song_table_drop, songplay_table_drop]
