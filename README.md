# PROJECT-1
Restaurant Billing System – Python Project
---------------Project Overview-----------------

This is an interactive Restaurant Billing System built using Python.
The program allows customers to:

1.View a menu

2.Select food items

3.Enter quantities

4.Add multiple items

5.Apply a discount code

6.View the final bill with subtotal, discount, and total amount

->It also includes user-friendly prompts, input validation, and a final thank-you message.

#Features:

~ Greets the user by name

~ Displays a menu with food items and prices

~ Accepts multiple orders

~ Validates quantity input

~ Calculates total bill

~ Supports a discount code (CODE10)

~ Shows detailed final bill

~ Clean and easy-to-use console interface

🧾 Menu Details:
Item	   Price (Rs)
Burger 🍔	70
Coffee ☕   80
Maggie 🍜	40
Pasta 🍝	130
Pizza 🍕	120

#Technologies Used:
Python 3.x
No external libraries are required.

#How to Run the Project?
1. Install Python

Make sure Python 3 is installed on your system.

2. Save the Code

Create a file named restaurant.py and paste your code into it.

3. Run the Program

Open a terminal or command prompt and type:

python restaurant.py

# How It Works
1. Greeting:
The program asks for your name and displays a welcome message.

2. Ordering System:
->Shows the menu

->Allows you to choose items

->Asks for quantity

->Allows multiple orders

3. Discount Code:

->If the user enters CODE10, a 10% discount is applied.

4. Final Bill

->The bill displays:

(a) Subtotal

(b)Discount (if applied)

(c)Final payable amount

#Example Interaction (Simplified)
Enter your name: Rahul
Welcome to our restaurant, Rahul!

Here's the menu:
Burger = Rs70
Coffee = Rs80
...

Please select your first item: Pizza
Great Pizza selected.
please select the quantity: 2

Do you want to order something else? Yes
Please select your next item: Coffee
please select the quantity: 1

Have a discount code? CODE10
Discount applied!

--- FINAL BILL ---
Subtotal: Rs320
Discount: -Rs32
FINAL AMOUNT DUE: Rs288

📜 Discount Information
Code	Discount
CODE10	10% off

## Future Improvements (Optional Ideas):

->Add GST calculation

->Add order review before final bill

->Add option to remove items

->Add graphical interface (Tkinter or PyQt)

->Save bill history in a file

# Contributing

Feel free to add improvements or customization.
Pull requests are welcome!

#License

This project is free to use for learning and educational purposes.
