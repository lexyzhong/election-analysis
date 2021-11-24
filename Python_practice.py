voting_data=[]
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.insert(1,{"county":"El Paso","registered_voters":4611489})
del voting_data["county"=="Arapahoe"]
print(voting_data)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for key, value in counties_dict.items():
    print(f"{key} county has {value:,} registered voters.")

voting_data2 = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county_dict2 in voting_data2:
    print(f"{county_dict2['county']} county has {county_dict2['registered_voters']:,} registered voters.")