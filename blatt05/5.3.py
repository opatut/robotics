from matplotlib import pyplot as plt
import numpy as np

# Define the functions as calculated
def L0(x):
    return -1.0/15.0 * x ** 3 + 9.0/15.0 * x ** 2 - 23.0/15.0 * x + 1
l0 = np.vectorize(L0)

# Define the functions as calculated
def L1(x):
    return 1.0/8.0 * x ** 3 - x ** 2 - 15.0/8.0 * x
l1 = np.vectorize(L1)

# Define the functions as calculated
def L2(x):
    return -1.0/12.0 * x ** 3 + 1.0/2.0 * x ** 2 - 5.0/12.0 * x
l2 = np.vectorize(L2)

# Define the functions as calculated
def L3(x):
    return 1.0/40.0 * x ** 3 - 1.0/10.0 * x ** 2 + 3.0/40.0 * x
l3 = np.vectorize(L3)

# Define the functions as calculated
def pI(x):
    return 23.0/40.0 * x ** 3 - 19.0/5.0 * x ** 2 + 209.0/40.0 * x + 1
pi = np.vectorize(pI)


# Create the x-axis range
x = np.linspace(-1.0, 6.0, num=250)

# Calculate the data points
l0a = l0(x)
l1a = l1(x)
l2a = l2(x)
l3a = l3(x)
pia = pi(x)

# Plot the data
plt.plot(x, l0a, label="$L_0$")
plt.plot(x, l1a, label="$L_1$")
plt.plot(x, l2a, label="$L_2$")
plt.plot(x, l3a, label="$L_3$")
plt.plot(x, pia, label="$p_I$")

# Enable grid
plt.grid()
# Position the legend
plt.legend(bbox_to_anchor=(0.185, 1))
# Save the graphic
plt.savefig("5-3.png")
