# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
# create songplay table
songplay_table_create = (
    "CREATE TABLE IF NOT EXISTS songplays ( \
    songplay_id SERIAL PRIMARY KEY, \
    start_time TIMESTAMP NOT NULL, \
    user_id INT NOT NULL, \
    level VARCHAR, \
    song_id VARCHAR, \
    artist_id VARCHAR, \
    session_id INT, \
    location VARCHAR, \
    user_agent VARCHAR)"
)

# create users table
user_table_create = (
    "CREATE TABLE IF NOT EXISTS users ( \
    user_id INT PRIMARY KEY, \
    first_name VARCHAR, \
    last_name VARCHAR, \
    gender CHAR(1), \
    level VARCHAR)"
)

# create songs table
song_table_create = (
    "CREATE TABLE IF NOT EXISTS songs ( \
    song_id VARCHAR PRIMARY KEY, \
    title VARCHAR NOT NULL, \
    artist_id VARCHAR NOT NULL, \
    year INT, \
    duration FLOAT NOT NULL)"
)

# create artists table
artist_table_create = (
    "CREATE TABLE IF NOT EXISTS artists ( \
    artist_id VARCHAR PRIMARY KEY, \
    name VARCHAR NOT NULL, \
    location VARCHAR, \
    latitude DOUBLE PRECISION, \
    longitude DOUBLE PRECISION)"
)

# create time table
time_table_create = (
    "CREATE TABLE IF NOT EXISTS time ( \
    start_time TIMESTAMP PRIMARY KEY, \
    hour INT, \
    day INT, \
    week INT, \
    month INT, \
    year INT, \
    weekday INT)"
)

# INSERT RECORDS
# insert into songplay table
songplay_table_insert = (
    "INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) \
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s) \
    ON CONFLICT DO NOTHING"
)

# insert into users table
user_table_insert = (
    "INSERT INTO users (user_id, first_name, last_name, gender, level) \
    VALUES(%s, %s, %s, %s, %s) \
    ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level"
)

# insert into songs table
song_table_insert = (
    "INSERT INTO songs (song_id, title, artist_id, year, duration) \
    VALUES(%s, %s, %s, %s, %s) \
    ON CONFLICT (song_id) DO NOTHING"
)

# insert into artists table
artist_table_insert = (
    "INSERT INTO artists (artist_id, name, location, latitude, longitude) \
    VALUES(%s, %s, %s, %s, %s) \
    ON CONFLICT (artist_id) DO NOTHING"
)

# insert into time table
time_table_insert = (
    "INSERT INTO time (start_time, hour, day, week, month, year, weekday) \
    VALUES(%s, %s, %s, %s, %s, %s, %s) \
    ON CONFLICT (start_time) DO NOTHING"
)

# FIND SONGS
# Select songs with song id and artist id and join tables
song_select = (
    "SELECT s.song_id as song_id, a.artist_id as artist_id FROM songs s \
    INNER JOIN artists a \
    ON  s.artist_id = a.artist_id \
    WHERE s.title = %s AND a.name = %s AND s.duration = %s"
)

# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
