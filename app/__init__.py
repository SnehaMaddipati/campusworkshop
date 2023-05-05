"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaarl3hp8u791h18350-a.oregon-postgres.render.com",
        database="todo_sqs5",
        user="sneha",
        password="dpg-chaarl3hp8u791h18350-a.oregon-postgres.render.com")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
