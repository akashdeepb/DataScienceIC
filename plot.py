import pandas
import matplotlib.pyplot as plt

# Read the CSV File containing Crop Production Data
data = pandas.read_csv("crop_production.csv")

# Create a DataFrame of the Data
df = pandas.DataFrame(data)
cashewData = df[df['Crop']=='Cashewnut']
cashewData=cashewData.sort_values(by=['Crop_Year'])     # Sort data using Crop Year
cashewData.plot(x="Crop_Year",y="Production",kind="bar")   # Plot a Graph
plt.show()
