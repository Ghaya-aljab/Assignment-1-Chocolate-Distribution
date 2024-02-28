#I took my screenshots from sagemath (cocal) since matplot doesnt work on my pycharm
#This code has the graphs for distributions, and sorting
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data provided by you
data = {
    "n": [0, 50, 100, 150, 200, 250, 300, 350, 400],
    "Iterative": [5.00e-06, 3.90e-05, 7.60e-05, 1.21e-04, 1.38e-04, 1.64e-04, 2.12e-04, 2.43e-04, 2.71e-04],
    "Recursive": [1.00e-06, 4.40e-05, 9.10e-05, 1.34e-04, 1.79e-04, 2.27e-04, 2.77e-04, 3.80e-04, 3.83e-04],
    "Sort by Weight": [0.00e+00, 1.22e-04, 2.58e-04, 4.12e-04, 5.61e-04, 6.12e-04, 7.04e-04, 1.18e-03, 1.03e-03],
    "Sort by Price": [0.00e+00, 1.15e-04, 2.69e-04, 4.04e-04, 4.85e-04, 6.09e-04, 7.68e-04, 1.19e-03, 1.04e-03],
}

# Creating DataFrame from the provided data
df = pd.DataFrame(data)

# Fill missing values with NaN
df = df.fillna(value=np.nan)

# List of methods to plot, which are the columns of the DataFrame except for 'n'
methods = df.columns[1:]

# Define the plot function
def plot_method_performance(df, method_name):
    plt.figure(figsize=(10, 5))
    plt.plot(df['n'], df[method_name], 'o-', label=method_name)
    plt.xlabel('Number of Students (n)')
    plt.ylabel('Time (seconds)')
    plt.title(f'Time Complexity of {method_name} Method')
    plt.legend()
    plt.grid(True)
    # Format the y-axis ticks in scientific notation
    plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
    plt.show()

# Iterate over each method and plot using the defined function
for method in methods:
    plot_method_performance(df, method)

#This code has graph for searching (I had to make this sperate because the values were small, and it wasnt able to create a graph on the other code)
import matplotlib.pyplot as plt
import numpy as np

students = np.array([0, 50, 100, 150, 200, 250, 300, 350, 400])
search_by_weight = np.array([0.000000374857, 0.00000166614, 0.00000187499, 0.00000187499, 0.00000195811, 0.0000057919, 0.00000175019, 0.00000241701, 0.000003458])
search_by_price = np.array([0.000000415836, 0.00000120816, 0.00000154087, 0.00000149989, 0.00000149989, 0.00000183308, 0.00000225008, 0.00000212481, 0.00000220793])

plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.semilogy(students, search_by_weight, marker='o', label='Search by Weight', linestyle='-')
plt.xlabel('Number of Students (n)')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of Search by Weight Method')
plt.legend()
plt.ylim(min(search_by_weight) * 0.5, max(search_by_weight) * 2)  # Set y-axis limits

plt.subplot(2, 1, 2)
plt.semilogy(students, search_by_price, marker='o', color='orange', label='Search by Price', linestyle='-')
plt.xlabel('Number of Students (n)')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of Search by Price Method')
plt.legend()
plt.ylim(min(search_by_price) * 0.5, max(search_by_price) * 2)  # Set y-axis limits

plt.tight_layout()
plt.show()