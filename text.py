# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

# Input stock data from user
while True:
    symbol = input("Enter stock symbol (or 'done' to finish): ").upper()
    if symbol == 'DONE':
        break
    if symbol not in stock_prices:
        print("Stock symbol not recognized. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {symbol}: "))
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
print("\n📊 Portfolio Summary:")
for symbol, quantity in portfolio.items():
    price = stock_prices[symbol]
    investment = price * quantity
    total_investment += investment
    print(f"{symbol}: {quantity} shares x ${price} = ${investment}")

print(f"\n💰 Total Investment: ${total_investment}")

# Optional: Save to file
save = input("\nDo you want to save the portfolio to a file? (y/n): ").lower()
if save == 'y':
    file_type = input("Enter file type (txt/csv): ").lower()
    filename = f"portfolio.{file_type}"
    with open(filename, "w") as f:
        if file_type == "csv":
            f.write("Stock,Quantity,Price,Investment\n")
            for symbol, quantity in portfolio.items():
                price = stock_prices[symbol]
                investment = price * quantity
                f.write(f"{symbol},{quantity},{price},{investment}\n")
            f.write(f",,,Total,{total_investment}\n")
        else:
            f.write("Stock Portfolio Summary\n")
            for symbol, quantity in portfolio.items():
                price = stock_prices[symbol]
                investment = price * quantity
                f.write(f"{symbol}: {quantity} x ${price} = ${investment}\n")
            f.write(f"\nTotal Investment: ${total_investment}\n")
    print(f"✅ Portfolio saved to {filename}")
