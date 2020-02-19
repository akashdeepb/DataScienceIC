import pandas

#Read the CSV File present in the same Directory
data = pandas.read_csv("crop_production.csv")

#Create a Data Frame from the Data imported from CSV File
df = pandas.DataFrame(data)

print(df)   # Print the content of the DataFrame

print(df[df['Crop']=='Coconut '])       # Print all the Rows containing Coconut as Crop


print(df[df['Crop']=='Arecanut'].max())     #Print Max of the Row with Crop as Arecanut
