# Stock Portfolio Tracker

##  Project Overview

This project is a simple Stock Portfolio Tracker developed using Python.

The program allows the user to select stocks, enter the quantity of each stock, and calculate the total investment value.

It also saves the portfolio summary into a text file.

##  Objective

The main objective of this project is to create a simple Python program that can:

- Display available stocks and their prices
- Accept stock names from the user
- Accept the quantity of stocks
- Calculate the investment amount
- Calculate the total investment
- Save the portfolio summary in a text file

## Technologies Used

- Python
- Visual Studio Code
- File Handling

##  How the Program Works

1. The program displays the available stocks and their prices.
2. The user enters the stock name.
3. The program asks for the quantity of the stock.
4. The investment amount is calculated using:

   `Investment = Stock Price × Quantity`

5. The investment amount is added to the total investment.
6. The user can enter `DONE` to finish adding stocks.
7. The program displays the total investment.
8. The total investment is saved in `portfolio.txt`.

## 💻 Example Input and Output

### Input

```text
Available Stocks:
AAPL : 180
TSLA : 250
GOOGL : 140
MSFT : 420
AMZN : 190

Enter stock name or 'DONE' to finish: AAPL
Enter quantity: 5

Investment for AAPL : 900

===== PORTFOLIO SUMMARY =====
Total Investment: 900
Portfolio saved successfully!

##  Features

- Displays available stocks and their prices
- Allows the user to select stocks
- Accepts the quantity of each stock
- Calculates individual investment amounts
- Calculates the total portfolio investment
- Handles multiple stock entries
- Saves the portfolio summary to a text file
- Provides a simple command-line interface
##  Python Concepts Used

This project demonstrates:

- Variables
- Dictionaries
- User input
- `if-else` statements
- `while` loop
- Arithmetic operations
- String methods
- File handling
- Functions