#!/usr/bin/env python

import pandas as pd
import pymysql
import sqlalchemy as db
import mysql.connector

#read csv's and add to database
engine = db.create_engine("mysql+pymysql://codetest:swordfish@database/codetest")
df = pd.read_csv('data/people.csv',index_col=0)
df2 = pd.read_csv('data/places.csv',index_col=0)
df.to_sql('people',con=engine,if_exists='append')
df2.to_sql('places',con=engine,if_exists='append')

#input city id into people table
mydb = mysql.connector.connect(
  host='database',
  user='codetest',
  password='swordfish',
  database='codetest'
)
mycursor = mydb.cursor()
update_fk_sql = 'UPDATE people INNER JOIN places ON people.place_of_birth = places.city SET people.city_id = places.id WHERE people.city_id IS NULL'
mycursor.execute(update_fk_sql)
mydb.commit()

#output requested data to json
task_sql = 'SELECT places.country, COUNT(places.country) FROM people INNER JOIN places ON places.id = people.city_id GROUP BY country'
df3 = pd.read_sql(task_sql,engine,index_col=None)
df3.to_json('data/summary_output.json',orient='values')
