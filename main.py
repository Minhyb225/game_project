

from tabulate import tabulate
import mysql.connector
testDB = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='Nu151200',
    autocommit= True
)
"""
#8.1
mycursor = testDB.cursor()
ICAO = input("Type ICAO code: ")
mycursor.execute(f"select name as 'airport name', municipality as 'location' from airport where ident = '{ICAO}';")
reTurn = mycursor.fetchall()
print(tabulate(reTurn, tablefmt="fancy_grid"))
"""
#8.2


areaCode = input("Input the area code (i.e. FI): ")
mycursor = testDB.cursor()
mycursor.execute(f"select country.name as 'country name', airport.name as 'airport name', airport.type as 'airport type' from country, airport where country.iso_country = airport.iso_country and airport.iso_country = '{areaCode}' order by airport.type;")
result = mycursor.fetchall()
print(tabulate(result, tablefmt="fancy_grid"))
print(mycursor.rowcount, 'rows in set')
"""

8.3
from geopy import distance
mycursor = testDB.cursor()
icao_1 = input("Type first ICAO code: ")
mycursor.execute(f"select name from airport where ident = '{icao_1}';")
reTurn = mycursor.fetchall()
print(tabulate(reTurn, tablefmt="fancy_grid"))
icao_2 = input("Type the second ICAO code: ")
mycursor.execute(f"select name from airport where ident = '{icao_2}';")
reTurn = mycursor.fetchall()
print(tabulate(reTurn, tablefmt="fancy_grid"))
mycursor.execute(f"select latitude_deg, longitude_deg from airport where ident = '{icao_1}' or ident = '{icao_2}';")
listDeg = []
for x in mycursor:
    listDeg.append(x)
print(f"The distance between 2 airports is", f"{distance.distance(listDeg[0], listDeg[1]).km:.2f} km")
"""

§122345