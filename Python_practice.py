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

for county in counties:
    print(county)

#Iterate through a dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

#F-string function
## my_votes = int(input("How many votes did you get in the election? "))
## total_votes = int(input("What is the total votes in the election? "))
## percentage_votes = (my_votes / total_votes) * 100
## print("I received " + str(percentage_votes)+"% of the total votes.")

my_votes = int(input("How many votes did you get in the election? "))

total_votes = int(input("What is the total votes in the election? "))

print(f"I received {my_votes / total_votes * 100}% of the total votes.")


counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

# Multiple F-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (f"You received {candidate_votes} number of votes. " f"The total number of votes in the election was {total_votes}. "  f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)


