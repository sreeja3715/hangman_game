stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 320,
    "AMZN": 140
}

total_value = 0

n = int(input("How many stocks do you want to enter? "))

for i in range(n):
    stock = input("Enter stock symbol: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        value = stock_prices[stock] * quantity
        total_value += value
    else:
        print("Stock not found")

print("Total Portfolio Value:", total_value)