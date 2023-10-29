from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
# The three /// signifies that our database is hosted locally within our workspace environment
db = create_engine("postgresql:///chinook")

# The metadata class will contain a collection of our table objects and the associated data within those objects
# Essentially it's recursive data about data meaning the data about our tables and teh data about the data in those tables
meta = MetaData(db)

# create variable for Artist table. Our first table class, or model, will be for the Artist table which we will assign to the variable of "artist_table"
# Using the Table import, we need to specify the name of our table and provide the meta schema
artist_table = Table(
    "Artist", meta, 
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumID")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making the connection. This saves our connection to the database into a variable called connection
with db.connect() as connection:

    # Query 1 - select all records from the "Artist" table
    #select_query = artist_table.select()

    # Query 2 - select only the "Name" column from the "Artist" table
    #select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - select only "Queen" from the "Artist" table
    #select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - select only by "ArtistId" #51 from the "Artist" table
    #select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select only the albums with "ArtistId" #51 from the "Album" table
    #select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - Select all tracks where the composer is "Queen" from the track table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results: 
        print(result)