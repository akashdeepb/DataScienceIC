import pandas

data = pandas.read_csv("crop_production.csv")
df = pandas.DataFrame(data)
print(df[df['Crop']=='Coconut '])       # Print all the Rows containing Coconut as Crop
