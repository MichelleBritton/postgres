from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sql-alchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")

# base variable which will be set to the declarative_base() class.  This new base class will essentially grab the metadata that is produced by our databased table schema
# and creates a subclass to map everything back to us here within the base variable.  In other words we are piggybacking off an existing ORM class.
base = declarative_base()

# create a class based model for the "Artist" table
# when defining classes it's best practice to use PascalCase
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# create a class based. model for the "album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

# Create a class based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)




# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)

# opens an actual session by calling the Session() subclass defined above
session = Session()

# The last thing we need to do before we can work with our db is to actually create the database subclass and generate all meta data.  The base variable, givven that it's a
# subclass from teh declarative_base, will now use the .create_all() methord from our database metadata.ab
# creting the database using declarative_base subclass
base.metadata.create_all(db)

# Now that we have the file set up, we can start to build our class based models, but this time we get to simply build a normal Python object, that subclasses base
# The class based models need to be added before the session is created above but after the base is declared since we need to use the base subclass.

