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
"""
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

print("You have to transit in 3 airports")
listc1 = []
listc2 = []
#1
A = "EFHK"
for x in range(1, 4):
    B = input("Player_1:Choose next airport: ")
    listc1.append(Cal(A,B))
    A = B
listc1.append(Cal(B,"EFIV"))
mycursor.execute(f"select name from airport where ident = 'EFIV';")
reTurn = mycursor.fetchall()

#2
A = "EFHK"
for x in range(1, 4):
    B = input("Player_2:Choose next airport: ")
    listc2.append(Cal(A,B))
    A = B
listc2.append(Cal(B,"EFIV"))
mycursor.execute(f"select name from airport where ident = 'EFIV';")
reTurn = mycursor.fetchall()

print(f"Player_1 went a total of {sum(listc1):.2f}km to find Snorkmaiden")
print(f"Player_2 went a total of {sum(listc2):.2f}km to find Snorkmaiden")
if sum(listc1) < sum(listc2):
    print("Layer_1 is Moomin\nLayer_2 is the loser" )
elif sum(listc1) > sum(listc2):
    print("Layer_1 is the loser\nLayer_2 is Moomin" )
"""
def calculate_distance(icao_1, icao_2):
    my_cursor.execute(f"select name from airport where ident = '{icao_1}';")
    name1 = my_cursor.fetchall()
    name1 = tabulate(name1, tablefmt="fancy_grid")
    my_cursor.execute(f"select name from airport where ident = '{icao_2}';")
    name2 = my_cursor.fetchall()
    name2 = tabulate(name2, tablefmt="fancy_grid")
    my_cursor.execute(
        f"select latitude_deg, longitude_deg from airport where ident = '{icao_1}' or ident = '{icao_2}';")
    list_deg = []
    for x in my_cursor:
        list_deg.append(x)
    return name1, name2, distance.distance(list_deg[0], list_deg[1]).km


print("You have to transit in 3 airports.")
player1_total_distance = 0
player1_airports = []
player2_total_distance = 0
player2_airports = []
# 1
A = "EFHK"
for x in range(0, 3):
    B = input("Hi, Player 1! Choose airport to transfer. Please type in ICAO of the airport: ")
    result = calculate_distance(A, B)
    player1_airports.append(result[0])
    player1_total_distance += result[2]
    print(f"You travelled from\n{result[0]} \nto\n{result[1]}")
    A = B

result = calculate_distance(B, "EFIV")
player1_airports.append(result[0])
player1_airports.append(result[1])
player1_total_distance += result[2]
print("All the airports you travelled:")
for airport in player1_airports:
    print(airport)

# 2
A = "EFHK"
for x in range(0, 3):
    B = input("Player 2:Choose next airport: ")
    result = calculate_distance(A, B)
    player2_airports.append(result[0])
    player2_total_distance += result[2]
    print(f"You travelled from\n{result[0]} \nto\n{result[1]}")
    A = B

result = calculate_distance(B, "EFIV")
player2_airports.append(result[0])
player2_airports.append(result[1])
player2_total_distance += result[2]

print("All the airports you travelled:")
for airport in player2_airports:
    print(airport)

print(f"Player_1 went a total of {player1_total_distance:.2f}km to find Snorkmaiden")
print(f"Player_2 went a total of {player2_total_distance:.2f}km to find Snorkmaiden")
if player1_total_distance < player2_total_distance:
    print("Player 1 is Moomin!\nPlayer 2 lost the game.")
else:
    print("Player 1 lost the game.\nPlayer 2 is Moomin!")