import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
data = pd.read_csv("student_data.csv")

# Show column names
print(data.columns)

# Show first rows
print(data.head())

# Show graph

plt.show()