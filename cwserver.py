import socket
from platform import python_version
import sqlite3 as sql
import mysql.connector as mysql

HOST = '127.0.0.1'
PORT = 65430
# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind
server_socket.bind((HOST, PORT))
# Listen
server_socket.listen()
print('Waiting for connection')

socket_client, (host, port) = server_socket.accept()
print(f'Received connection from {host} ({port})\n')
print(f'Connection Established., Connected from: {host}')

# all shop keepers in the shop, passwords and username
shopkeepers = []
password = []

mydb = mysql.connect(host='localhost', user='root', password='root', database='CST1510cw')
print(mydb)

cursor = mydb.cursor()
cursor.execute("DROP TABLE ShopAssistant")
cursor.execute("DROP TABLE Client")


cursor.execute("CREATE DATABASE IF NOT EXISTS CST1510cw")

# creating ShopAssistant Table:
cursor.execute \
    ("CREATE TABLE IF NOT EXISTS ShopAssistant (shopkeeper_id VARCHAR(200), password VARCHAR(200), name VARCHAR(200), surname VARCHAR(200), date_workday VARCHAR(50), sold_item VARCHAR(200), item_price FLOAT(50,2), commission_amount FLOAT(50,2))")
cursor.execute("CREATE TABLE IF NOT EXISTS Client (cname VARCHAR(200), position VARCHAR(200), status VARCHAR(200), shopkeeper_name VARCHAR(200))")

def getdate():
    mess = socket_client.send("a").encode()
    date = socket_client.receive(1024).decode()
    return date

sql = "INSERT INTO ShopAssistant (shopkeeper_id, password, name, surname) VALUES (%s,%s,%s,%s)"
assistant1 = ("DO450", "unicorn123", "Dooshina", "Oolun")
assistant2= ("MW1204", "chocolate50", "Megan", "Wu")
assistant3= ("AD390", "da678", "Amelia", "Duncan")
assistant4= ("UP265", "blabla1", "Ulysse", "Parker")

cursor.execute(sql, assistant1)
cursor.execute(sql, assistant2)
cursor.execute(sql, assistant3)
cursor.execute(sql, assistant4)

mydb.commit()

cursor.execute("SELECT shopkeeper_id, password, name, surname FROM ShopAssistant")
usercheck=cursor.fetchall()

def login():
    text = "user"
    text1= "password"
    socket_client.send(text.encode("utf-8"))
    user = socket_client.recv(1024).decode('utf-8')
    print (f"Username entered {user}")
    socket_client.send(text1.encode("utf-8"))
    password = socket_client.recv(1024).decode('utf-8')
    print (f"Password entered: {password}")

    if user == usercheck[0][0] and password == usercheck[0][1]:
        text1 = "good"
        name=usercheck[0][2]
        surname=usercheck[0][3]
        socket_client.send(text1.encode("utf-8"))
        socket_client.send(name.encode("utf-8"))
        socket_client.send(surname.encode("utf-8"))
    elif user == usercheck[1][0] and password == usercheck[1][1]:
        text1 = "good"
        name = usercheck[1][2]
        surname = usercheck[1][3]
        socket_client.send(text1.encode("utf-8"))
        socket_client.send(name.encode("utf-8"))
        socket_client.send(surname.encode("utf-8"))
    elif user == usercheck[2][0] and password == usercheck[2][1]:
        text1 = "good"
        name = usercheck[2][2]
        surname = usercheck[2][3]
        socket_client.send(text1.encode("utf-8"))
        socket_client.send(name.encode("utf-8"))
        socket_client.send(surname.encode("utf-8"))
    elif user == usercheck[3][0] and password == usercheck[3][1]:
        text1 = "good"
        name = usercheck[3][2]
        surname = usercheck[3][3]
        socket_client.send(text1.encode("utf-8"))
        socket_client.send(name.encode("utf-8"))
        socket_client.send(surname.encode("utf-8"))
    elif user == usercheck[4][0] and password == usercheck[4][1]:
        text1 = "good"
        name = usercheck[4][2]
        surname = usercheck[4][3]
        socket_client.send(text1.encode("utf-8"))
        socket_client.send(name.encode("utf-8"))
        socket_client.send(surname.encode("utf-8"))
    else:
        text1 = "bad"
        socket_client.send(text1.encode("utf-8"))
        login()

login()



def send(msg):  # send info to shop keepers
    for socket_client in shopkeepers:
        socket_client.send(msg.encode("utf-8"))



def status():  # update clients in the shop
    pass


def products():  # stock etc
    pass


def client():  # all clients and infos + their basket etc
    socket_client.send("clientinfo".encode("utf-8"))
    name=socket_client.recv(1024).decode("utf-8")
    position=socket_client.recv(1024).decode("utf-8")
    print (name, position)
    socket_client.send(("received".encode("utf-8")))
    sql = "INSERT INTO client (cname, position, status) VALUES (%s,%s,%s)"
    values=(f"{name}", f"{position}", "Start")
    cursor.execute(sql, values)
    mydb.commit()

    cursor.execute("SELECT cname, position, status")
    result = cursor.fetchall()
    for r in result:
        print (r)


msg1=socket_client.recv(1024).decode("utf-8")
while msg1 == "client":
    client()
    msg1 = socket_client.recv(1024).decode("utf-8")


def pupdate():  # update stocks
    pass


def sassistant():  # assistanct details, money made, etc
    pass
