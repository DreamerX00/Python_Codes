location = {"Akash":"RK Puram","Himanish":"Gurugram","Vikram":"FIMT NalaRoad","Karan":"ChorBazar","Ankita":"HongKong","Nitin":"Sames as Ankita","Duplicate": "Gurugram"}

print("\nThe Loaction of Akash is ",location["Akash"])

location["Akash"] = "Los Angelas"
print("\nThe Loaction of Akash is ",location["Akash"])

del location["Nitin"]
print("\n",location) 

print("\nThe Data type of the given Dictionary Items is -- >> ",type(location["Akash"]))
print("\nThe Data type of the given Dictionary is -- >> ",type(location))

print("\nThe original dictionary is : " + str(location))

temp = []
res = dict()
for key, val in location.items():
	if val not in temp:
		temp.append(val)
		res[key] = val

print("\nThe dictionary after values removal : " + str(res))




