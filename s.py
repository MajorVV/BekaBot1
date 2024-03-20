import numpy as np

profit = 789
print("Profit:", profit)
binance = 0.0149
okey = 0.0155

tolerance = 0.01

# Creating numpy arrays for okx and bin volumes, using finer granularity.
okx_volumes = np.arange(1, 10000, 0.01)  # Example granularity of 0.01
bin_volumes = np.arange(1, 10000, 0.01)

found = False

# Vectorized computation for performance
for okx_volume in okx_volumes:
    calculated_profits = (okey * okx_volume) - (binance * bin_volumes)
    # Find indices where the calculated profit is within the tolerance of the target profit
    valid_indices = np.where(np.abs(calculated_profits - profit) < tolerance)[0]

    if valid_indices.size > 0:
        found = True
        # Pick the first valid index
        valid_index = valid_indices[0]
        print("First OKX volume:", okx_volume, "First BIN volume:", bin_volumes[valid_index])
        break

if not found:
    print("No solution found within the given ranges.")

