#
#
#
import pytest
import pprint as pp
import logging
LOG = logging.getLogger(__name__)

#
#
#
import os
import sqlite3

#
#
#
@pytest.mark.skip()
class TestDbSqlite:

    @pytest.fixture
    def session(self):
        db_url = os.environ['DATABASE_URL'].replace("sqlite:///","")
        LOG.info( os.environ['DATABASE_URL'] )
        LOG.info(f'db_url {db_url}')

        connection = sqlite3.connect(db_url)
        db_session = connection.cursor()
        yield db_session
        connection.close()


    @pytest.mark.skip()
    @pytest.mark.order(102)
    def test_db_sqlite_step2_info(self):
        db_url = os.environ['DATABASE_URL'].replace("sqlite:///","")
        LOG.info( os.environ['DATABASE_URL'] )
        LOG.info(f'db_url {db_url}')

        connection = sqlite3.connect(db_url) 
        db_session = connection.cursor()
        db_session.execute('select * from user') 
        connection.commit()
        #yield db_session # 5
        connection.close()

    
    @pytest.mark.skip()
    @pytest.mark.order(109)
    def test_db_sqlite_step9_template(self):
        db_url = os.environ['DATABASE_URL'].replace("sqlite:///","")
        LOG.info( os.environ['DATABASE_URL'] )
        LOG.info(f'db_url {db_url}')

        try:
            sqliteConnection = sqlite3.connect(db_url)
            cursor = sqliteConnection.cursor()
            LOG.info("Database created and Successfully Connected to SQLite")

            sqlite_select_Query = "select sqlite_version();"
            cursor.execute(sqlite_select_Query)
            record = cursor.fetchall()
            LOG.info("SQLite Database Version is: ", record)
            cursor.close()

        except sqlite3.Error as error:
            LOG.info("Error while connecting to sqlite", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                LOG.info("The SQLite connection is closed")

    