# CST1510 Programming for data communication and networks 2021/22 coursework

## Brief Task Description
Design and implement 'Store automatic system' similar to the Apple store, allowing the staff 
to communicate and provide an excellent customer experience. 
You should build a Client/ Server-side software system in Python to interact with the user (shop 
assistant) on the client-side and add, remove or update data on the server-side.
The client-site part of the program should have an intuitive user interface to start a client 
request, view available items and prices, create order (add, remove item), manage order and 
payment, close the request, and view the client (shopkeeper) record for the day. The software 
should interact with the current stockpile of a product and update the inventory based on the 
orders done by the client. The server program should interact with one client or multiple clients 
for the advanced version of the software.

## Scenario
'Shop automatic system' allows the staff/shopkeeper to communicate and provide an excellent 
customer experience. When a potential customer arrives at a store, he/she is asked by the 
shopkeeper for a name and the customer is added to the system. Then, next available staff 
member can approach the customer and proceed with the service. The shopkeepers are the 
primary users of the system, and they can view the current stock, create orders, add more 
items into a basket, submit the order, and make a payment. Each client/shopkeeper will see 
his/her daily activity.

## Scope
The Shop automating system must have four main options:
a. New customer request
b. Current stock 
c. Order
d. Client/Shopkeeper dashboard 

### a)The ‘New customer request’ option should allow the client/shopkeeper to;
-Enter the customer’s name and mark the geographical place (position in the shop) 
where the customer is. (The list will be sent to a server for all shop assistants to see)
-Show list of current customers waiting to be served (Including name and location of the 
clients). 
-Option to add the Client/salesperson name when the customer get to be serve by a 
salesperson (This should be sent to a server for the customer to be removed from the 
list of customers waiting to be served)

### b)The 'Current stock' option should allow viewing of all of the available stock. The stock should be stored in databases (text, csv or MySQL) on the server-side and can be retrieved by the client. Each item should have its name, price, colour and number of items available. 

### c) The 'Order' functionalities should be available in the 'current stock' option. (Feel free to suggest your implementation)
When a customer wants to make an order, there is an option of; 
- adding an item to a basket, 
- adding more items to a basket and/or finish and pay
- cancel/delete the item in the basket
- finish and pay
The receipt should be displayed on the client-side of the application for the customer to see it.
The order should be sent to a server-side where; stock, orders and shopkeeper data storage 
should be updated accordingly.

### d) The 'Client Dashboard' option should allow the client/shopkeeper to see his/her daily summary including amount of money their make in a day and commission.

## Software Description
Start by designing your shop system using a UML diagram. The UML diagram does not have 
to be using precise UML notations; however it should have a graphical illustration of the 
whole system.

### Data storage:
You could have a simple .txt file or .csv file or full implementation of MySQL data containing 
the following: 
Customer: customer name, geographical position, status (start, finish), shopkeeper’s name.
Available stock. The file should contain the product id number, name, colour, price (more 
attributes if you wish).
Shopkeepers including; shopkeeper id, name, surname, date/workday, sold item-name, item 
price and commission amount. 
Each order contains all data from the receipt. For example, order id, item name, item price, 
tax, buyer’s name, surname, and if the payment was cash or card. 
### Server
Design and implement a (command line) server program that connects to the previously 
implemented database (in text or CSV or MySQL). The Server should have methods to add, 
remove, or update the data described above and communicate with the client accordingly.
### Client
Design and implement Python file to be used as the client. The client should contain the 
Shopping system user Interface (UI), in GUI or text-based.
This GUI or text-based program should allow the user/shopkeeper to implement all four
functionalities described above in the scope (point 4) and consequently communicate with the 
server

## GUI 
Login:
![Screenshot 2024-03-02 124029](https://github.com/doolun1312/Python-Store_automatic_system/assets/132755399/7f51ef55-664d-409d-8be4-d8253d886027)

Menu:
![Screenshot 2024-03-02 124311](https://github.com/doolun1312/Python-Store_automatic_system/assets/132755399/a3735901-3332-47cc-8cc2-bd8e80350d6b)
