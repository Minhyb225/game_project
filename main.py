

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
from geopy import distance
mycursor = testDB.cursor()
"""



areaCode = input("Input the area code (i.e. FI): ")
mycursor = testDB.cursor()
mycursor.execute(f"select country.name as 'country name', airport.name as 'airport name', airport.type as 'airport type', airport.ident from country, airport where country.iso_country = airport.iso_country and airport.iso_country = '{areaCode}' and airport.type = 'm_airport'  order by airport.type;")
result = mycursor.fetchall()
print(tabulate(result, tablefmt="fancy_grid"))
print(mycursor.rowcount, 'rows in set')
"""


#
CO2_consume = 18
def Cal(icao_1,icao_2):
    mycursor.execute(f"select name from airport where ident = '{icao_1}';")
    reTurn = mycursor.fetchall()
    print(tabulate(reTurn, tablefmt="fancy_grid"))
    mycursor.execute(f"select name from airport where ident = '{icao_2}';")
    reTurn = mycursor.fetchall()
    print(tabulate(reTurn, tablefmt="fancy_grid"))
    mycursor.execute(f"select latitude_deg, longitude_deg from airport where ident = '{icao_1}' or ident = '{icao_2}';")
    listDeg = []
    for x in mycursor:
        listDeg.append(x)
    return distance.distance(listDeg[0], listDeg[1])
A = "EFHK"
B = input("Choose next airport: ")
while B != "ivalo":
    xx = Cal(A,B)
    CO2_consume = CO2_consume - (xx.km * 0.1)
    if CO2_consume > 0:
        print(f"{xx.km:.2f}")
        print(f"You released {xx.km*0.1:.2f}kg CO2 after the flight")
        print(f"The remaining {CO2_consume:.2f}kg of CO2 is allowed to consume")
        A = B
    elif CO2_consume < 0:
        print(f"You need {CO2_consume * -1:.2f}kg CO2 to go {B}")
    B = input("Choose next airport: ")
#