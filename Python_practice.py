print("Hello World")

counties = ["Arapahoe","Denver","Jefferson"]
print(counties)

#Create a dictionary
counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
print(counties_dict)

#Append Registered Voters
voting_data_dict = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]
print(voting_data_dict)

# If-else statements
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
     print("El Paso is not the list of counties.")
    
# Compound membership and logical operation using the list of counties.
counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
