#!/usr/bin/python
import sqlite3
import os

dir_path = os.path.dirname(os.path.abspath(__file__))

class PiDatabase:

  def __init__(self, path_to_database):
    self.conn = sqlite3.connect(os.path.join(dir_path, path_to_database))
    self.cur = self.conn.cursor()

  def tableCreate(self, ):
    self.cur.execute("CREATE TABLE images(dateTime TEXT, path_to_image TEXT, latitude TEXT, longitude TEXT, altitude TEXT) ")

  def dataEntry(self, data):
    with self.conn:
      self.cur.execute("INSERT INTO images (dateTime, path_to_image, latitude, longitude, altitude) VALUES( ?, ?, ?, ?, ?)", (data[0], data[1], data[2], data[3], data[4], data[5]))
      self.conn.commit()
      print("Image successfully recorded")