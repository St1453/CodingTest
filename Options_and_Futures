'''
A graph of a combined position

The generated functions 𝑓,𝑔,ℎ
by the following codes represent buying a futures, buying a put option and the combined position, respectively.
'''



import numpy as np
import matplotlib.pyplot as plt

# Define functions f(x) and g(x)
def f(x):
    return x

def g(x):
    return -2 if x >= 0 else -x - 2

# Define the range of x values
x_values = np.linspace(-10, 10, 400)  # Adjust the range as needed

# Calculate the values of f(x) and g(x) for the given x values
f_values = f(x_values)
g_values = np.array([g(x) for x in x_values])

# Calculate the sum of f(x) and g(x)
h_values = f_values + g_values

# Plot the functions
plt.figure(figsize=(8, 6))
plt.plot(x_values, f_values, label='f(x) = x', color='blue')
plt.plot(x_values, g_values, label='g(x)', color='red')
plt.plot(x_values, h_values, label='h(x) = f(x) + g(x)', color='green')

# Add a legend
plt.legend()

# Add labels and title
plt.xlabel('Asset')
plt.ylabel('Profit')
plt.title('Graph of Functions f(x), g(x), and h(x)')

# Show the plot
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()
