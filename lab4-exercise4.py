#!/usr/bin/env python3
import sqlite3
dbconnect = sqlite3.connect("mydatabase.db")
dbconnect.row_factory = sqlite3.Row
cursor = dbconnect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS sensors (sensorID, type, zone)''')
cursor.execute('''INSERT INTO sensors VALUES (1, 'door', 'kitchen')''')
cursor.execute('''INSERT INTO sensors VALUES (2, 'temperature', 'kitchen')''')
cursor.execute('''INSERT INTO sensors VALUES (3, 'door', 'garage')''')
cursor.execute('''INSERT INTO sensors VALUES (4, 'motion', 'garage')''')
cursor.execute('''INSERT INTO sensors VALUES (5, 'temperature', 'garage')''')

print("Sensors in kitchen:")
cursor.execute('''SELECT * FROM sensors WHERE zone="kitchen"''')
for row in cursor:
    print(row['sensorID'], row['type'], row['zone'])

print("Door sensors:")
cursor.execute('''SELECT * FROM sensors WHERE type="door"''')
for row in cursor:
    print(row['sensorID'], row['type'], row['zone'])

dbconnect.close()
