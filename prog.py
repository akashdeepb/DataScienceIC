import pandas

data = pandas.read_csv("crop_production.csv")
df = pandas.DataFrame(data)
print(df[df['Crop']=='Coconut '])       # Print all the Rows containing Coconut as Crop


print(df[df['Crop']=='Arecanut'].max())     #Print Max of the Row with Crop as Arecanut
