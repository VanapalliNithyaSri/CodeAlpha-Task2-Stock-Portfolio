stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    print("\nAvailable Stocks:")
    for stock in stock_prices:
        print(stock, ":", stock_prices[stock])

    stock_name = input("\nEnter stock name or 'DONE' to finish: ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock_name]
        investment = price * quantity

        total_investment += investment

        print("Investment for", stock_name, ":", investment)

    else:
        print("Stock not available.")

print("\n===== PORTFOLIO SUMMARY =====")
print("Total Investment:", total_investment)
with open("portfolio.txt", "w") as file:
    file.write("===== STOCK PORTFOLIO =====\n")
    file.write("Total Investment: " + str(total_investment))

print("Portfolio saved successfully!")