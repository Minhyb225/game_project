import random

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
#
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
    return distance.distance(listDeg[0], listDeg[1]).km
rand = random.randint(2,4)
rand1 = rand
rand2 = rand
print(f"You have to transit {rand-1} point")
A = "EFHK"
listc1 = []
listc2 = []
if rand1 > 1:
    A = "EFHK"
    for x in range(1, rand1):
        B = input("Player_1:Choose next airport: ")
        listc1.append(Cal(A,B))
        A = B
else:
    listc1.append(Cal(B,"EFIV"))
    mycursor.execute(f"select name from airport where ident = EFIV;")
    reTurn = mycursor.fetchall()
    print(tabulate(reTurn, tablefmt="fancy_grid"))
if rand2 > 1:
    A = "EFHK"
    for x in range(1, rand2):
        B = input("Player_2:Choose next airport: ")
        listc2.append(Cal(A,B))
        A = B
else:
        listc2.append(Cal(B,"EFIV"))
        mycursor.execute(f"select name from airport where ident = EFIV;")
        reTurn = mycursor.fetchall()
        print(tabulate(reTurn, tablefmt="fancy_grid"))
print(f"Player_1 went a total of {sum(listc1):.2f}km to find Snorkmaiden")
print(f"Player_2 went a total of {sum(listc2):.2f}km to find Snorkmaiden")
if sum(listc1) < sum(listc2):
    print("Layer_1 is Moomin\nLayer_2 is the loser" )
elif sum(listc1) > sum(listc2):
    print("Layer_1 is the loser\nLayer_2 is Moomin" )
#