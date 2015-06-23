from matplotlib import pyplot as plt
import numpy as np

# time series
t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def N(i, k, time):
    """This function calculates the normalized basis spline as shown on slide 220"""
    if k == 1 and time >= i and time < i+1:
        return 1
    elif k == 1:
        return 0
    elif k > 1:
        return (time - t[i])/(t[i + k - 1] - t[i]) * N(i, k-1, time) + (t[i+k] - time)/(t[i+k] - t[i+1]) * N(i+1, k-1, time)


# With this the function can be applied to numpy arrays element wise
func = np.vectorize(N)

# Create an array with 200 evenly spaced numbers between 0 and 5
x = np.linspace(-0.1, 5.0, num=200)

# Use every k with k in [1, 2, 3, 4]
for k in range(1, 5):
    for i in range(0, 5-k):
        # Calculate all the numbers
        y = func(i, k, x)
        # Plot the function
        plt.plot(x, y, label="$N_{{{i}, {k}}}$".format(i=i, k=k))

    # Set the x-axis label
    plt.xlabel("time")
    # Set ranges for axes
    plt.xlim([-0.1, 4.1])
    plt.ylim([-0.05, 1.05])
    # Grid
    plt.grid()
    # Legend
    plt.legend()
    # Save the plot as png
    plt.savefig('5-1-k=' + str(k) + '.png')
    # Clear the figure
    plt.clf()
