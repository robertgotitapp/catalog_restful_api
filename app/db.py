from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import config

# how to configure multiple database
engine = create_engine(config.SQL_ALCHEMY_DATABASE_URI)
# engine = engine_from_config(config)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def executeScriptsFromFile(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        # This will skip and report validation
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
            db_session.execute(command)
        except:
            print("'{}' skipped".format(command))


def init_db():
    # import all modules here that might define models so that they will be registered
    # properly on the metadata. Otherwise, you will have to import them first before call init_db()
    import app.models
    Base.metadata.create_all(bind=engine)


def clear_db():
    # run the sql script to clear all the data from the database
    executeScriptsFromFile('app/sql/remove_tables.sql')


def create_mock_data():
    # run the sql script to create mock data for testing
    executeScriptsFromFile('app/sql/mock_data.sql')
