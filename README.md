# Moomin's traveling
[Link github](https://github.com/Minhyb225/game_project)
----

![image link](https://github.com/Minhyb225/game_project/blob/master/picturemoomin1.png)

----
### Code
```python
from tabulate import tabulate
import mysql.connector
from geopy import distance
my_cursor = testDB.cursor()
cursor_all = testDB.cursor()

list1=["EFHK","EFHA","EFJY","EFJO","EFKU","EFKK","EFKI","EFKS","EFKT","EFKE","EFMA","EFOU","EFPO","EFRO","EFSA","EFTU","EFTP","EFUT","EFVA","EFIV"]
for x in range(0,20):
    cursor_all.execute(f"select name from airport where ident = '{list1[x]}';")
    result = cursor_all.fetchall()
    print(f"{list1[x]}  :  {result}\n-------------------------------")

print("You have to transit in 3 airports.")
#function to query airport
def calculate_distance(icao_1, icao_2):
    my_cursor.execute(f"select name from airport where ident = '{icao_1}';")
    name1 = my_cursor.fetchall()
    name1=tabulate(name1, tablefmt="fancy_grid")
    my_cursor.execute(f"select name from airport where ident = '{icao_2}';")
    name2 = my_cursor.fetchall()
    name2=tabulate(name2, tablefmt="fancy_grid")
    my_cursor.execute(f"select latitude_deg, longitude_deg from airport where ident = '{icao_1}' or ident = '{icao_2}';")
    list_deg = []
    for x in my_cursor:
        list_deg.append(x)
    return name1, name2, distance.distance(list_deg[0], list_deg[1]).km

player1_total_distance = 0
player1_airports = []
player2_total_distance = 0
player2_airports = []
# Player1
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
#player2
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
#Compare-result
print("All the airports you travelled:")
for airport in player2_airports:
    print(airport)

print(f"Player_1 went a total of {player1_total_distance:.2f}km to find Snorkmaiden")
print(f"Player_2 went a total of {player2_total_distance:.2f}km to find Snorkmaiden")
if player1_total_distance < player2_total_distance:
    print("Player 1 is Moomin!\nPlayer 2 lost the game.")
else:
    print("Player 1 lost the game.\nPlayer 2 is Moomin!")
```
----
### Preliminary Requirements
    -Players type ICAO to choose the next airport
    -Airport will be fetched and showed on the screen based on ICAO of country
    -After each choice distance will be added to the “list” and the name will show to the player
    -After third choices all of airports will be displayed
    -Comparing the distance between 2 trips and print the result.
----
### Run
Mac/Linux run
```bash
python3 connect_py.py
```
Windows run
```bash
py -3 connect_py.py
```
Make sure user name is root and password is your database password.
