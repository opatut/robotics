from matplotlib import pyplot as plt
import numpy as np

# (a)
def a(t):
    return 1.0 + t
a = np.vectorize(a)

# (b)
def b(t):
    return t + 1 + t**2 * 1.0/2.0
b = np.vectorize(b)


# Create the x-axis range
t = np.linspace(0.0, 20.0, num=250)

# Calculate the data points
a_array = a(t)
b_array = b(t)

# Plot the data
plt.plot(t, a_array, label="(a)")
plt.plot(t, b_array, label="(b)")

# Enable grid
plt.grid()
# Labels
plt.xlabel("time")
plt.ylabel("response")
# Position the legend
plt.legend(bbox_to_anchor=(0.185, 1))
# Save the graphic
plt.savefig("5-4.png")
