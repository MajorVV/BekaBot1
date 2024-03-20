profit = 789
print("Profit:", profit)
binance = 0.0149
okey = 0.0155

# Defining a tolerance for floating-point comparison
tolerance = 0.01

found = False  # Flag to indicate if we've found the solution

# Using floating-point increments
for okx in range(1, 100000):  # Increasing range for finer granularity
    if found:
        break
    for bin in range(1, 100000):
        # Converting to float by dividing by 10000 for more granular search
        calculated_profit = (okey * (okx / 10000)) - (binance * (bin / 10000))
        if abs(calculated_profit - profit) < tolerance:  # Checking if within tolerance
            print("First OKX volume:", okx / 10000, "First BIN volume:", bin / 10000)
            found = True
            break

if not found:
    print("No solution found within the given ranges.")
