counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
x = 5
y = 5
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties")
else:
    print("Araphoe or El Paso is not in the list of counties")
if "Arapahoe" or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties")
else:
    print("Arapahoe and El Paso are not in the list.")
if "Araphoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Only Arapahoe is in the list of counties and El Paso is not")
for county in counties:
    print(county)
for num in range(5):
    print(num)
for i in range(len(counties)):
    print(counties[i])
voting_data = [{"county":"Arapahoe","regsitered voters":"42289",},
                {"county":"Denver","registered_voters":"463353"}, 
                {"county":"Jefferson","registered_voters":"432438"}]
for county_dict in voting_data:
    print(county_dict)
for i in range(len(voting_data)):
    print(voting_data[i])
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
print(f"I received {my_votes / total_votes * 100}% of the total votes")  
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)