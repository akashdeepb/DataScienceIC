import pandas

# Read the CSV File present in the same Directory
data = pandas.read_csv("crop_production.csv")

# Create a Data Frame from the Data imported from CSV File
df = pandas.DataFrame(data)

print(df)   # Print the content of the DataFrame

print("Print all Coconut : ", df[df['Crop']=='Coconut '])       # Print all the Rows containing Coconut as Crop

print("Max Arecanut : ", df[df['Crop']=='Arecanut']['Production'].max())     # Print Max of the Row with Crop as Arecanut

print("Max of Coconut : ",df['Area'].sum())     # Print Max of the Row containing Coconut as Crop

print("Sum of Coconut : ",df[df['Crop']=='Coconut ']['Area'].sum())     # Print the Sum of the Area of Coconut as Crop
