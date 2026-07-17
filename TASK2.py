# Hardcoded stock price dictionary
stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "AMZN": 175, "MSFT": 400}

portfolio = {}
total_investment = 0.0

print("Welcome to your Stock Portfolio Tracker!")
print(f"Available stocks: {list(stock_prices.keys())}")

# Collect user input
while True:
    stock = input("\nEnter stock ticker (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    
    if stock not in stock_prices:
        print("Stock not found in our hardcoded dictionary. Try again.")
        continue
        
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity < 0:
            print("Quantity cannot be negative.")
            continue
            
        # Add or update portfolio
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_investment += stock_prices[stock] * quantity
    except ValueError:
        print("Invalid input! Please enter a whole number for quantity.")

# Display results
print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    print(f"{stock}: {qty} shares @ ${price} each = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional file saving
save_choice = input("\nWould you like to save this summary to a portfolio.txt file? (y/n): ").lower()
if save_choice == 'y':
    with open("portfolio.txt", "w") as file:
        file.write("--- Portfolio Summary ---\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("Portfolio successfully saved to portfolio.txt!")