# requests
# atexit
import psycopg2
#
# pip install -r ../requirements.txt

from configparser import ConfigParser


# # function to get info from config file
# params = get_config()
#
# # connecting to config file
# conn = psycopg2.connect(**params)
#
# # the returned value from database
# cur = conn.cursor()
#
# # sends the query to database and returns nothing
# cur.execute('SELECT ...')
#
# # return one row
# db_version1 = cur.fetchone()
#
# # returns all
# db_version2 = cur.fetchall()
#
# # returns given amount
# db_version3 = cur.fetchmany(size=0)
#
# # remember to close connection
# cur.close()
#
# # context manager with cursor
# with conn.cursor() as cur:

from flask import Flask
app = Flask("simple_web_app")









